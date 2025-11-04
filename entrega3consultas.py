import mysql.connector

# ==============================================
# CONEXIÓN A LA BASE DE DATOS
# ==============================================
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   ## contrasena de la base de datos 
        database="" ## nombre de la base de datos 
    )

# ==============================================
# FUNCIONES PARA LAS 15 CONSULTAS
# ==============================================

def ejecutar_consulta(sql, params=None):
    """Ejecuta una consulta y muestra los resultados"""
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(sql, params or ())
        filas = cur.fetchall()
        print("\n--- Resultado ---")
        if not filas:
            print("⚠️ No se encontraron resultados.")
        else:
            for fila in filas:
                print(fila)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# ========================
# CONSULTAS DEL PROYECTO
# ========================

def q1_publicaciones():
    sql = """
    SELECT p.ID_publicacion, p.modalidad, p.estado, p.precio, p.fecha_publicacion,
           u.nombre AS usuario, l.titulo, l.autor
    FROM Publicacion p
    JOIN Usuario u ON u.ID_usuario = p.ID_usuario
    JOIN Libro l ON l.ID_libro = p.ID_libro AND l.ISBN = p.ISBN
    ORDER BY p.fecha_publicacion;
    """
    ejecutar_consulta(sql)

def q2_modalidad():
    sql = """
    SELECT p.modalidad, COUNT(*) AS total_libros, ROUND(AVG(p.precio),2) AS precio_promedio
    FROM Publicacion p
    GROUP BY p.modalidad;
    """
    ejecutar_consulta(sql)

def q3_libros():
    sql = "SELECT ID_libro, ISBN, titulo, autor, genero FROM Libro ORDER BY titulo ASC;"
    ejecutar_consulta(sql)

def q4_resenas():
    sql = """
    SELECT r.ID_reseña, l.titulo, u.nombre AS autor_reseña, r.calificacion, r.contenido, r.fecha_reseña
    FROM Reseña r
    JOIN Usuario u ON u.ID_usuario = r.ID_usuario_autor
    JOIN Libro l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
    ORDER BY r.fecha_reseña DESC;
    """
    ejecutar_consulta(sql)

def q5_libros_calificados():
    sql = """
    SELECT l.titulo, l.autor, ROUND(AVG(r.calificacion),2) AS promedio, COUNT(r.ID_reseña) AS cantidad
    FROM Reseña r
    JOIN Libro l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
    GROUP BY l.titulo, l.autor
    ORDER BY promedio DESC, cantidad DESC;
    """
    ejecutar_consulta(sql)

def q6_intercambios_libro():
    sql = """
    SELECT l.titulo, l.autor, i.estado, COUNT(i.ID_intercambio) AS total
    FROM Intercambio i
    JOIN Libro l ON l.ID_libro = i.ID_libro AND l.ISBN = i.ISBN
    GROUP BY l.titulo, l.autor, i.estado
    ORDER BY l.titulo;
    """
    ejecutar_consulta(sql)

def q7_libros_mas_intercambiados():
    sql = """
    SELECT l.titulo, l.autor, COUNT(i.ID_intercambio) AS veces_intercambiado
    FROM Intercambio i
    JOIN Libro l ON l.ID_libro = i.ID_libro AND l.ISBN = i.ISBN
    GROUP BY l.titulo, l.autor
    ORDER BY veces_intercambiado DESC;
    """
    ejecutar_consulta(sql)

def q8_ventas_detalle():
    sql = """
    SELECT v.ID_venta, v.fecha_venta, v.estado, v.precio, u.nombre AS vendedor, l.titulo, l.autor
    FROM Venta v
    JOIN Usuario u ON u.ID_usuario = v.ID_usuario
    JOIN Libro l ON l.ID_libro = v.ID_libro AND l.ISBN = v.ISBN
    ORDER BY v.fecha_venta;
    """
    ejecutar_consulta(sql)

def q9_ventas_por_libro():
    sql = """
    SELECT l.titulo, l.autor, COUNT(v.ID_venta) AS total_ventas, SUM(v.precio) AS total_ingresos
    FROM Venta v
    JOIN Libro l ON l.ID_libro = v.ID_libro AND l.ISBN = v.ISBN
    GROUP BY l.titulo, l.autor
    ORDER BY total_ventas DESC;
    """
    ejecutar_consulta(sql)

