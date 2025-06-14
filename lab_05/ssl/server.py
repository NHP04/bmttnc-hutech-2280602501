import socket
import ssl
import threading

# Địa chỉ máy chủ
server_address = ('localhost', 12345)
clients = []

# Hàm xử lý kết nối với client
def handle_client(client_socket):
    print(f"Client đã kết nối: {client_socket.getpeername()}")
    try:
        while True:
            # Nhận dữ liệu từ client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Nhận: {data.decode('utf-8')}")
            
            # Gửi dữ liệu đến tất cả các client khác
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
                        client.close()
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server đang chờ kết nối...")

# Thiết lập kết nối SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='./certificates/server-cert.crt', keyfile='./certificates/server-key.key')

# Lắng nghe kết nối của client
while True:
    client_socket, client_address = server_socket.accept()
    client_socket = context.wrap_socket(client_socket, server_side=True)
    clients.append(client_socket)
    print(f"Kết nối với client: {client_address}")
    
    # Tạo luồng để xử lý client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
