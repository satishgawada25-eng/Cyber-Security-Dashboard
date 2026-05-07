import re
from modules.database import add_alert

FAILED_THRESHOLD = 3

failed_attempts = {}


def detect_failed_login(log_line):
    """
    Detect failed login attempts from logs.
    """

    pattern = r'Failed login from (\d+\.\d+\.\d+\.\d+)'

    match = re.search(pattern, log_line)

    if match:
        ip = match.group(1)

        if ip not in failed_attempts:
            failed_attempts[ip] = 0

        failed_attempts[ip] += 1

        if failed_attempts[ip] >= FAILED_THRESHOLD:
            alert_message = (
                f"Suspicious activity detected from IP {ip}. "
                f"Multiple failed login attempts."
            )

            add_alert(alert_message)

            return {
                "status": "alert",
                "ip": ip,
                "attempts": failed_attempts[ip]
            }

    return {
        "status": "safe"
    }