-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Des 2023 pada 05.00
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `capstone`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `urine`
--

CREATE TABLE `urine` (
  `Number` int(11) NOT NULL,
  `Color` varchar(255) DEFAULT NULL,
  `Health` varchar(350) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `urine`
--

INSERT INTO `urine` (`Number`, `Color`, `Health`) VALUES
(1, 'Biru', 'Warna biru pada urine tidak umum dan mungkin merupakan hasil dari konsumsi pewarna makanan tertentu. Namun, jika warna biru terus menerus muncul, itu bisa menunjukkan masalah dengan ginjal atau saluran kemih. Disarankan untuk berkonsultasi dengan profesional kesehatan.'),
(2, 'Coklat', 'Warna coklat pada urine bisa disebabkan oleh dehidrasi, konsumsi makanan tertentu, atau masalah dengan hati. Tetapi, coklat juga dapat menjadi tanda adanya darah dalam urine, yang memerlukan perhatian medis segera.'),
(3, 'Hijau', 'Warna hijau pada urine biasanya disebabkan oleh konsumsi makanan atau suplemen tertentu. Namun, jika hijau terus muncul dan tidak dapat dijelaskan oleh faktor diet, itu bisa mengindikasikan masalah kesehatan seperti infeksi atau penyakit hati. Konsultasikan dengan dokter untuk evaluasi lebih lanjut.'),
(4, 'Hitam', 'Urine hitam dapat menjadi tanda adanya darah teroksidasi atau masalah hati. Beberapa jenis makanan dan obat-obatan juga dapat menyebabkan urine hitam. Jika urine hitam terus muncul, segera hubungi profesional kesehatan.'),
(5, 'Jingga', 'Warna jingga pada urine mungkin disebabkan oleh dehidrasi atau konsumsi vitamin B kompleks. Namun, jika jingga terus muncul tanpa alasan yang jelas, itu bisa menunjukkan masalah dengan hati atau saluran empedu. Periksakan ke dokter untuk evaluasi lebih lanjut.'),
(6, 'Kuning', 'Warna kuning pada urine biasanya normal dan disebabkan oleh pigmen urine yang disebut urobilin. Namun, warna kuning yang sangat gelap atau kuning kecoklatan bisa menunjukkan dehidrasi. Pastikan untuk cukup minum air.'),
(7, 'Merah', 'Urine merah dapat disebabkan oleh keberadaan darah. Ini bisa disebabkan oleh infeksi saluran kemih, batu ginjal, atau masalah lain pada ginjal atau kandung kemih. Segera cari bantuan medis jika urine berwarna merah.'),
(8, 'Putih', 'Urine yang putih atau bening (transparan) umumnya dianggap normal dan sehat. Ini menunjukkan bahwa Anda mungkin sedang minum cukup air, dan ginjal Anda berfungsi dengan baik untuk menyaring kelebihan air dalam tubuh. Peningkatan konsumsi air dapat menghasilkan urine yang lebih transparan.');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `urine`
--
ALTER TABLE `urine`
  ADD PRIMARY KEY (`Number`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `urine`
--
ALTER TABLE `urine`
  MODIFY `Number` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
