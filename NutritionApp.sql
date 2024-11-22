-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: nutrition_app
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `baby_profiles`
--

DROP TABLE IF EXISTS `baby_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baby_profiles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age_months` int NOT NULL,
  `weight` float NOT NULL,
  `sleep_hours` float DEFAULT NULL,
  `advice` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baby_profiles`
--

LOCK TABLES `baby_profiles` WRITE;
/*!40000 ALTER TABLE `baby_profiles` DISABLE KEYS */;
INSERT INTO `baby_profiles` VALUES (1,'Tresor',8,5,12,'Weight Alert: Tresor\'s weight (5.0kg) is below the recommended range (6.9kg - 8.8kg). Add more protein and high-calorie meals, such as mashed sweet potatoes, avocados, and banana porridge.\nSleep Alert: Tresor is sleeping 12.0 hours, below the recommended 14 hours. Create a consistent bedtime routine, limit distractions, and ensure the baby has a comfortable sleeping environment.\nEnsure the baby is hydrated throughout the day.\nIntroduce a variety of fruits and vegetables gradually.\nAvoid processed foods or foods with added sugar or salt.\nEngage in play and tummy time to promote development.'),(2,'Eddy',12,11,15,'Weight Alert: Eddy\'s weight (11.0kg) is above the recommended range (7.8kg - 9.5kg). \nConsult a pediatrician for a detailed assessment.\nSleep: Eddy is getting enough sleep (15.0 hours).\nEnsure the baby is hydrated throughout the day.\nIntroduce a variety of fruits and vegetables gradually.\nAvoid processed foods or foods with added sugar or salt.\nEngage in play and tummy time to promote development.'),(3,'Emry',4,2,13,'Weight Alert: Emry\'s weight (2.0kg) is below the recommended range (5.6kg - 7.3kg). \nAdd more protein and high-calorie meals, such as mashed sweet potatoes, avocados, and banana porridge.\nSleep Alert: Emry is sleeping 13.0 hours, below the recommended 14 hours. \nCreate a consistent bedtime routine, limit distractions, and ensure the baby has a comfortable sleeping environment.\n\n=== Meal Plan Advice ===\n\nEnsure the baby is hydrated throughout the day.\nIntroduce a variety of fruits and vegetables gradually.\nAvoid processed foods or foods with added sugar or salt.\nEngage in play and tummy time to promote development.'),(4,'Jean',15,11,14,'We don\'t have weight data for this age group.\nSleep: Jean is getting enough sleep (14.0 hours).\n\n=== Meal Plan Advice ===\n\nEnsure the baby is hydrated throughout the day.\nIntroduce a variety of fruits and vegetables gradually.\nAvoid processed foods or foods with added sugar or salt.\nEngage in play and tummy time to promote development.'),(5,'Jean',10,7,16,'Weight Alert: Jean\'s weight (7.0kg) is below the recommended range (7.4kg - 9.2kg). \nAdd more protein and high-calorie meals, such as mashed sweet potatoes, avocados, and banana porridge.\nSleep: Jean is getting enough sleep (16.0 hours).\n\n=== Meal Plan Advice for Jean ===\n\nEnsure the baby is hydrated throughout the day.\nIntroduce a variety of fruits and vegetables gradually.\nAvoid processed foods or foods with added sugar or salt.\nEngage in play and tummy time to promote development.');
/*!40000 ALTER TABLE `baby_profiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-22 14:35:05
