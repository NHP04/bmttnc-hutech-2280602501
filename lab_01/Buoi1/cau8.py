# hàm kiểm tra số nhị phân
def chia_het_cho_5(so_nhi_phan):
    # chuyểnn số nhị phân sang số thập phân
    so_thap_phan = int (so_nhi_phan, 2)
    #kiểm tra số thập phân 
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input(" nhập chuỗi số nhị phân ( phân tách bởi dấu phẩy):")