<?php
require 'koneksi.php';

// Memastikan data dikirim melalui metode GET
if(isset($_GET['ph']) && isset($_GET['tds']) && isset($_GET['turbidity']) && isset($_GET['risk_score']) && isset($_GET['status'])) {
    
    $ph = $_GET['ph'];
    $tds = $_GET['tds'];
    $turbidity = $_GET['turbidity'];
    $risk_score = $_GET['risk_score'];
    $status = $_GET['status'];

    // Query untuk memasukkan data
    $sql = "INSERT INTO tb_log_sensor (ph, tds, turbidity, risk_score, status) 
            VALUES ('$ph', '$tds', '$turbidity', '$risk_score', '$status')";

    if ($conn->query($sql) === TRUE) {
        echo "Data berhasil disimpan";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    echo "Akses ditolak: Data sensor tidak lengkap.";
}

$conn->close();
?>