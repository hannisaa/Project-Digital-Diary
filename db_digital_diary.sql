-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 03 Jun 2026 pada 07.03
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_digital_diary`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `achievement`
--

CREATE TABLE `achievement` (
  `id_achieve` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `date_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `achievement`
--

INSERT INTO `achievement` (`id_achieve`, `id_user`, `title`, `description`, `date_time`) VALUES
(3, 2, 'Pertama Kali Nulis Diary Rutin', 'Konsisten menulis selama 7 hari berturut-turut', '2025-09-20 16:25:51'),
(8, 1, 'first place in the running competition', 'first place in the running competition at my school', '2025-09-28 10:35:38');

-- --------------------------------------------------------

--
-- Struktur dari tabel `diary_entry`
--

CREATE TABLE `diary_entry` (
  `id_entry` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `todays_activities` text NOT NULL,
  `date_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `diary_entry`
--

INSERT INTO `diary_entry` (`id_entry`, `id_user`, `todays_activities`, `date_time`) VALUES
(3, 2, 'Latihan supporteran Olim UI bareng teman-teman', '2025-09-20 15:40:48'),
(15, 12, 'hari ini seruu', '2025-09-24 14:21:50'),
(19, 13, 'Today was so exciting. I just came back from my friend\'s birthday party, yippie!!', '2025-09-25 15:03:42'),
(20, 13, 'huft... I\'m so tired after taking the exam', '2025-09-25 15:32:09'),
(22, 1, 'haii, today was fun', '2025-09-28 10:15:01'),
(25, 1, 'iyaa seru', '2025-10-01 09:44:17');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mood`
--

CREATE TABLE `mood` (
  `id_mood` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `mood` varchar(50) NOT NULL,
  `date_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `mood`
--

INSERT INTO `mood` (`id_mood`, `id_user`, `mood`, `date_time`) VALUES
(1, 1, 'happy', '2025-09-20 16:22:18'),
(2, 1, 'Capek', '2025-09-20 16:22:18'),
(3, 2, 'Happy', '2025-09-20 16:22:18'),
(4, 13, 'Happy', '2025-09-24 10:49:29'),
(5, 13, 'fun!', '2025-09-24 11:51:03');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` enum('M','F') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id_user`, `username`, `fullname`, `password`, `date_of_birth`, `gender`) VALUES
(1, 'Luna', 'Raya Luna', '12345', '2003-09-12', 'F'),
(2, 'Lintang', 'Lintang Cahaya', 'abcd123', '2002-05-20', 'M'),
(12, 'yusuf', 'yusuf yoga', '565656', '2008-02-01', 'F'),
(13, 'Rizky', 'Rizky Nur Aziz', '101010', '2000-10-01', 'M'),
(17, 'juna', 'juna j', '12345', '2009-07-01', 'M'),
(19, 'HILWA', 'hilwa Annisa', '121212', '2006-09-01', 'F'),
(20, '', '', '', '0000-00-00', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `achievement`
--
ALTER TABLE `achievement`
  ADD PRIMARY KEY (`id_achieve`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `diary_entry`
--
ALTER TABLE `diary_entry`
  ADD PRIMARY KEY (`id_entry`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `mood`
--
ALTER TABLE `mood`
  ADD PRIMARY KEY (`id_mood`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `achievement`
--
ALTER TABLE `achievement`
  MODIFY `id_achieve` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `diary_entry`
--
ALTER TABLE `diary_entry`
  MODIFY `id_entry` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT untuk tabel `mood`
--
ALTER TABLE `mood`
  MODIFY `id_mood` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `achievement`
--
ALTER TABLE `achievement`
  ADD CONSTRAINT `achievement_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `diary_entry`
--
ALTER TABLE `diary_entry`
  ADD CONSTRAINT `diary_entry_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

--
-- Ketidakleluasaan untuk tabel `mood`
--
ALTER TABLE `mood`
  ADD CONSTRAINT `mood_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
