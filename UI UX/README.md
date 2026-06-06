# AquaSafe Pipe 💧

![AquaSafe Banner](https://img.shields.io/badge/Status-Active-brightgreen)
![React](https://img.shields.io/badge/React-18.x-blue?logo=react)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-4.x-38B2AC?logo=tailwind-css)
![Arduino](https://img.shields.io/badge/Hardware-Arduino_Mega_2560-00979D?logo=arduino)

**Smart IoT-Based Water Quality & Corrosion Monitoring System**

AquaSafe Pipe adalah platform sistem tertanam (*embedded system*) terintegrasi IoT yang dirancang untuk memantau kualitas air dan mendeteksi potensi korosi pada infrastruktur pipa secara *real-time*. Sistem ini menggabungkan pembacaan sensor analog via mikrokontroler dengan antarmuka *dashboard web* yang modern, interaktif, dan responsif.

## ✨ Fitur Utama

- 📊 **Real-time Telemetry Dashboard:** Visualisasi data sensor aktual (pH, TDS, Turbidity) dengan antarmuka gaya *glassmorphism* dan *dark mode*.
- 🎛️ **Dynamic Risk Gauge Chart:** Kalkulasi dan representasi visual *Risk Score* (Skor Risiko) dalam bentuk grafik *gauge meter* (Aman, Hati-hati, Bahaya).
- 🧠 **Embedded Risk Algorithm:** Pengolahan algoritma klasifikasi risiko yang dioptimalkan pada level arsitektur *bare-metal* AVR.
- 🔌 **Hardware Simulation Mode:** Mode simulasi bawaan (*mockup data*) untuk pengujian UI/UX tanpa perlu menyambungkan perangkat keras.

## 🛠️ Tech Stack

**Frontend Web:**
- [React.js](https://reactjs.org/) (v18)
- [Vite](https://vitejs.dev/) (Build tool)
- [Tailwind CSS](https://tailwindcss.com/) (v4.x)
- [Lucide React](https://lucide.dev/) (Iconography)

**Hardware & IoT (Target Architecture):**
- ATmega2560 (Arduino Mega Base Platform)
- Bare-metal AVR C Programming
- Serial Communication (UART0 @ 9600 bps)

## 🧮 Algoritma Kalkulasi Risiko
Sistem memberikan skor akumulatif batas aman (*Risk Score* 0-100) berdasarkan parameter berikut:
1. **pH Level:** Jika `< 6.50` (Asam) $\rightarrow$ +40 Poin
2. **TDS (Total Dissolved Solids):** Jika `> 500 ppm` $\rightarrow$ +35 Poin
3. **Turbidity (Kekeruhan):** Jika `> 50%` $\rightarrow$ +25 Poin

*Indikator Status:*
- **AMAN:** Skor 0 - 40
- **WASPADA:** Skor 41 - 70
- **BAHAYA:** Skor > 70

## 🚀 Cara Menjalankan Proyek (Frontend)

Pastikan [Node.js](https://nodejs.org/) sudah terinstal di komputermu.

1. **Clone repositori ini**
   ```bash
   git clone [https://github.com/username-kamu/aquasafe-pipe.git](https://github.com/username-kamu/aquasafe-pipe.git)
   cd aquasafe-pipe
