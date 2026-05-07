from flask import Flask, render_template, request, redirect, session
from modules.monitor import get_system_usage
from modules.port_scanner import scan_ports
from modules.database import init_db, add_alert, get_alerts

app = Flask(__name__)
app.secret_key = 'cybersecurityproject'

init_db()

USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['user'] = username
            return redirect('/dashboard')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    system_data = get_system_usage()
    alerts = get_alerts()

    return render_template(
        'dashboard.html',
        system_data=system_data,
        alerts=alerts
    )

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    ports = scan_ports(target)

    if len(ports) > 0:
        add_alert(f"Open ports found on {target}: {ports}")

    return {
        "target": target,
        "open_ports": ports
    }

@app.route('/alerts')
def alerts():
    data = get_alerts()
    return render_template('alerts.html', alerts=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)