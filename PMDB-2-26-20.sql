-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: powermonitor
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `device1_readings`
--

DROP TABLE IF EXISTS `device1_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device1_readings` (
  `DEVICE1_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICE1_VOLTAGE` double NOT NULL,
  `DEVICE1_CURRENT` double NOT NULL,
  `DEVICE1_TIMESTAMP` datetime NOT NULL,
  PRIMARY KEY (`DEVICE1_ID`),
  UNIQUE KEY `DEVICE1_ID_UNIQUE` (`DEVICE1_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device1_readings`
--

LOCK TABLES `device1_readings` WRITE;
/*!40000 ALTER TABLE `device1_readings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device1_readings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device2_readings`
--

DROP TABLE IF EXISTS `device2_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device2_readings` (
  `DEVICE2_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICE2_VOLTAGE` double NOT NULL,
  `DEVICE2_CURRENT` double NOT NULL,
  `DEVICE2_TIMESTAMP` datetime NOT NULL,
  PRIMARY KEY (`DEVICE2_ID`),
  UNIQUE KEY `DEVICE2_ID_UNIQUE` (`DEVICE2_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device2_readings`
--

LOCK TABLES `device2_readings` WRITE;
/*!40000 ALTER TABLE `device2_readings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device2_readings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device3_readings`
--

DROP TABLE IF EXISTS `device3_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device3_readings` (
  `DEVICE3_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICE3_VOLTAGE` double NOT NULL,
  `DEVICE3_CURRENT` double NOT NULL,
  `DEVICE3_TIMESTAMP` datetime NOT NULL,
  PRIMARY KEY (`DEVICE3_ID`),
  UNIQUE KEY `DEVICE3_ID_UNIQUE` (`DEVICE3_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device3_readings`
--

LOCK TABLES `device3_readings` WRITE;
/*!40000 ALTER TABLE `device3_readings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device3_readings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device4_readings`
--

DROP TABLE IF EXISTS `device4_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device4_readings` (
  `DEVICE4_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICE4_VOLTAGE` double NOT NULL,
  `DEVICE4_CURRENT` double NOT NULL,
  `DEVICE4_TIMESTAMP` datetime NOT NULL,
  PRIMARY KEY (`DEVICE4_ID`),
  UNIQUE KEY `DEVICE4_ID_UNIQUE` (`DEVICE4_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device4_readings`
--

LOCK TABLES `device4_readings` WRITE;
/*!40000 ALTER TABLE `device4_readings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device4_readings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device5_readings`
--

DROP TABLE IF EXISTS `device5_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device5_readings` (
  `DEVICE5_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEVICE5_VOLTAGE` double NOT NULL,
  `DEVICE5_CURRENT` double NOT NULL,
  `DEVICE5_TIMESTAMP` datetime NOT NULL,
  PRIMARY KEY (`DEVICE5_ID`),
  UNIQUE KEY `DEVICE5_ID_UNIQUE` (`DEVICE5_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device5_readings`
--

LOCK TABLES `device5_readings` WRITE;
/*!40000 ALTER TABLE `device5_readings` DISABLE KEYS */;
/*!40000 ALTER TABLE `device5_readings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `NOTIFICATIONS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOTIFICATIONS_MESSAGE` varchar(45) DEFAULT NULL COMMENT 'Contents of notification',
  `NOTIFICATIONS_TIMESTAMP` datetime DEFAULT NULL COMMENT 'Time notification was received',
  `NOTIFICATIONS_UNREAD` tinyint(4) DEFAULT NULL COMMENT 'Indicates whether notification is read or unread',
  PRIMARY KEY (`NOTIFICATIONS_ID`),
  UNIQUE KEY `NOTIFICATIONS_ID_UNIQUE` (`NOTIFICATIONS_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profiles` (
  `PROFILES_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Max should be 5. 5 device profiles.',
  `PROFILES_NAME` varchar(45) DEFAULT NULL COMMENT 'Name of device profile',
  `PROFILES_DESCRIPTION` varchar(45) DEFAULT NULL COMMENT 'Description of device',
  PRIMARY KEY (`PROFILES_ID`),
  UNIQUE KEY `PROFILES_ID_UNIQUE` (`PROFILES_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (1,'Test 1','Default Profile 1'),(2,'Test 2','Default Profile 2'),(3,'Test 3','Default Profile 3'),(4,'Test 4','Default Profile 4'),(5,'Test 5','Default Profile 5');
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `SETTINGS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SETTINGS_THEME` varchar(45) NOT NULL,
  `SETTINGS_DEVICE_PROFILE` varchar(45) NOT NULL,
  PRIMARY KEY (`SETTINGS_ID`),
  UNIQUE KEY `SETTINGS_ID_UNIQUE` (`SETTINGS_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES (1,'Dark','Test 2');
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-26 13:04:25
