-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 27, 2020 at 09:26 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pidgeon`
--

-- --------------------------------------------------------

--
-- Table structure for table `duiven`
--

CREATE TABLE `duiven` (
  `naam` text NOT NULL,
  `id` int(11) NOT NULL,
  `geboortedatum` date NOT NULL,
  `leeftijd` int(11) NOT NULL,
  `initialstate` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `duiven`
--

INSERT INTO `duiven` (`naam`, `id`, `geboortedatum`, `leeftijd`, `initialstate`) VALUES
('Anne', 4, '2017-01-15', 3, 'https://go.init.st/sez2t6a'),
('Brent', 2, '2007-01-15', 13, 'http://test.com');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `created_at`) VALUES
(1, 'test', '$2y$10$0ytn1/BnWNlRZAhQk7ByxOlytp075xayn4QO4f1SEkefIRdUDVGOi', '2020-01-22 10:52:05'),
(2, 'test2', '$2y$10$mMXLInSoAtGkdTCtzcroR.qzIl8dtxfYC9gzMRelOp7URWw0eeQeu', '2020-01-22 11:37:04'),
(3, 'testje2', '$2y$10$ZT5xqs19gKbqkn5INw.HAeMBt/0GlMq5FL80XDtiu2zIUTZxpliEO', '2020-01-27 08:51:27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
