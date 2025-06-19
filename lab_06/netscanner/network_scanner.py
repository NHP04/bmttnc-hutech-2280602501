import requests  
from scapy.all import ARP, Ether, srp  

def local_network_scan(ip_range):
    # Tạo gói ARP để quét dải IP đã cho
    arp = ARP(pdst=ip_range)
    # Tạo gói Ether với địa chỉ MAC đích là broadcast (ff:ff:ff:ff:ff:ff) để gửi đến tất cả các thiết bị trong mạng
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Kết hợp gói ARP và gói Ether
    packet = ether / arp
    # Gửi gói ARP và nhận phản hồi từ các thiết bị trên mạng (với timeout là 3 giây)
    result = srp(packet, timeout=3, verbose=0)[0]
    # Danh sách để lưu các thiết bị tìm được
    devices = []
    # Duyệt qua các gói phản hồi và lấy thông tin IP, MAC và nhà sản xuất của mỗi thiết bị
    for sent, received in result:
        devices.append({
            'ip': received.psrc,  # Lấy IP từ gói phản hồi
            'mac': received.hwsrc,  # Lấy địa chỉ MAC từ gói phản hồi
            'vendor': get_vendor_by_mac(received.hwsrc)  # Lấy nhà sản xuất từ MAC address
        })
    return devices

# Hàm lấy thông tin nhà sản xuất từ địa chỉ MAC bằng API của macvendors.com
def get_vendor_by_mac(mac):
    try:
        # Gửi yêu cầu HTTP GET đến API macvendors để lấy thông tin nhà sản xuất của địa chỉ MAC
        response = requests.get(f"https://api.macvendors.com/{mac}")
        
        # Nếu yêu cầu thành công (mã trả về 200), trả về tên nhà sản xuất
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"  # Nếu không tìm thấy nhà sản xuất, trả về "Unknown"
    except Exception as e:
        # Nếu có lỗi trong quá trình gửi yêu cầu, in lỗi và trả về "Unknown"
        print("Error fetching vendor information:", e)
        return "Unknown"

def main():
    # Dải IP của mạng cục bộ cần quét (subnet 192.168.88.114/24)
    ip_range = "192.168.88.114/24"
    # Gọi hàm local_network_scan để tìm các thiết bị trên mạng
    devices = local_network_scan(ip_range)
    print("Devices on the local network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")

if __name__ == '__main__':
    main()
