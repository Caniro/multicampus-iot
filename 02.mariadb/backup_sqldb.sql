-- MariaDB dump 10.19  Distrib 10.6.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: sqldb
-- ------------------------------------------------------
-- Server version	10.6.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `buytbl`
--

DROP TABLE IF EXISTS `buytbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buytbl` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `userID` char(8) NOT NULL,
  `prodName` char(6) NOT NULL,
  `groupName` char(4) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `amount` smallint(6) NOT NULL,
  PRIMARY KEY (`num`),
  KEY `userID` (`userID`),
  CONSTRAINT `buytbl_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `usertbl` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buytbl`
--

LOCK TABLES `buytbl` WRITE;
/*!40000 ALTER TABLE `buytbl` DISABLE KEYS */;
INSERT INTO `buytbl` VALUES (1,'KBS','운동화',NULL,30,2),(2,'KBS','노트북','전자',1000,1),(3,'JYP','모니터','전자',200,1),(4,'BBK','모니터','전자',200,5),(5,'KBS','청바지','의류',50,3),(6,'BBK','메모리','전자',80,10),(7,'SSK','책','서적',15,5),(8,'EJW','책','서적',15,2),(9,'EJW','청바지','의류',50,1),(10,'BBK','운동화',NULL,30,2),(11,'EJW','책','서적',15,1),(12,'BBK','운동화',NULL,30,2);
/*!40000 ALTER TABLE `buytbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buytbl2`
--

DROP TABLE IF EXISTS `buytbl2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buytbl2` (
  `num` int(11) NOT NULL DEFAULT 0,
  `userID` char(8) NOT NULL,
  `prodName` char(6) NOT NULL,
  `groupName` char(4) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `amount` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buytbl2`
--

LOCK TABLES `buytbl2` WRITE;
/*!40000 ALTER TABLE `buytbl2` DISABLE KEYS */;
INSERT INTO `buytbl2` VALUES (1,'KBS','운동화',NULL,30,2),(2,'KBS','노트북','전자',1000,1),(3,'JYP','모니터','전자',200,1),(4,'BBK','모니터','전자',200,5),(5,'KBS','청바지','의류',50,3),(6,'BBK','메모리','전자',80,10),(7,'SSK','책','서적',15,5),(8,'EJW','책','서적',15,2),(9,'EJW','청바지','의류',50,1),(10,'BBK','운동화',NULL,30,2),(11,'EJW','책','서적',15,1),(12,'BBK','운동화',NULL,30,2);
/*!40000 ALTER TABLE `buytbl2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membertbl`
--

DROP TABLE IF EXISTS `membertbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `membertbl` (
  `userID` char(8) NOT NULL,
  `name` varchar(10) NOT NULL,
  `birthYear` int(11) NOT NULL,
  `addr` char(2) NOT NULL,
  `mobile1` char(3) DEFAULT NULL,
  `mobile2` char(8) DEFAULT NULL,
  `height` smallint(6) DEFAULT NULL,
  `mDate` date DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membertbl`
--

LOCK TABLES `membertbl` WRITE;
/*!40000 ALTER TABLE `membertbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `membertbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testtbl1`
--

DROP TABLE IF EXISTS `testtbl1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testtbl1` (
  `id` int(11) DEFAULT NULL,
  `userName` char(3) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testtbl1`
--

LOCK TABLES `testtbl1` WRITE;
/*!40000 ALTER TABLE `testtbl1` DISABLE KEYS */;
INSERT INTO `testtbl1` VALUES (1,'홍길동',25),(2,'설현',NULL),(3,'초아',26);
/*!40000 ALTER TABLE `testtbl1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usertbl`
--

DROP TABLE IF EXISTS `usertbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usertbl` (
  `userID` char(8) NOT NULL,
  `name` varchar(10) NOT NULL,
  `birthYear` int(11) NOT NULL,
  `addr` char(2) NOT NULL,
  `mobile1` char(3) DEFAULT NULL,
  `mobile2` char(8) DEFAULT NULL,
  `height` smallint(6) DEFAULT NULL,
  `mDate` date DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertbl`
--

LOCK TABLES `usertbl` WRITE;
/*!40000 ALTER TABLE `usertbl` DISABLE KEYS */;
INSERT INTO `usertbl` VALUES ('BBK','바비킴',1973,'서울','010','00000000',176,'2013-05-05'),('EJW','은지원',1972,'경북','011','88888888',174,'2014-03-03'),('JKW','조관우',1965,'경기','018','99999999',172,'2010-10-10'),('JYP','조용필',1950,'경기','011','44444444',166,'2009-04-04'),('KBS','김범수',1979,'경남','011','22222222',173,'2012-04-04'),('KKH','김경호',1971,'전남','019','33333333',177,'2007-07-07'),('LJB','임재범',1963,'서울','016','66666666',182,'2009-09-09'),('LSG','이승기',1987,'서울','011','11111111',182,'2008-08-08'),('SSK','성시경',1979,'서울',NULL,NULL,186,'2013-12-12'),('YJS','윤종신',1969,'경남',NULL,NULL,170,'2005-05-05');
/*!40000 ALTER TABLE `usertbl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-19 13:34:31
