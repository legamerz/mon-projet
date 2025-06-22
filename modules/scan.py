import socket

def run():
    print("📡 Scan réseau simple")
    target = input("Adresse IP : ").strip()
    ports = [21, 22, 80, 443]
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f"✅ Port {port} ouvert")
        s.close()
