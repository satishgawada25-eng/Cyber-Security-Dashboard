import socket


def scan_ports(target):
    open_ports = []

    common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445]

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports