import socket

def port_scan(target_ip, ports):
    print(f"[+] Starting Port Scan on {target_ip}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            s.close()
        except Exception as e:
            print(f"[ERROR] Could not scan port {port} - {e}")
