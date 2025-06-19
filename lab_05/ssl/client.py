import socket   
import ssl     
import threading 

# Thông tin server mà client sẽ kết nối tới
server_address = ('localhost', 12345)  # Địa chỉ và cổng của server

# Hàm nhận dữ liệu từ server
def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)  # Nhận tối đa 1024 byte dữ liệu từ server
            if not data:  # Nếu không có dữ liệu (server đóng kết nối)
                break
            print("Nhận:", data.decode('utf-8'))  # In dữ liệu nhận được (giải mã từ UTF-8)
    except:
        pass  # Bỏ qua mọi lỗi nếu có
    finally:
        ssl_socket.close()  # Đảm bảo đóng kết nối SSL khi hoàn thành
        print("Kết nối đã đóng.")  # Thông báo kết nối đã bị đóng

# Tạo một socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khởi tạo SSL context để bảo mật kết nối
context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # Sử dụng giao thức TLS cho kết nối bảo mật
context.verify_mode = ssl.CERT_NONE  # Không yêu cầu xác minh chứng chỉ (thường trong môi trường thử nghiệm)
context.check_hostname = False  # Không kiểm tra hostname của server (có thể thay đổi theo yêu cầu)

# Bọc socket TCP trong SSL để tạo kết nối bảo mật
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Kết nối đến server qua địa chỉ và cổng đã chỉ định
ssl_socket.connect(server_address)

# Tạo một luồng con để nhận dữ liệu từ server trong khi client vẫn có thể gửi dữ liệu
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))  # Gọi hàm nhận dữ liệu trong luồng riêng
receive_thread.start()  # Bắt đầu luồng nhận dữ liệu

try:
    while True:
        message = input("Nhập tin nhắn: ")  # Yêu cầu người dùng nhập tin nhắn
        ssl_socket.send(message.encode('utf-8'))  # Gửi tin nhắn qua kết nối SSL (mã hóa UTF-8)
except KeyboardInterrupt:  # Nếu người dùng nhấn Ctrl+C để dừng
    pass  # Bỏ qua lỗi khi dừng
finally:
    ssl_socket.close()  # Đảm bảo đóng kết nối khi hoàn thành