def q10_ventas_por_usuario():
    sql = """
    SELECT u.nombre, COUNT(v.ID_venta) AS total_ventas, SUM(v.precio) AS total_ingresos
    FROM Usuario u
    JOIN Venta v ON v.ID_usuario = u.ID_usuario
    GROUP BY u.nombre
    ORDER BY total_ventas DESC;
    """
    ejecutar_consulta(sql)

def q11_intercambios_usuario():
    sql = """
    SELECT u.nombre, COUNT(i.ID_intercambio) AS total_intercambios
    FROM Usuario u
    JOIN Intercambio i ON i.ID_usuario = u.ID_usuario
    GROUP BY u.nombre
    ORDER BY total_intercambios DESC;
    """
    ejecutar_consulta(sql)

def q12_publicaciones_catalogo():
    sql = """
    SELECT c.nombre AS catalogo, p.modalidad,
           COUNT(*) AS total_publicaciones,
           ROUND(AVG(p.precio),2) AS precio_promedio
    FROM Publicacion p
    JOIN Catalogo c ON c.ID_catalogo = p.ID_catalogo
    GROUP BY c.nombre, p.modalidad
    ORDER BY c.nombre;
    """
    ejecutar_consulta(sql)

def q13_resenas_usuario():
    sql = """
    SELECT u.nombre, COUNT(r.ID_reseña) AS total_reseñas
    FROM Usuario u
    JOIN Reseña r ON r.ID_usuario_autor = u.ID_usuario
    GROUP BY u.nombre
    ORDER BY total_reseñas DESC;
    """
    ejecutar_consulta(sql)

def q14_publicaciones_estado():
    sql = """
    SELECT l.titulo, p.estado, p.modalidad, p.precio, u.nombre AS propietario
    FROM Publicacion p
    JOIN Libro l ON l.ID_libro = p.ID_libro AND l.ISBN = p.ISBN
    JOIN Usuario u ON u.ID_usuario = p.ID_usuario
    ORDER BY p.estado;
    """
    ejecutar_consulta(sql)

def q15_resenas_alta():
    sql = """
    SELECT r.ID_reseña, l.titulo, r.calificacion, r.contenido, u.nombre AS autor
    FROM Reseña r
    JOIN Libro l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
    JOIN Usuario u ON u.ID_usuario = r.ID_usuario_autor
    WHERE r.calificacion >= 4
    ORDER BY r.calificacion DESC;
    """
    ejecutar_consulta(sql)


# ==============================================
# MENÚ PRINCIPAL
# ==============================================
def menu_consultas():
    while True:
        print("\n===== MENÚ DE CONSULTAS SQL =====")
        print("1) Publicaciones con usuario y libro")
        print("2) Libros publicados por modalidad")
        print("3) Listar libros (ordenados)")
        print("4) Reseñas con autor y libro")
        print("5) Libros mejor calificados")
        print("6) Intercambios por libro y estado")
        print("7) Libros más intercambiados")
        print("8) Ventas con detalle")
        print("9) Ventas agrupadas por libro")
        print("10) Ventas por usuario")
        print("11) Intercambios por usuario")
        print("12) Publicaciones por catálogo")
        print("13) Usuarios con reseñas")
        print("14) Libros con estado actual")
        print("15) Reseñas con calificación >= 4")
        print("0) Salir")
        op = input("Opción: ").strip()
        if op == "1": q1_publicaciones()
        elif op == "2": q2_modalidad()
        elif op == "3": q3_libros()
        elif op == "4": q4_resenas()
        elif op == "5": q5_libros_calificados()
        elif op == "6": q6_intercambios_libro()
        elif op == "7": q7_libros_mas_intercambiados()
        elif op == "8": q8_ventas_detalle()
        elif op == "9": q9_ventas_por_libro()
        elif op == "10": q10_ventas_por_usuario()
        elif op == "11": q11_intercambios_usuario()
        elif op == "12": q12_publicaciones_catalogo()
        elif op == "13": q13_resenas_usuario()
        elif op == "14": q14_publicaciones_estado()
        elif op == "15": q15_resenas_alta()
        elif op == "0":
            print("Saliendo del menú de consultas...")
            break
        else:
            print("❌ Opción no válida.")


# ==============================================
# EJECUCIÓN PRINCIPAL
# ==============================================
if __name__ == "__main__":
    print("Conexión con la base de datos 'quiz3' establecida correctamente.")
    menu_consultas()
