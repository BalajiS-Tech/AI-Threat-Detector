-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 17, 2022 at 02:35 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `nox_eye`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `location` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `name`, `email`, `mobile`, `location`) VALUES
('admin', 'admin', 'Sivam', 'ram@gmail.com', 9081171123, 'Adayar');

-- --------------------------------------------------------

--
-- Table structure for table `detect_info`
--

CREATE TABLE `detect_info` (
  `id` int(11) NOT NULL,
  `detect_img` varchar(20) NOT NULL,
  `date_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detect_info`
--


-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`) VALUES
(1, 'abnormal');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `location` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `name`, `mobile`, `email`, `location`, `uname`, `pass`) VALUES
(1, 'Surya', 8812706225, 'surya@gmail.com', '15,SS Nagar', 'user1', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `vt_face`
--

CREATE TABLE `vt_face` (
  `id` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `vface` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vt_face`
--

INSERT INTO `vt_face` (`id`, `vid`, `vface`) VALUES
(1, 1, '1_2.jpg'),
(2, 1, '1_3.jpg'),
(3, 1, '1_4.jpg'),
(4, 1, '1_5.jpg'),
(5, 1, '1_6.jpg'),
(6, 1, '1_7.jpg'),
(7, 1, '1_8.jpg'),
(8, 1, '1_9.jpg'),
(9, 1, '1_10.jpg'),
(10, 1, '1_11.jpg'),
(11, 1, '1_12.jpg'),
(12, 1, '1_13.jpg'),
(13, 1, '1_14.jpg'),
(14, 1, '1_15.jpg'),
(15, 1, '1_16.jpg'),
(16, 1, '1_17.jpg'),
(17, 1, '1_18.jpg'),
(18, 1, '1_19.jpg'),
(19, 1, '1_20.jpg'),
(20, 1, '1_21.jpg'),
(21, 1, '1_22.jpg'),
(22, 1, '1_23.jpg'),
(23, 1, '1_24.jpg'),
(24, 1, '1_25.jpg'),
(25, 1, '1_26.jpg'),
(26, 1, '1_27.jpg'),
(27, 1, '1_28.jpg'),
(28, 1, '1_29.jpg'),
(29, 1, '1_30.jpg'),
(30, 1, '1_31.jpg'),
(31, 1, '1_32.jpg'),
(32, 1, '1_33.jpg'),
(33, 1, '1_34.jpg'),
(34, 1, '1_35.jpg'),
(35, 1, '1_36.jpg'),
(36, 1, '1_37.jpg'),
(37, 1, '1_38.jpg'),
(38, 1, '1_39.jpg'),
(39, 1, '1_40.jpg');
