import streamlit as st
import plotly.graph_objects as go
import serial
import time

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(page_title="AquaSafe Pipe", page_icon="💧", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #0b132b; color: #f1f5f9; }
    .css-1d391kg { background-color: #0f172a; } 
    .stButton>button { width: 100%; border-radius: 8px; background-color: #0ea5e9; color: white; border: none; }
    .stButton>button:hover { background-color: #0284c7; }
    .metric-card { background-color: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; margin-bottom: 15px;}
    .badge { padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .badge-aman { background-color: rgba(74, 222, 128, 0.1); color: #4ade80; border: 1px solid rgba(74, 222, 128, 0.2); }
    .badge-waspada { background-color: rgba(251, 191, 36, 0.1); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.2); }
    .badge-bahaya { background-color: rgba(248, 113, 113, 0.1); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.2); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INISIALISASI KONEKSI SERIAL WOKWI
# ==========================================
@st.cache_resource
def init_serial():
    try:
        # Menghubungkan ke rfc2217 virtual port Wokwi (Port 4000)
        ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=9600, timeout=0.5)
        return ser
    except Exception as e:
        return None

arduino = init_serial()

# Inisialisasi State Awal
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if 'sensor' not in st.session_state:
    st.session_state['sensor'] = {'ph': 7.0, 'tds': 0, 'turbidity': 0, 'riskScore': 0, 'status': 'AMAN'}

# ==========================================
# FUNGSI PEMBACAAN DATA REAL-TIME
# ==========================================
def fetch_realtime_data():
    if arduino and arduino.in_waiting > 0:
        try:
            raw_line = arduino.readline().decode('utf-8').strip()
            data_split = raw_line.split(',')
            
            if len(data_split) == 4:
                v_ph = float(data_split[0])
                v_tds = float(data_split[1])
                v_turb = float(data_split[2])
                v_status = data_split[3]

                # Kalkulasi Bobot Risiko
                score = 0
                if v_ph < 6.5 or v_ph > 8.5: score += 40
                if v_tds > 1200: score += 35
                elif v_tds > 500: score += 15
                if v_turb > 1000: score += 25
                elif v_turb > 300: score += 10

                st.session_state['sensor'] = {
                    'ph': v_ph, 'tds': v_tds, 'turbidity': v_turb, 'riskScore': score, 'status': v_status
                }
        except Exception:
            pass

def login(): st.session_state['auth'] = True
def logout(): st.session_state['auth'] = False

# ==========================================
# INTERMUKA USER (UI)
# ==========================================
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write(""); st.write("")
        st.markdown("<h1 style='text-align: center; color: #38bdf8;'>💧 AquaSafe Pipe</h1>", unsafe_allow_html=True)
        with st.form("login_form"):
            st.text_input("Email / ID", placeholder="admin@aquasafe.net")
            st.text_input("Password", type="password", placeholder="••••••••")
            if st.form_submit_button("Access System"):
                login(); st.rerun()
else:
    with st.sidebar:
        st.markdown("## 💧 AquaSafe Pipe")
        st.caption("v1.1.0 (Live Stream)")
        st.write("---")
        menu = st.radio("Navigasi", ["Home", "Monitoring", "About"])
        st.write("---")
        if arduino:
            st.markdown("---")
        if st.button("Sign Out"):
            logout(); st.rerun()

    if menu == "Home":
        st.markdown("<h1 style='text-align: center;'>AquaSafe Pipe</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color:#cbd5e1;'>Smart IoT-Based Water Quality & Corrosion Monitoring System</h4>", unsafe_allow_html=True)
        st.info("💡 Hubungkan Wokwi Simulator terlebih dahulu, lalu buka menu **Monitoring** untuk melihat data real-time.")

    elif menu == "Monitoring":
        st.title("AquaSafe Live Telemetry Dashboard")
        st.caption("Data diperbarui otomatis setiap detik langsung dari core mikrokontroler Wokwi.")
        st.write("---")

        # ENGINE AUTO-REFRESH SINKRONISASI DATA
        fetch_realtime_data()

        data = st.session_state['sensor']
        col_sensor, col_gauge = st.columns([1, 1.5])
        
        with col_sensor:
            # Card pH
            ph_status = "Abnormal" if (data['ph'] < 6.5 or data['ph'] > 8.5) else "Normal"
            ph_class = "badge-bahaya" if ph_status == "Abnormal" else "badge-aman"
            st.markdown(f'<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">PH LEVEL</p><h2 style="margin:0;">{data["ph"]:.1f} <span class="badge {ph_class}" style="float:right;">{ph_status}</span></h2></div>', unsafe_allow_html=True)
            
            # Card TDS
            tds_status = "Bahaya" if data['tds'] > 1200 else ("Waspada" if data['tds'] > 500 else "Aman")
            tds_class = "badge-bahaya" if data['tds'] > 1200 else ("badge-waspada" if data['tds'] > 500 else "badge-aman")
            st.markdown(f'<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">TDS (DISSOLVED SOLIDS)</p><h2 style="margin:0;">{int(data["tds"])} <span style="font-size:14px; color:#64748b;">ppm</span> <span class="badge {tds_class}" style="float:right;">{tds_status}</span></h2></div>', unsafe_allow_html=True)
            
            # Card Turbidity
            turb_status = "Keruh" if data['turbidity'] > 1000 else ("Waspada" if data['turbidity'] > 300 else "Jernih")
            turb_class = "badge-bahaya" if data['turbidity'] > 1000 else ("badge-waspada" if data['turbidity'] > 300 else "badge-aman")
            st.markdown(f'<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">TURBIDITY (KEKERUHAN)</p><h2 style="margin:0;">{int(data["turbidity"])} <span style="font-size:14px; color:#64748b;">NTU</span> <span class="badge {turb_class}" style="float:right;">{turb_status}</span></h2></div>', unsafe_allow_html=True)

        with col_gauge:
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=data['riskScore'], domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': f"SYSTEM RISK STATUS: {data['status']}", 'font': {'color': '#e2e8f0'}},
                number={'suffix': " /100", 'font': {'color': '#e2e8f0'}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "#0ea5e9", 'thickness': 0.2}, 
                    'bgcolor': "rgba(0,0,0,0)", 'borderwidth': 0,
                    'steps': [
                        {'range': [0, 14], 'color': '#4ade80'},
                        {'range': [15, 70], 'color': '#fbbf24'},
                        {'range': [71, 100], 'color': '#f87171'}
                    ],
                }
            ))
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#e2e8f0"}, height=350, margin=dict(l=20, r=20, t=50, b=20))
            st.plotly_chart(fig, use_container_width=True)

        # Trigger perulangan refresh halaman otomatis (setiap 1 detik)
        time.sleep(1)
        st.rerun()

    elif menu == "About":
        st.title("Tentang Proyek AquaSafe Pipe")
        st.write("Sistem monitoring IoT real-time terintegrasi penuh menggunakan port serial virtual RFC2217.")
        