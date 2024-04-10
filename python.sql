-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-04-2024 a las 01:11:44
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `python`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bebida`
--

CREATE TABLE `bebida` (
  `id_bebida` int(6) NOT NULL,
  `nombre_b` varchar(20) DEFAULT NULL,
  `precio` float(10,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bebida`
--

INSERT INTO `bebida` (`id_bebida`, `nombre_b`, `precio`) VALUES
(1, 'Cocacola', 10.000),
(2, 'Ginger', 20.000),
(3, 'Jugo', 30.000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comida`
--

CREATE TABLE `comida` (
  `id_comida` int(6) NOT NULL,
  `nombre_c` varchar(20) DEFAULT NULL,
  `precio` float(10,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comida`
--

INSERT INTO `comida` (`id_comida`, `nombre_c`, `precio`) VALUES
(1, 'Hamborguesa', 10.000),
(2, 'Sandwich', 20.000),
(3, 'Lasagna', 30.000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedido` int(6) NOT NULL,
  `total` float(10,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos_bebida`
--

CREATE TABLE `pedidos_bebida` (
  `id_p` int(6) DEFAULT NULL,
  `id_b` int(6) DEFAULT NULL,
  `cantidad` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos_comida`
--

CREATE TABLE `pedidos_comida` (
  `id_p` int(6) DEFAULT NULL,
  `id_c` int(6) DEFAULT NULL,
  `cantidad` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bebida`
--
ALTER TABLE `bebida`
  ADD PRIMARY KEY (`id_bebida`);

--
-- Indices de la tabla `comida`
--
ALTER TABLE `comida`
  ADD PRIMARY KEY (`id_comida`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id_pedido`);

--
-- Indices de la tabla `pedidos_bebida`
--
ALTER TABLE `pedidos_bebida`
  ADD KEY `fk_id3` (`id_p`),
  ADD KEY `fk_id4` (`id_b`);

--
-- Indices de la tabla `pedidos_comida`
--
ALTER TABLE `pedidos_comida`
  ADD KEY `fk_id1` (`id_p`),
  ADD KEY `fk_id2` (`id_c`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bebida`
--
ALTER TABLE `bebida`
  MODIFY `id_bebida` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `comida`
--
ALTER TABLE `comida`
  MODIFY `id_comida` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pedidos_bebida`
--
ALTER TABLE `pedidos_bebida`
  ADD CONSTRAINT `fk_id3` FOREIGN KEY (`id_p`) REFERENCES `pedidos` (`id_pedido`),
  ADD CONSTRAINT `fk_id4` FOREIGN KEY (`id_b`) REFERENCES `bebida` (`id_bebida`);

--
-- Filtros para la tabla `pedidos_comida`
--
ALTER TABLE `pedidos_comida`
  ADD CONSTRAINT `fk_id1` FOREIGN KEY (`id_p`) REFERENCES `pedidos` (`id_pedido`),
  ADD CONSTRAINT `fk_id2` FOREIGN KEY (`id_c`) REFERENCES `comida` (`id_comida`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
