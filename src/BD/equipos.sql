SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `equipos` DEFAULT CHARACTER SET utf8mb4 ;
USE `equipos` ;

CREATE TABLE IF NOT EXISTS `equipos`.`equipos` (
  `Id` INT(3) NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(100) NOT NULL,
  `Deporte` VARCHAR(100) NOT NULL,
  `Localidad` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `equipos`.`jugadores` (
  `DNI` INT(8) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Apellido` VARCHAR(100) NOT NULL,
  `Localidad` VARCHAR(200) NOT NULL,
  `Edad` INT(3) NOT NULL,
  PRIMARY KEY (`DNI`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `equipos`.`equipo_has_jugadores` (
  `jugadores_DNI` INT(8) NOT NULL,
  `equipos_Id` INT(3) NOT NULL,
  PRIMARY KEY (`jugadores_DNI`, `equipos_Id`),
  INDEX `fk_jugadores_has_equipos_equipos1_idx` (`equipos_Id`),
  INDEX `fk_jugadores_has_equipos_jugadores_idx` (`jugadores_DNI`),
  CONSTRAINT `fk_jugadores_has_equipos_jugadores`
    FOREIGN KEY (`jugadores_DNI`)
    REFERENCES `equipos`.`jugadores` (`DNI`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_jugadores_has_equipos_equipos1`
    FOREIGN KEY (`equipos_Id`)
    REFERENCES `equipos`.`equipos` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
