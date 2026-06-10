<?php
// Konfigurasi Database XAMPP
$host = "127.0.0.1";
$user = "root";         // Username default XAMPP
$pass = "";             // Password default XAMPP (biasanya kosong)
$db   = "aqua_safe_db"; // Nama database di phpMyAdmin
$port = "3307";         // Sesuai dengan screenshot kamu sebelumnya

// Membuat koneksi menggunakan MySQLi
$conn = new mysqli($host, $user, $pass, $db, $port);

// Mengecek apakah koneksi berhasil
if ($conn->connect_error) {
    // Jika gagal, tampilkan pesan error yang jelas di browser
    die("Koneksi ke database gagal: " . $conn->connect_error);
}
?>