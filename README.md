<div align="center">

# 💧 AquaSafe Pipe

### Smart IoT-Based Water Quality & Corrosion Monitoring System

<img src="asset/banner.png" alt="AquaSafe Pipe Banner" width="100%">

![Arduino](https://img.shields.io/badge/Arduino_Mega-00979D?style=for-the-badge\&logo=arduino\&logoColor=white)
![IoT](https://img.shields.io/badge/IoT-Monitoring-blue?style=for-the-badge)
![Water Quality](https://img.shields.io/badge/Water-Quality-success?style=for-the-badge)
![Corrosion Detection](https://img.shields.io/badge/Corrosion-Detection-orange?style=for-the-badge)

### 🚰 Monitoring Kualitas Air dan Deteksi Korosi Pipa Berbasis IoT

</div>

---

## 📖 Overview

AquaSafe Pipe merupakan sistem monitoring kualitas air berbasis Internet of Things (IoT) yang dirancang untuk menjaga keamanan distribusi air bersih melalui pemantauan parameter kualitas air secara real-time.

Sistem menggunakan **Arduino Mega 2560 (ATmega2560)** sebagai pusat kendali yang terintegrasi dengan beberapa sensor kualitas air, yaitu:

* 🌡️ Sensor pH
* 💧 Sensor TDS (Total Dissolved Solids)
* 🌫️ Sensor Turbidity (Kekeruhan)

Data dari sensor dikirim secara real-time ke dashboard IoT sehingga memungkinkan pemantauan jarak jauh dan deteksi dini terhadap kondisi yang berpotensi menyebabkan korosi pipa serta kontaminasi logam berat seperti Timbal (Pb).

---

## 🎯 Project Objective

Membangun sistem pemantauan kualitas air pipa berbasis mikrokontroler Arduino Mega yang mampu mendeteksi potensi korosi dan pelarutan timbal (Pb) secara real-time guna mencegah kontaminasi air bersih serta memungkinkan tindakan preventif secara cepat melalui dashboard monitoring jarak jauh.

---

## ✨ Features

✅ Monitoring pH secara Real-Time

✅ Monitoring TDS secara Real-Time

✅ Monitoring Kekeruhan Air (Turbidity)

✅ Deteksi Potensi Korosi Pipa

✅ Monitoring Dashboard IoT

✅ Sistem Peringatan Dini (Alert System)

✅ Pemantauan Jarak Jauh

✅ Data Logging dan Analisis

---

## 🏗️ System Architecture

```text
                 WATER FLOW
                      │
                      ▼
         ┌───────────────────────┐
         │      pH Sensor        │
         ├───────────────────────┤
         │      TDS Sensor       │
         ├───────────────────────┤
         │   Turbidity Sensor    │
         └───────────────────────┘
                      │
                      ▼
         ┌───────────────────────┐
         │    Arduino Mega       │
         │      ATmega2560       │
         └───────────────────────┘
                      │
                      ▼
         ┌───────────────────────┐
         │      IoT Dashboard    │
         └───────────────────────┘
                      │
                      ▼
              Alert & Monitoring
```

---

## 🔧 Komponen
| No | Komponen | Qty |
| :---: | :--- | :---: |
| 1 | Arduino Mega 2560 Compatible | 1 |
| 2 | Sensor pH + Probe pH | 1 |
| 3 | Sensor TDS Gravity | 1 |
| 4 | Sensor Turbidity | 1 |
| 5 | LED Merah 5 mm | 1 |
| 6 | LED Kuning 5 mm | 1 |
| 7 | LED Hijau 5 mm | 1 |
| 8 | Resistor 220 Ω | 3 |
| 9 | Buzzer Aktif 5V | 1 |
| 10 | Kabel Jumper Set | 1 |
| 11 | Adaptor/USB Power Supply | 1 |

---

## Visualisasi Sistem 
---

## 🔬 Sensors Used

| Sensor           | Function                       |
| ---------------- | ------------------------------ |
| pH Sensor        | Mengukur tingkat keasaman air  |
| TDS Sensor       | Mengukur jumlah zat terlarut   |
| Turbidity Sensor | Mengukur tingkat kekeruhan air |

---

## 🐟 Fishbone Analysis

<div align="center">

<img src="asset/image.png" width="900">

</div>

---

## 🧠 Mind Map

<div align="center">

<img src="asset/figjam.jpeg" width="900">

</div>

---

## 📊 Block Diagram

<div align="center">

<img src="asset/image.jpg" width="900">

</div>

---

## ⚙️ Desain Simulasi
<img src="https://github.com/RofifFairuzZaki/Aquasafe-Pipe-ATmega2560-Kelompok/blob/64849967c441cfd8933c97948101f717775407f3/asset/Screenshot%202026-06-06%20172606.png"> 

## 📸 Project Documentation

<div align="center">

<img src="asset/documentation.jpeg" width="800">

</div>

---

## 🎥 Project Presentation

<div align="center">

### 📊 Open Presentation

<a href="https://www.canva.com/design/DAHLUscpbcU/ThfkQryM6eWiujemS9Ijmg/edit">
<img src="https://img.shields.io/badge/Open-Canva_Presentation-00C4CC?style=for-the-badge&logo=canva&logoColor=white">
</a>

</div>

---

## 👨‍💻 Team Members

| No | Name                 | NRP        | Role              |
| -- | -------------------- | ---------- | ----------------- |
| 1  | Rofif Fairuz Zaki    | 2124600040 | Project Manager   |
| 2  | Didit Bayu Kurnianto | 2124600047 | Programmer        |
| 3  | Ridho Yanuar         | 2124600046 | Hardware Engineer |
| 4  | Moch. Akhdan Nabilly | 2124600038 | 3D Designer       |
| 5  | Anggara Bayu Saputra | 2124600057 | UI/UX Designer    |
| 6  | Aissyah Fitriani     | 2124600059 | Nonteknis         |

---

## 🛠️ Technologies Used

* Arduino Mega 2560
* ATmega2560
* IoT Dashboard
* Embedded C Programming
* Water Quality Sensors
* Corrosion Monitoring System

---

## 🎓 Academic Information

### Supported By

**Dosen Pengampu**

Akhmad Hendriawan, ST., MT.

NIP. 197501272002121003

**Mata Kuliah**

Mikrokontroler

**Program Studi**

D4 Teknik Elektronika

**Institusi**

Politeknik Elektronika Negeri Surabaya (PENS)

---

<div align="center">

### 💧 AquaSafe Pipe

Smart Monitoring • Safe Water • Better Future

© 2026 Kelompok 4 – D4 Teknik Elektronika PENS

</div>
