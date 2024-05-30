-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: project_schema
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem` varchar(45) NOT NULL,
  `answer` varchar(45) NOT NULL,
  `is_correct` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'2+2','4',0,1),(2,'3+3','6',1,1),(3,'4+4','8',1,2),(4,'5+5','10',0,2),(5,'2 * 2','4',1,3),(6,'0 * 3','0',1,4),(13,'170-69','101',0,8),(14,'19-2','17',0,8),(15,'19*15','285',0,8),(16,'47+16','63',0,8),(17,'103-48','55',0,8),(18,'22*13','286',0,9),(19,'20*6','120',0,9),(20,'6+12','18',0,9),(21,'22*6','132',0,9),(22,'45-40','5',0,9),(23,'703/37','19',0,10),(24,'7*11','77',0,10),(25,'0+18','18',0,10),(26,'131-101','30',0,10),(27,'117-98','19',0,10),(28,'x + 6 = 30','24',0,11),(29,'sqrt(9)','3',0,11),(30,'36 - x = 16','20',0,11),(31,'8x = 24','3',0,11),(32,'1 + 10 * 10 + 4 * 3 - 1','112',0,11),(33,'26+1','27',1,12),(34,'42+43','85',1,12),(35,'1034/47','22',1,12),(36,'23*29','667',1,12),(37,'10*9','90',1,12),(38,'1x^2  -13x + 12 = 0','[\'12\', \'1\']',0,13),(39,'(x +19)(x +7) = 0','[\'-19\', \'-7\']',0,13),(40,'-1x^2 + 17x = 16','[\'1\', \'16\']',0,13),(41,'4x^2  -17x + 4 = 0','[\'4\', \'0.25\']',0,13),(42,'4x^2  -13x + 10 = 0','[\'2\', \'1.25\']',0,13),(43,'(x -13)(x -12) = 0','[\'13\', \'12\']',0,14),(44,'2x^2  -11x = -12','[\'4\', \'1.5\']',0,14),(45,'1x^2  -18x + 17 = 0','[\'17\', \'1\']',0,14),(46,'-3x^2 + 18x  -15 = 0','[\'1\', \'5\']',0,14),(47,'(x -8)(x +4) = 0','[\'8\', \'-4\']',0,14),(48,'109-59','50',0,15),(49,'6+39','45',0,15),(50,'10*28','280',0,15),(51,'36-11','25',0,15),(52,'77/24','3.21',0,15),(53,'29*8','232',1,16),(54,'12*9','108',1,16),(55,'28+6','34',1,16),(56,'63/6','10.5',1,16),(57,'600/12','50',1,16),(58,'-2x^2 + 20x = 18','[\'1\', \'9\']',0,17),(59,'(x -2)(x -19) = 0','[\'2\', \'19\']',1,17),(60,'-2x^2 + 12x  -10 = 0','[\'1\', \'5\']',0,17),(61,'2x^2  -20x + 18 = 0','[\'9\', \'1\']',0,17),(62,'4x^2  -15x = -11','[\'2.75\', \'1\']',0,17),(63,'9 / 3 + 1 - 1 / 5 + 2 * 6 - 5 - 5','5.8',0,18),(64,'sqrt(4)','2',0,18),(65,'5**4 ','625',0,18),(66,'8 ** 1 + 8 - 7 + 10','19',0,18),(67,'2 - 9 / 8 * 6','-4.75',0,18),(68,'2x^2  -13x + 18 = 0','[\'4.5\', \'2\']',0,19),(69,'(x -17)(x +15) = 0','[\'17\', \'-15\']',0,19),(70,'-4x^2 + 17x  -4 = 0','[\'0.25\', \'4\']',0,19),(71,'(x -8)(x +2) = 0','[\'8\', \'-2\']',0,19),(72,'2x^2  -9x = -4','[\'4\', \'0.5\']',0,19),(73,'42+40','82',0,20),(74,'23*6','138',0,20),(75,'5*28','140',0,20),(76,'150-148','2',0,20),(77,'26-10','16',0,20),(78,'53/21','2.52',0,21),(79,'2-2','0',0,21),(80,'25/6','4.17',0,21),(81,'20*14','280',0,21),(82,'52/84','0.62',0,21),(83,'2**1 ','2',0,22),(84,'22x + 2 = 8','0.27',0,22),(85,'5 + 9 * 3 + 2 / 7 / 2 - 8 - 7','17.14',0,22),(86,'10 + 8 * 6 + 8 / 10 / 7','58.11',0,22),(87,'10 / 4 + 10 + 1 - 5 / 5 / 7 + 4 / 2','15.36',0,22),(88,'(x +11)(x -5) = 0','[\'-11\', \'5\']',0,23),(89,'(x -10)(x +7) = 0','[\'10\', \'-7\']',0,23),(90,'(x +11)(x -10) = 0','[\'-11\', \'10\']',0,23),(91,'(x +14)(x +20) = 0','[\'-14\', \'-20\']',0,23),(92,'4x^2  -18x + 14 = 0','[\'3.5\', \'1\']',0,23),(93,'(x +11)(x -5) = 0','[\'-11\', \'5\']',0,24),(94,'(x -10)(x +7) = 0','[\'10\', \'-7\']',0,24),(95,'(x +11)(x -10) = 0','[\'-11\', \'10\']',0,24),(96,'(x +14)(x +20) = 0','[\'-14\', \'-20\']',0,24),(97,'4x^2  -18x + 14 = 0','[\'3.5\', \'1\']',0,24),(98,'(x +11)(x -5) = 0','[\'-11\', \'5\']',0,25),(99,'(x -10)(x +7) = 0','[\'10\', \'-7\']',0,25),(100,'(x +11)(x -10) = 0','[\'-11\', \'10\']',0,25),(101,'(x +14)(x +20) = 0','[\'-14\', \'-20\']',0,25),(102,'4x^2  -18x + 14 = 0','[\'3.5\', \'1\']',0,25),(103,'(x +11)(x -5) = 0','[\'-11\', \'5\']',0,26),(104,'(x -10)(x +7) = 0','[\'10\', \'-7\']',0,26),(105,'(x +11)(x -10) = 0','[\'-11\', \'10\']',0,26),(106,'(x +14)(x +20) = 0','[\'-14\', \'-20\']',0,26),(107,'4x^2  -18x + 14 = 0','[\'3.5\', \'1\']',0,26);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (1,'13.01.2024','1'),(2,'14.01.2024','2'),(3,'15.01.2024','3'),(4,'16.01.2024','3'),(8,'27.05.2024','1'),(9,'27.05.2024','1'),(10,'27.05.2024','6'),(11,'27.05.2024','6'),(12,'27.05.2024','6'),(13,'27.05.2024','6'),(14,'27.05.2024','6'),(15,'27.05.2024','7'),(16,'27.05.2024','7'),(17,'27.05.2024','7'),(18,'27.05.2024','7'),(19,'27.05.2024','7'),(20,'27.05.2024','2'),(21,'27.05.2024','2'),(22,'27.05.2024','2'),(23,'27.05.2024','2'),(24,'27.05.2024','2'),(25,'27.05.2024','2'),(26,'27.05.2024','2');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Kason','Francis','Menendez','1@d.e','1','1'),(2,'Giavanna','Warner','Wadsworth','heidar.bright@aol.com','HwyjEkbEhjUw','98'),(3,'Melvin','Olsen','Diamond','cole.downs@msn.com','UsnxhsyxzpJX','57'),(4,'Issac','Schultz','Isaacson','diarmuid.nielsen@hotmail.com','A3wtsKNNSpAZ','24'),(6,'Richard','Velazquez','Ziegler','parkash.gallegos@comcast.net','pfBNvPqVdAGS','46'),(7,'Felix','Dougherty','Ashworth','rahim.singleton@googlemail.com','HBEunCtjjQuW','33');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'project_schema'
--

--
-- Dumping routines for database 'project_schema'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-30 17:04:49
