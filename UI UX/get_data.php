    <?php
require 'koneksi.php';

// Mengambil 1 data paling baru (diurutkan berdasarkan id menurun)
$sql = "SELECT ph, tds, turbidity, risk_score, status, timestamp FROM tb_log_sensor ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

$data = array();

if ($result->num_rows > 0) {
    $data = $result->fetch_assoc();
    // Konversi tipe data agar sesuai saat dibaca oleh JSON
    $data['ph'] = (float)$data['ph'];
    $data['tds'] = (int)$data['tds'];
    $data['turbidity'] = (int)$data['turbidity'];
    $data['risk_score'] = (int)$data['risk_score'];
} else {
    // Nilai default jika database masih kosong
    $data = [
        "ph" => 0, "tds" => 0, "turbidity" => 0, "risk_score" => 0, "status" => "TIDAK ADA DATA"
    ];
}

header('Content-Type: application/json');
echo json_encode($data);

$conn->close();
?>