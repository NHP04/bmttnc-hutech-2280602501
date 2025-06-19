from scapy.all import * 
import socket  

# Danh sách các cổng phổ biến cần quét
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

# Hàm quét các cổng phổ biến của một tên miền
def scan_common_ports(domain):
    open_ports = []  # Danh sách lưu các cổng mở
    try:
        ip = socket.gethostbyname(domain)
        print(f"Scanning IP: {ip}")  # In ra địa chỉ IP của tên miền
    except socket.gaierror:
        # Nếu không thể phân giải tên miền, thông báo lỗi và trả về danh sách cổng mở rỗng
        print("Không thể phân giải tên miền.")
        return open_ports

    # Lặp qua các cổng phổ biến để kiểm tra xem cổng nào đang mở
    for port in COMMON_PORTS:
        try:
            # Tạo một socket TCP/IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Thiết lập thời gian chờ (timeout) cho mỗi kết nối là 1 giây
            result = s.connect_ex((ip, port))  # Kết nối đến địa chỉ IP và cổng
            if result == 0:  # Nếu kết nối thành công (result = 0), cổng mở
                open_ports.append(port)  # Thêm cổng vào danh sách mở
            s.close()  
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports 

def main():
    # Nhập tên miền từ người dùng
    domain = input("Enter the target domain: ")
    
    # Gọi hàm scan_common_ports để quét các cổng phổ biến
    open_ports = scan_common_ports(domain)

    # Kiểm tra nếu có cổng mở
    if open_ports:
        print("Open common ports:")
        # In ra các cổng mở
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open common ports found.")  # Thông báo nếu không có cổng nào mở

# Kiểm tra nếu chương trình được chạy trực tiếp
if __name__ == '__main__':
    main()
