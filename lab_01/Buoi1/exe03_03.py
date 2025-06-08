def tao_tuple_tu_list(lst):
  """
  Chuyển đổi một danh sách thành một tuple.

  Args:
    lst: Danh sách cần chuyển đổi.

  Returns:
    Một tuple chứa các phần tử của danh sách.
  """
  return tuple(lst)

# Nhập danh sách số từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Sử dụng hàm và in kết quả
my_tuple = tao_tuple_tu_list(numbers)
print("List:", numbers)
print("Tuple từ List:", my_tuple)