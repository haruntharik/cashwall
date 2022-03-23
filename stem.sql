CREATE DATABASE  IF NOT EXISTS `wallet` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `wallet`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: localhost    Database: wallet
-- ------------------------------------------------------
-- Server version	5.5.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t1` (
  `a` int(11) DEFAULT NULL,
  KEY `a` (`a`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transde`
--

DROP TABLE IF EXISTS `transde`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transde` (
  `walletid` varchar(20) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `transactionmode` varchar(20) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `balance` varchar(22) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transde`
--

LOCK TABLES `transde` WRITE;
/*!40000 ALTER TABLE `transde` DISABLE KEYS */;
INSERT INTO `transde` VALUES ('12345678','2022-03-18','09:42:48','credit','100','159800'),('None','2022-03-18','15:15:41','credit','100','100400'),('None','2022-03-18','15:17:43','debit','100','100300'),(NULL,'2022-03-18','15:19:23','credit','100','100400'),(NULL,'2022-03-18','15:27:13','credit','100','100500'),('12345678','2022-03-18','15:29:59','credit','100','160000'),('20222','2022-03-18','15:32:40','credit','100','300'),('12345678','2022-03-18','15:41:26','credit','100','160100'),('12345678','2022-03-18','15:47:40','credit','100','160200'),('12345678','2022-03-18','15:50:33','credit','100','160300'),('12345678','2022-03-18','15:58:15','credit','100','160400'),('12345678','2022-03-18','15:58:21','debit','100','160300'),('12345678','2022-03-18','16:00:53','credit','100','160400'),('12345678','2022-03-18','16:01:01','credit','100','160500'),('12345678','2022-03-18','16:01:07','credit','100','160600'),('12345678','2022-03-18','16:01:14','credit','100','160700'),('12345678','2022-03-18','16:01:20','credit','100','160800'),('12345678','2022-03-18','16:01:28','debit','100','160700'),('12345678','2022-03-18','16:01:36','credit','100','160800'),('12345678','2022-03-18','16:01:43','credit','100','160900'),('12345678','2022-03-18','16:02:12','debit','10000','150900'),('12345678','2022-03-18','16:02:19','credit','100000000','100150900'),('12345678','2022-03-18','16:08:47','credit','100','100151000'),('12345678','2022-03-18','16:08:58','debit','10000','100141000'),('12345678','2022-03-18','16:21:07','credit','100','100141100'),('12345678','2022-03-18','16:21:14','credit','100','100141200'),('12345678','2022-03-18','16:21:23','debit','100000000','141200'),('12345678','2022-03-18','16:31:45','credit','100','141300'),('12345678','2022-03-18','16:31:54','credit','100000','241300'),('12345678','2022-03-18','16:32:02','credit','100000','341300'),('12345678','2022-03-18','16:32:12','debit','100000','241300'),('12345678','2022-03-18','16:32:25','debit','1000','240300'),('12345678','2022-03-18','16:32:32','credit','1000','241300'),('12345678','2022-03-18','16:33:09','credit','1000','242300'),('12345678','2022-03-18','16:38:02','credit','100','242400'),('12345678','2022-03-18','16:39:22','credit','100','242500'),('12345678','2022-03-18','16:39:29','debit','100','242400'),('12345678','2022-03-18','16:41:05','credit','100','242500'),('12345678','2022-03-18','16:41:16','debit','100','242400'),('12345678','2022-03-18','16:43:20','credit','100','242500'),('12345678','2022-03-18','16:43:28','debit','100','242400'),('12345678','2022-03-18','16:45:20','credit','100','242500'),('12345678','2022-03-18','16:49:59','credit','100','242600'),('12345678','2022-03-18','16:50:07','debit','100','242500'),('12345678','2022-03-18','16:51:27','credit','100','242600'),('12345678','2022-03-18','16:51:42','credit','100000000','100242600'),('12345678','2022-03-18','16:52:04','credit','100','100242700'),('12345678','2022-03-18','16:52:13','debit','100000000','242700'),('12345678','2022-03-18','16:52:25','credit','100','242800'),('20222','2022-03-18','19:52:12','credit','100','400'),('20222','2022-03-18','19:52:35','debit','10','390'),('20222','2022-03-18','19:52:43','debit','10','380'),('20222','2022-03-18','19:59:22','credit','100000','100380'),('12345678','2022-03-18','20:04:36','credit','100','242900'),('45678','2022-03-18','20:15:02','credit','100','9100'),('45678','2022-03-18','20:15:29','debit','100','9000'),('9090','2022-03-18','20:21:55','credit','100','8100'),('12345678','2022-03-19','15:33:07','credit','100','243000'),('12345678','2022-03-19','15:33:23','credit','100','243100'),('12345678','2022-03-19','15:56:10','credit','100','243200'),('12345678','2022-03-19','15:56:19','debit','100','243100'),('12345678','2022-03-19','15:56:40','credit','100','243200'),('12345678','2022-03-19','16:01:59','credit','100','243300'),('12345678','2022-03-19','16:02:07','debit','100000','143300'),('12345678','2022-03-19','16:06:00','credit','100','143400'),('12345678','2022-03-19','16:12:46','credit','100','143500'),('45678','2022-03-19','16:13:24','credit','100','9100'),('12345678','2022-03-19','16:18:20','credit','100','143600'),('12345678','2022-03-19','16:21:53','credit','100','143700'),('12345678','2022-03-19','16:22:01','debit','100','143600'),('12345678','2022-03-19','16:30:57','credit','100','143700'),('12345678','2022-03-19','16:31:08','debit','1000','142700'),('12345678','2022-03-19','19:59:51','credit','100.0','142800.0'),('12345678','2022-03-19','20:03:23','credit','100.5','142900.5'),('12345678','2022-03-19','20:09:09','credit','100.0','143001.0'),('12345678','2022-03-19','20:09:17','debit','100.0','142901.0'),('20222','2022-03-19','20:11:03','credit','2.5','100382.5'),('20222','2022-03-19','20:11:27','credit','2.765','100385.765'),('20222','2022-03-19','20:13:49','credit','2.765','100388.765'),('12345678','2022-03-19','20:28:43','credit','100.0','143001.0');
/*!40000 ALTER TABLE `transde` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` varchar(20) DEFAULT NULL,
  `walletid` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `balance` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('tharik','10000',NULL,NULL),('harun',NULL,NULL,NULL),('harun',NULL,NULL,NULL),(NULL,NULL,'irfan123',NULL),(NULL,'20222',NULL,NULL),(NULL,NULL,NULL,80000),('asar',NULL,NULL,100500),(NULL,NULL,'asar1223',NULL),(NULL,'2222',NULL,NULL),(NULL,NULL,NULL,9000),('nehru',NULL,'irfan123',NULL),(NULL,'2222',NULL,NULL),(NULL,NULL,NULL,80000),('ahamed','2345','2321j',9000),('bilal','12345678','123456',143001),('harun','20000','arun123',9000),('harun','20000','arun123',9000),('harun','20222','asar1223',80000),('asar','2222','asar123',100500),('lucie','20222','lucie123',100389),('arifa','45678','arifa123',9100),('nisa','9090','nisa123',8100);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-23 13:04:01
