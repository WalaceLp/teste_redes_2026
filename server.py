import socket

HOST = ""
PORTA = 2026

print("iniciando um servidor de chat na porta {PORTA}...")
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORTA))

while True:
    msg, cliente = udp.recvfrom(1024)
    print(f"{cliente} -> {msg.decode()}")

