-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 10, 2020 at 10:07 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edumate`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

DROP TABLE IF EXISTS `student_details`;
CREATE TABLE IF NOT EXISTS `student_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `gender` text NOT NULL,
  `university` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `fullname`, `email`, `password`, `gender`, `university`) VALUES
(1, 'John Doe', 'john@gmail.com', '1234', 'male', 'Mumbai University'),
(2, ' r ', ' r.v@gmail.com ', ' rohan ', ' male ', ' Mumbai University '),
(3, ' rohan ', ' rohan.v@gmail.com ', ' rohan ', ' male ', ' Mumbai University '),
(4, ' rohan ', ' rohan@gmail.com ', ' rohan@gmail.com ', ' male ', ' Mumbai University '),
(5, ' xx ', ' xx@d.com ', ' xx ', ' male ', ' Mumbai University ');

-- --------------------------------------------------------

--
-- Table structure for table `student_records`
--

DROP TABLE IF EXISTS `student_records`;
CREATE TABLE IF NOT EXISTS `student_records` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` text NOT NULL,
  `marks_scored` int(3) NOT NULL,
  `out_off` int(3) NOT NULL,
  `credit_point` int(1) NOT NULL,
  `semester` int(1) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_records`
--

INSERT INTO `student_records` (`id`, `subject_name`, `marks_scored`, `out_off`, `credit_point`, `semester`, `student_id`) VALUES
(8, 'IP', 95, 100, 5, 5, 1),
(9, 'IMP', 92, 100, 5, 5, 1),
(10, 'CNS', 88, 100, 5, 5, 1),
(11, 'ADMT', 85, 100, 5, 5, 1),
(12, 'MES', 81, 100, 5, 5, 1),
(13, 'BCE', 48, 50, 2, 5, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
