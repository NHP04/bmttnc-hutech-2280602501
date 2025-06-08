# tạo một danh sách rỗng để lưu kết quả 
j=[]
# duyệt qua tẩt cả các số trong đoạn 
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print (','. join(j))
