CREATE TABLE IF NOT EXISTS `agrocadenas` (
  `id` int(4) NOT NULL,
  `suministro` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `produccion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `distribucion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `encargado` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `agrocadenas`
--

INSERT INTO `agrocadenas` (`id`, `suministro`, `produccion`, `distribucion`, `encargado`) VALUES
('0521', 'Semillas traídas de Canadá', 'Se plantan a la sombra', 'La cosecha se lleva a Canadá', 'Julián Martínez'),
('3342', 'Leche de vaca', 'Se procesa para hacer queso', 'Se vende a Colanta', 'Pamela Armani'),
('9510', 'Semillas de girasol', 'Se plantan con buena luz solar', 'Se exportan los girasoles a Perú', 'Ingrid Perea');
COMMIT;