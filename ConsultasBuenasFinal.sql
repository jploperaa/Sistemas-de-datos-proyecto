-- =====================================================
-- CONSULTAS SQL - PROYECTO CLUB DE LECTURA
-- Basado en tu modelo y dataset (Usuario, Libro, Publicacion, Reseña, Venta, Intercambio, Catalogo)
-- =====================================================


-- 1) Publicaciones con su libro y usuario que la creó
SELECT 
  p.ID_publicacion,
  p.modalidad,
  p.estado,
  p.precio,
  p.fecha_publicacion,
  u.nombre AS usuario,
  l.titulo,
  l.autor
FROM Publicacion AS p
JOIN Usuario   AS u ON u.ID_usuario = p.ID_usuario
JOIN Libro     AS l ON l.ID_libro   = p.ID_libro AND l.ISBN = p.ISBN
ORDER BY p.fecha_publicacion;



-- 2) Libros publicados por modalidad (Venta o Intercambio)
SELECT 
  p.modalidad,
  COUNT(*) AS total_libros,
  ROUND(AVG(p.precio),2) AS precio_promedio
FROM Publicacion AS p
GROUP BY p.modalidad;



-- 3) Libros ordenados por título y su autor
SELECT 
  l.ID_libro,
  l.ISBN,
  l.titulo,
  l.autor,
  l.genero
FROM Libro AS l
ORDER BY l.titulo ASC;



-- 4) Reseñas con autor y libro reseñado
SELECT 
  r.ID_reseña,
  l.titulo,
  u.nombre AS autor_reseña,
  r.calificacion,
  r.contenido,
  r.fecha_reseña
FROM Reseña AS r
JOIN Usuario AS u ON u.ID_usuario = r.ID_usuario_autor
JOIN Libro   AS l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
ORDER BY r.fecha_reseña DESC;



-- 5) Libros mejor calificados (promedio + cantidad reseñas)
SELECT 
  l.titulo,
  l.autor,
  ROUND(AVG(r.calificacion),2) AS promedio,
  COUNT(r.ID_reseña) AS cantidad_reseñas
FROM Reseña AS r
JOIN Libro AS l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
GROUP BY l.titulo, l.autor
ORDER BY promedio DESC, cantidad_reseñas DESC;



-- 6) Intercambios por libro y estado
SELECT 
  l.titulo,
  l.autor,
  i.estado,
  COUNT(i.ID_intercambio) AS total_intercambios
FROM Intercambio AS i
JOIN Libro AS l ON l.ID_libro = i.ID_libro AND l.ISBN = i.ISBN
GROUP BY l.titulo, l.autor, i.estado
ORDER BY l.titulo, i.estado;



-- 7) Libros más intercambiados (con conteo)
SELECT 
  l.titulo,
  l.autor,
  COUNT(i.ID_intercambio) AS veces_intercambiado
FROM Intercambio AS i
JOIN Libro AS l ON l.ID_libro = i.ID_libro AND l.ISBN = i.ISBN
GROUP BY l.titulo, l.autor
ORDER BY veces_intercambiado DESC;



-- 8) Ventas con libro y usuario vendedor
SELECT 
  v.ID_venta,
  v.fecha_venta,
  v.estado,
  v.precio,
  u.nombre AS vendedor,
  l.titulo,
  l.autor
FROM Venta AS v
JOIN Usuario AS u ON u.ID_usuario = v.ID_usuario
JOIN Libro   AS l ON l.ID_libro = v.ID_libro AND l.ISBN = v.ISBN
ORDER BY v.fecha_venta;



-- 9) Ventas agrupadas por libro (veces vendido e ingresos)
SELECT 
  l.titulo,
  l.autor,
  COUNT(v.ID_venta) AS total_ventas,
  SUM(v.precio)     AS total_ingresos
FROM Venta AS v
JOIN Libro AS l ON l.ID_libro = v.ID_libro AND l.ISBN = v.ISBN
GROUP BY l.titulo, l.autor
ORDER BY total_ventas DESC, total_ingresos DESC;



-- 10) Ventas por usuario (cuántas y cuánto dinero)
SELECT 
  u.nombre,
  COUNT(v.ID_venta) AS total_ventas,
  SUM(v.precio)     AS total_ingresos
FROM Usuario AS u
JOIN Venta   AS v ON v.ID_usuario = u.ID_usuario
GROUP BY u.nombre
ORDER BY total_ventas DESC, total_ingresos DESC;



-- 11) Intercambios por usuario
SELECT 
  u.nombre,
  COUNT(i.ID_intercambio) AS total_intercambios
FROM Usuario AS u
JOIN Intercambio AS i ON i.ID_usuario = u.ID_usuario
GROUP BY u.nombre
ORDER BY total_intercambios DESC, u.nombre;



-- 12) Publicaciones agrupadas por catálogo y modalidad
SELECT 
  c.nombre AS catalogo,
  p.modalidad,
  COUNT(*) AS total_publicaciones,
  ROUND(AVG(p.precio),2) AS precio_promedio
FROM Publicacion AS p
JOIN Catalogo AS c ON c.ID_catalogo = p.ID_catalogo
GROUP BY c.nombre, p.modalidad
ORDER BY c.nombre, p.modalidad;



-- 13) Usuarios con reseñas hechas (conteo)
SELECT 
  u.nombre,
  COUNT(r.ID_reseña) AS total_reseñas
FROM Usuario AS u
JOIN Reseña  AS r ON r.ID_usuario_autor = u.ID_usuario
GROUP BY u.nombre
ORDER BY total_reseñas DESC;



-- 14) Libros con su estado actual en publicación
SELECT 
  l.titulo,
  p.estado,
  p.modalidad,
  p.precio,
  u.nombre AS propietario
FROM Publicacion AS p
JOIN Libro AS l ON l.ID_libro = p.ID_libro AND l.ISBN = p.ISBN
JOIN Usuario AS u ON u.ID_usuario = p.ID_usuario
ORDER BY p.estado, p.modalidad;



-- 15) Reseñas con libro y calificación mayor a 4
SELECT 
  r.ID_reseña,
  l.titulo,
  r.calificacion,
  r.contenido,
  u.nombre AS autor_reseña
FROM Reseña AS r
JOIN Libro AS l ON l.ID_libro = r.ID_libro AND l.ISBN = r.ISBN
JOIN Usuario AS u ON u.ID_usuario = r.ID_usuario_autor
WHERE r.calificacion >= 4
ORDER BY r.calificacion DESC, l.titulo;

-- =====================================================
-- FIN DEL ARCHIVO
-- =====================================================
