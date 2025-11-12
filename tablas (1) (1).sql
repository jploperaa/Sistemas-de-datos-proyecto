
CREATE TABLE `Usuario` (
  `ID_usuario` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre`     VARCHAR(100) NOT NULL,
  `correo`     VARCHAR(120) UNIQUE,
  `telefono`   VARCHAR(30),
  `password`   VARCHAR(255) NOT NULL,
  `ciudad`     VARCHAR(100)
) ;

CREATE TABLE `Catalogo` (
  `ID_catalogo`   INT PRIMARY KEY AUTO_INCREMENT,
  `nombre`        VARCHAR(120) NOT NULL,
  `descripcion`   TEXT,
  `fecha_creacion` DATE NOT NULL
) ;

CREATE TABLE `Club_lectura` (
  `ID_club`        INT PRIMARY KEY AUTO_INCREMENT,
  `nombre`         VARCHAR(120) NOT NULL,
  `descripcion`    TEXT,
  `estado`         VARCHAR(30),
  `fecha_creacion` DATE NOT NULL
) ;

-- PK compuesta: (ID_libro, ISBN)
CREATE TABLE `Libro` (
  `ID_libro`        INT NOT NULL,
  `ISBN`            VARCHAR(20) NOT NULL,
  `titulo`          VARCHAR(200) NOT NULL,
  `autor`           VARCHAR(150) NOT NULL,
  `año_publicacion` INT,
  `genero`          VARCHAR(80),
  `modalidad`       VARCHAR(40),
  `resumen`         TEXT,
  `propietario`     VARCHAR(120),
  -- Usuario ----recibe---- Libro (1:N)
  `ID_usuario_recibe` INT,
  CONSTRAINT `pk_libro` PRIMARY KEY (`ID_libro`, `ISBN`),
  CONSTRAINT `fk_libro_usuario_recibe`
    FOREIGN KEY (`ID_usuario_recibe`) REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ;

CREATE TABLE `Publicacion` (
  `ID_publicacion`    INT PRIMARY KEY AUTO_INCREMENT,
  `modalidad`         VARCHAR(40),
  `estado`            VARCHAR(30),
  `fecha_publicacion` DATE,
  `precio`            DECIMAL(10,2) CHECK (`precio` >= 0),

  -- Usuario ----realiza---- Publicacion (1:N)
  `ID_usuario`        INT NOT NULL,

  -- Publicacion ----pertenece---- Catalogo (N:1)
  `ID_catalogo`       INT NOT NULL,

  -- NUEVO: Publicacion ----(N:1)---- Libro
  `ID_libro`          INT NOT NULL,
  `ISBN`              VARCHAR(20) NOT NULL,

  CONSTRAINT `fk_publicacion_usuario`
    FOREIGN KEY (`ID_usuario`)  REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_publicacion_catalogo`
    FOREIGN KEY (`ID_catalogo`) REFERENCES `Catalogo`(`ID_catalogo`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_publicacion_libro`
    FOREIGN KEY (`ID_libro`, `ISBN`) REFERENCES `Libro`(`ID_libro`, `ISBN`)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ;

CREATE TABLE `Reseña` (
  `ID_reseña`     INT PRIMARY KEY AUTO_INCREMENT,
  `calificacion`  TINYINT CHECK (`calificacion` BETWEEN 1 AND 5),
  `contenido`     TEXT,
  `fecha_reseña`  DATE,

  -- Usuario ----escribe---- Reseña (1:N)
  `ID_usuario_autor`    INT NOT NULL,

  -- Usuario ----comenta---- Reseña (1:N)
  `ID_usuario_comenta`  INT,

  -- Reseña ----corresponde---- Libro (N:1)
  `ID_libro` INT NOT NULL,
  `ISBN`     VARCHAR(20) NOT NULL,

  CONSTRAINT `fk_resena_usuario_autor`
    FOREIGN KEY (`ID_usuario_autor`)   REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_resena_usuario_comenta`
    FOREIGN KEY (`ID_usuario_comenta`) REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_resena_libro`
    FOREIGN KEY (`ID_libro`, `ISBN`)    REFERENCES `Libro`(`ID_libro`, `ISBN`)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ;

CREATE TABLE `Intercambio` (
  `ID_intercambio` INT PRIMARY KEY AUTO_INCREMENT,
  `fecha`          DATE,
  `estado`         VARCHAR(30),

  -- Usuario ----realiza---- Intercambio (1:N)
  `ID_usuario`     INT NOT NULL,

  -- Intercambio ----tiene---- Libro (1:1)
  `ID_libro` INT NOT NULL,
  `ISBN`     VARCHAR(20) NOT NULL,

  CONSTRAINT `fk_intercambio_usuario`
    FOREIGN KEY (`ID_usuario`) REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_intercambio_libro`
    FOREIGN KEY (`ID_libro`, `ISBN`) REFERENCES `Libro`(`ID_libro`, `ISBN`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  -- Garantiza 1:1 (un libro en un solo intercambio activo)
  CONSTRAINT `uq_intercambio_libro` UNIQUE (`ID_libro`, `ISBN`)
) ;

CREATE TABLE `Venta` (
  `ID_venta`     INT PRIMARY KEY AUTO_INCREMENT,
  `fecha_venta`  DATE,
  `estado`       VARCHAR(30),
  `precio`       DECIMAL(10,2) CHECK (`precio` >= 0),

  -- Usuario ----realiza---- Venta (1:N)
  `ID_usuario`   INT NOT NULL,

  -- Venta ----tiene---- Libro (1:1)  y  Libro ----vende---- Venta (1:1)
  `ID_libro` INT NOT NULL,
  `ISBN`     VARCHAR(20) NOT NULL,

  CONSTRAINT `fk_venta_usuario`
    FOREIGN KEY (`ID_usuario`) REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  CONSTRAINT `fk_venta_libro`
    FOREIGN KEY (`ID_libro`, `ISBN`) REFERENCES `Libro`(`ID_libro`, `ISBN`)
    ON UPDATE CASCADE ON DELETE RESTRICT,

  -- Garantiza 1:1: cada libro a lo sumo en UNA venta
  CONSTRAINT `uq_venta_libro` UNIQUE (`ID_libro`, `ISBN`)
) ;

-- =========================
--  RELACIONES N:M
-- =========================

-- Usuario ----participa---- Club_lectura (N:M) con atributo fecha_union
CREATE TABLE `usuario_club` (
  `ID_usuario` INT NOT NULL,
  `ID_club`    INT NOT NULL,
  `fecha_union` DATE NOT NULL,
  CONSTRAINT `pk_usuario_club` PRIMARY KEY (`ID_usuario`, `ID_club`),
  CONSTRAINT `fk_uc_usuario`
    FOREIGN KEY (`ID_usuario`) REFERENCES `Usuario`(`ID_usuario`)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT `fk_uc_club`
    FOREIGN KEY (`ID_club`)    REFERENCES `Club_lectura`(`ID_club`)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ;

-- Club_lectura ----leído---- Libro (N:M)
CREATE TABLE `club_lectura_libro` (
  `ID_club`  INT NOT NULL,
  `ID_libro` INT NOT NULL,
  `ISBN`     VARCHAR(20) NOT NULL,
  CONSTRAINT `pk_club_libro` PRIMARY KEY (`ID_club`, `ID_libro`, `ISBN`),
  CONSTRAINT `fk_club_libro_club`
    FOREIGN KEY (`ID_club`)           REFERENCES `Club_lectura`(`ID_club`)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT `fk_club_libro_libro`
    FOREIGN KEY (`ID_libro`, `ISBN`)  REFERENCES `Libro`(`ID_libro`, `ISBN`)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ;
