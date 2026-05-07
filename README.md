# 🔐 Cyber Security Monitoring Dashboard

A professional Cyber Security Monitoring Dashboard built using Python and Flask.

This project monitors system performance, scans ports, detects suspicious activities, and displays alerts through an interactive dashboard interface.

---

# 🚀 Features

✅ Admin Login System  
✅ System Monitoring (CPU, RAM, Disk)  
✅ Port Scanner  
✅ Security Alert Detection  
✅ Failed Login Detection  
✅ Live Threat Level Indicator  
✅ Dark Mode  
✅ Interactive Charts  
✅ Real-Time Clock  
✅ Responsive Dashboard UI  
✅ SQLite Database Integration  

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Flask | Web Framework |
| SQLite | Database |
| HTML/CSS | Frontend |
| Bootstrap | UI Design |
| JavaScript | Client-side Functions |
| Chart.js | Dashboard Charts |
| Psutil | System Monitoring |
| Socket | Port Scanning |

---

# 📂 Project Structure

```text
security-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── database.db
│
├── modules/
│   ├── monitor.py
│   ├── database.py
│   ├── port_scanner.py
│   └── login_detector.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── alerts.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── charts.js
│
└── logs/
    └── security.log
