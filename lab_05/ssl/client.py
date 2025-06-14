import socket
import ssl
import threading

# Địa chỉ server
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print(f"Nhận: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thiết lập SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.verify_mode = ssl.CERT_NONE  # Tắt việc kiểm tra chứng chỉ
context.check_hostname = False  # Tắt kiểm tra hostname


# Kết nối với server qua SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Tạo một luồng nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi tin nhắn tới server
while True:
    message = input("Nhập tin nhắn: ")
    ssl_socket.send(message.encode('utf-8'))
