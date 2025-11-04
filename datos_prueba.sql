-- =========================
-- USUARIOS
-- =========================
INSERT INTO Usuario (nombre, correo, telefono, password, ciudad)
VALUES 
('Juan Pérez', 'juan@example.com', '3001112233', 'passjuan', 'Medellín'),
('María Gómez', 'maria@example.com', '3002223344', 'passmaria', 'Bogotá'),
('Carlos Ruiz', 'carlos@example.com', '3003334455', 'passcarlos', 'Cali'),
('Luisa Fernández', 'luisa@example.com', '3004445566', 'passluisa', 'Barranquilla'),
('Andrés Mejía',    'andres@example.com', '3005556677', 'passandres', 'Bucaramanga');


-- =========================
-- CATÁLOGOS
-- =========================
INSERT INTO Catalogo (nombre, descripcion, fecha_creacion)
VALUES 
('Catálogo General', 'Colección de todos los libros publicados', '2025-01-01'),
('Novedades', 'Libros recién agregados', '2025-02-01'),
('Clásicos',           'Obras clásicas universales',           '2025-02-15'),
('Intercambio Activo', 'Libros disponibles para intercambio',  '2025-02-20'),
('Ofertas',            'Libros con descuento',                 '2025-02-25');

-- =========================
-- CLUBES DE LECTURA
-- =========================
INSERT INTO Club_lectura (nombre, descripcion, estado, fecha_creacion)
VALUES
('Club Realismo', 'Discusión de novelas realistas', 'Activo', '2025-01-15'),
('Club Ciencia Ficción', 'Explorar universos de sci-fi', 'Activo', '2025-01-20'),
('Club Historia',  'Historia y biografías',      'Activo', '2025-01-25'),
('Club Fantasía',  'Mundos fantásticos y mitos', 'Activo', '2025-01-28'),
('Club Ensayo',    'Ensayos y no ficción',       'Activo', '2025-01-30');

-- =========================
-- LIBROS
-- =========================
INSERT INTO Libro (ID_libro, ISBN, titulo, autor, año_publicacion, genero, modalidad, resumen, propietario, ID_usuario_recibe)
VALUES
(1, '978-3-16-148410-0', 'Cien Años de Soledad', 'Gabriel García Márquez', 1967, 'Realismo Mágico', 'Intercambio', 'Novela clásica de la literatura latinoamericana', 'Juan Pérez', 1),
(2, '978-1-4028-9462-6', '1984', 'George Orwell', 1949, 'Distopía', 'Venta', 'Una sociedad totalitaria vigilada en extremo', 'María Gómez', 2),
(3, '978-0-7432-7356-5', 'El amor en los tiempos del cólera', 'Gabriel García Márquez', 1985, 'Romance',          'Intercambio', 'Historia de amores perdurables', 'Carlos Ruiz',   3),
(4, '978-0-452-28423-4', 'Fahrenheit 451',                    'Ray Bradbury',            1953, 'Ciencia ficción', 'Venta',       'Sociedad que quema libros',       'Juan Pérez',    1),
(5, '978-84-376-0494-7', 'Don Quijote de la Mancha',          'Miguel de Cervantes',     1605, 'Clásico',         'Venta',       'Aventuras del ingenioso hidalgo', 'María Gómez',   2);

-- =========================
-- PUBLICACIONES
-- =========================
INSERT INTO Publicacion (modalidad, estado, fecha_publicacion, precio, ID_usuario, ID_catalogo, ID_libro, ISBN)
VALUES
('Intercambio', 'Disponible', '2025-03-01', 0.00, 1, 1, 1, '978-3-16-148410-0'),
('Venta', 'Disponible', '2025-03-02', 50000.00, 2, 2, 2, '978-1-4028-9462-6'),
('Intercambio', 'Disponible', '2025-03-03', 0.00,     3, 3, 3, '978-0-7432-7356-5'),  -- Carlos, Clásicos
('Venta',       'Disponible', '2025-03-04', 65000.00, 1, 5, 4, '978-0-452-28423-4'),  -- Juan, Ofertas
('Venta',       'Disponible', '2025-03-05', 80000.00, 2, 3, 5, '978-84-376-0494-7');  -- María, Clásicos

-- =========================
-- RESEÑAS
-- =========================
-- María escribe reseña sobre "Cien Años de Soledad"
INSERT INTO Reseña (calificacion, contenido, fecha_reseña, ID_usuario_autor, ID_usuario_comenta, ID_libro, ISBN)
VALUES
(5, 'Obra maestra, lenguaje poético y profundo.', '2025-03-05', 2, NULL, 1, '978-3-16-148410-0'),
(4, 'Muy vigente y perturbador.',               '2025-03-06', 1, NULL, 2, '978-1-4028-9462-6'),  -- Juan reseña 1984
(5, 'Historia de amor inolvidable.',            '2025-03-07', 4,  5,   3, '978-0-7432-7356-5'),  -- Luisa reseña Amor..., comenta Andrés
(4, 'Clásico imprescindible; prosa brillante.', '2025-03-08', 5,  NULL, 5, '978-84-376-0494-7'),  -- Andrés reseña Quijote
(3, 'Interesante pero esperaba más acción.',    '2025-03-09', 3,  2,   4, '978-0-452-28423-4');

-- Carlos comenta la reseña de María
UPDATE Reseña
SET ID_usuario_comenta = 3
WHERE ID_reseña = 1;

-- =========================
-- INTERCAMBIO
-- =========================
INSERT INTO Intercambio (fecha, estado, ID_usuario, ID_libro, ISBN)
VALUES
('2025-03-10', 'Pendiente', 1, 1, '978-3-16-148410-0'),
('2025-03-12', 'Completado',  3, 2, '978-1-4028-9462-6'),  
('2025-03-13', 'Pendiente',   4, 3, '978-0-7432-7356-5'),
('2025-03-14', 'En proceso',  5, 4, '978-0-452-28423-4');


-- =========================
-- VENTA
-- =========================
INSERT INTO Venta (fecha_venta, estado, precio, ID_usuario, ID_libro, ISBN)
VALUES
('2025-03-12', 'En proceso', 45000.00, 2, 2, '978-1-4028-9462-6'),
('2025-03-13', 'Completada', 48000.00, 1, 3, '978-0-7432-7356-5'),  -- cambia libro
('2025-03-14', 'Cancelada', 50000.00, 3, 4, '978-0-452-28423-4'),   -- cambia libro
('2025-03-15', 'En proceso', 65000.00, 2, 5, '978-84-376-0494-7'),  -- cambia libro
('2025-03-16', 'Completada', 79000.00, 4, 1, '978-3-16-148410-0');  -- cambia libro


-- =========================
-- RELACIONES N:M
-- =========================
-- Usuario participa en Club con fecha_union
INSERT INTO usuario_club (ID_usuario, ID_club, fecha_union)
VALUES
(1, 1, '2025-02-01'),
(2, 2, '2025-02-05'),
(3, 1, '2025-02-07'),
(4, 3, '2025-02-10'),
(5, 2, '2025-02-12');

-- Club de lectura ha leído libros
INSERT INTO club_lectura_libro (ID_club, ID_libro, ISBN)
VALUES
(1, 1, '978-3-16-148410-0'),
(2, 2, '978-1-4028-9462-6'),
(3, 3, '978-0-7432-7356-5'),
(4, 4, '978-0-452-28423-4'),
(5, 5, '978-84-376-0494-7');
