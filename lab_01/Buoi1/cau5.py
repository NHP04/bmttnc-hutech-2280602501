so_gio_lam = float(input("nhập số giờ làm mỗi tuần:"))
luong_gio = float (input("nhập thù lao trên mỗi giờ làm tiêu chuẩn :"))
gio_tieu_chuan = 44
gioi_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)

thuc_tinh = gio_tieu_chuan * luong_gio + gio_tieu_chuan * luong_gio * 1.5
print(f"số tiền thực lĩnh của nhân viên:{thuc_tinh}")