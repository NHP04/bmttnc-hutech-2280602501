a = 5
b = 3 
c = a + b
print(c)


a = 8
b = 4
c = a-b
print(c)

a = 6
b = 7
c = a*b
print(c)

a = 20
b = 5
c = a / b
print(c)

a = 20
b = 3
c = a // b
print(c)

a = 20
b = 7
c = a % b
print(c)

a = 2
b = 3
c = a ** b
print(c)

x = 5
y = 3
c = (x>2) and (y<4)
print(c)

x = 5
y = 3
c = (x>2) or (y>4)
print(c)

x = 5
c = not(x==5)
print(c)

x = 5
c = (x==5)
print(c)

x = 5
c = (x!=3)
print(c)

x = 5
c = (x>3)
d = (x<3)
print(c,d)

x = 5
c = (x>=3)
d = (x<=3)
print(c,d)

name = input("Nhập tên của bạn: ")
print("xin chào,",name)

age = 25
print("Tuổi của bạn:",age)

print("Python","là","ngôn","ngữ","lập","trình", sep="-")
print("Xin chào", end=" ")
print("các bạn")


x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else: 
    print("x nhỏ hơn 5")   
    
    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
count = 0
while count < 5:
    print(count)
    count +=1
    

for i in range(1,101):
  if i % 5 == 0:
    print ("số chia hết cho 5 đầu tiên là: ",i)
    break

for i in range(1,11):
  if i % 2 != 0:
    continue
  print(i)
  
x = 5
if x>10:
    print("x lớn hơn 10")
else: 
    pass

# Sử dụng dấu ngoặc đơn 
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.' 
 # Sử dụng dấu ngoặc kép 
string_double_quotes = "Đây là một chuỗi sử dụng dấu ngoặc kép." 
 # Sử dụng dấu ngoặc ba 
string_triple_quotes='''Đây là một chuỗi 
sử dụng dầu ngoặc ba, 
có thể trải dài qua nhiều dòng.''' 


my_string = "Hello, World!" 
print(my_string[0]) # Két quả: 'H' 
print(my_string[7]) # Kết quả: 'W



my_string = "Hello, World!" 
print(my_string [7:]) # Lấy từ kỳ tự thứ 7 đến hết: Kết quả: "World!" 
print(my_string[:5]) # lấy từ đầu đến ký tự thứ 4: Kết quả: 'Hello' 
print(my_string [3:8])# Lấy từ ký tự thứ 3 đến ký tự thứ 7: Kết quả: lo, W' 
   

string1 = "Hello" 
string2 = "World" 
concatenated_string = string1 +" " +string2 # Kết quả: 'Hello World'         



my_string= "Hello, World!"
print(my_string.strip()) # Loại bỏ khoảng trắng: Kết quả: 'Hello, World!' 

my_string = "Hello, World!" 
print(my_string.split(",")) 
# Phân tách chuỗi: Kết quả: ['Hello', 'World!'] 

my_string = "Hello, World!" 
print(my_string.replace("Hello", "Hi")) 
# Thay thế chuỗi: Kết quả: Hi, World!'




def my_function(parameter1, parameter2): 
    # Khối mà của hàm 
    # Thực hiện các hoạt động dựa trên tham số được truyên vào 
    result = parameter1 + parameter2 
    return result 



result = my_function(10, 20) # Gọi hàm và lưu kết quả vào biên result 
print(result) # In kết quả của hàm 



#Định nghĩa hàm tình tổng 
def calculate_sum(a, b): 
   result = a+b 
   return result 
# Gọi hàm và lưu kết quả vào biên 
sum_result=calculate_sum(10, 20) 
# In kết quả 
print("Tổng hai số là:", sum_result) 


from array import array 
# Khai báo một mảng số nguyên 
int_array = array('i', [1, 2, 3, 4, 5]) 
# Khai báo một mảng số thực 
float_array = array('f', [3.14, 2.5, 6.7])


print(int_array[0]) # Truy cập phần tử đầu tiên của máng số nguyên 
print(float_array[2]) # Truy cập phần từ thứ ba của máng số thực 

int_array[2] = 10 
# Cập nhật giá trị của phân tử thứ ba trong máng số nguyên


int_array.append(6) # Thêm phân tử 6 vào cuối màng số nguyên 



#Danh sách số nguyên 
my_list = [1, 2, 3, 4, 5] 
#Danh sách chuỗi 
names = ["Alice", "Bob", "Charlie"] 
#Danh sách kết hợp kiểu dữ liệu 
mixed_list = [10, "hello", 3.14, True] 


print(my_list[0]) # Truy cập phân tử đầu tiên: Kết quả: 1 
print(names[2]) # Truy cập phân tử thứ ba: Kết quả: "Charlie" 


my_list[1]=20 # Thay đổi giá trị của phần tử thứ hai 
print(my_list) # Kết quả: [1, 20, 3, 4, 5] 



names.append("David") # Thêm phần tử vào cuối danh sách 
print(names) # Kết quả: ['Alice', 'Bob', 'Charlie', 'David'] 


del my_list[2] # Xóa phân tử thứ ba khỏi danh sách 
print(my_list) # Kết quả: [1, 20, 4, 5]

for element in names:
    print(element) #in ra từng phần tử trong danh sách
    
    
#Tuple các số nguyên 
my_tuple = (1, 2, 3, 4, 5) 
#Tuple các chuỗi 
names = ("Alice", "Bob", "Charlie") 
# Tuple kết hợp kiểu dữ liệu 
mixed_tuple = (10, "hello", 3.14) 


print(my_tuple[0])   #Truy cập phần từ đầu tiên: Kết quả: 1 
print(names [2])     # Truy cập phần từ thứ ba: Kết quá: 'Charlie 


my_tuple (1, 2, 3, 1, 4, 1) 
print(my_tuple.count(1)) # Kết quả: 3 (1 xuất hiện 3 làn trong tuple) 



my_tuple ('a', 'b', 'c', 'd', 'b') 
print(my_tuple.index('b')) 
# Kết quả: 1 (chỉ số đầu tiên của 'b' trong tuple là 1)


# Khai báo một dictionary rồng 
my_dict={}
# Khai báo một dictionary với các cặp key-value 
person = {"name": "Alice", "age": 25, "city": "New York"} 


print(person ["name"]) # In giá trị của key "name": Kết quả: "Alice" 
print(person["age"]) # In giá trị của key "age": Kết quả: 25 

# Thêm một cập key-value mới 
person["email"] = "alice@example.com" 
# Cập nhật giá trị của key đã tồn tại 
person ["age"] = 26 


# Xóa một cặp key value từ dictionary 
del person["city"] 
# Xóa phần tử và lây giá trị của key 
age = person.pop("age") 


print(person.keys()) 
# In ra tất cả các keys trong dictionary 
print(person.values()) 
# In ra tất cả các values trong dictionary 
print(person.items()) 
# In ra tất cả các cặp key-value trong dictionary


# Định nghĩa một lớp đơn giản 
class Car: 
   def   __init__(self, brand, model): 
     self.brand = brand 
     self.model = model 
   def get_info(self): 
        return f"{self.brand} {self.model}" 
    
    
    
# Tạo đối tượng từ lớp Car 
my_car = Car("Toyota", "Corolla") 
# Gọi phương thức của đối tượng 
print(my_car.get_info()) 
# Kết quả: Toyota Corolla



class ClassName: 
  def _init_(self, parameter1, parameter2, ...):
    self.parameter1 = parameter1 
    self.parameter2 = parameter2 
# ...


class Car: 
   def _init__(self, brand, model): 
     self.brand = brand 
     self.model = model 
   def get_info(self): 
     return f"{self.brand} {self.model}" 
# Tạo đối tượng từ lớp Car và truy cập thông tin 
my_car = Car("Toyota", "Corolla") 
print(my_car.get_info()) 
# Kết quả: Toyota Corolla



class ClassName: 
   def _init_(self, attribute1, attribute2):
       
     self.attribute1 = attribute1 # Thuộc tính instance 
     
     self.attribute2 = attribute2 # Thuộc tính instance 
   class_attribute = "Class Attribute" # Thuộc tính lớp 


# Tạo đối tượng từ lớp và truy cập các thuộc tính 
object_name = ClassName (value1, value2) 
print(object_name.attribute1) # Truy cập thuộc tính instance 
print(object_name.class_attribute) # Truy cập thuộc tính lớp


class ClassName: 
    def method_name(self, parameter1, parameter2): 
# Các thao tác hoặc xử lý 
      return something #Trả về kết quả (nếu cần) 
  
  
  
# Tạo đối tượng từ lớp và gọi phương thức 
object_name = ClassName() 
# Gọi phương thức và truyền các tham số 
object_name.method_name(value1, value2) 



class ParentClass: 
# Định nghĩa các thuộc tính và phương thức của lớp cha 
class ChildClass (ParentClass): 
# Định nghĩa các thuộc tĩnh và phương thức mới hoặc mở rộng từ lớp cha 


class ParentClass1: 
# Định nghĩa các thuộc tỉnh và phương thức của lớp cha 1 
class ParentClass2: 
#Định nghĩa các thuộc tỉnh và phương thức của lớp cha 2 
class ChildClass(ParentClass1, ParentClass2): 
# Định nghĩa các thuộc tính và phương thức mới hoặc mở rộng từ các lớp cha 


class Calculation: 
      def add(self, a, b): 
        return a+b 
      def add(self, a, b, c): 
        return a+b+c 
    
    
class Animal: 
    def make_sound(self): 
       return "Generic sound" 
class Dog(Animal): 
     def make_sound(self): 
       return "Woof!"
class Cat(Animal): 
    def make_sound(self): 
      return "Meow!" 
# Đa hình tại thời điển chạy 
    def animal_sound(animal): 
     return animal.make_sound() 
dog = Dog() 
cat = Cat() 
print(animal_sound(dog))  # Kết quả: Woof! 
print(animal_sound(cat))  # Kết quả: Meow!



from abc import ABC, abstractmethod

# Lớp trừu tượng 
class Animal(ABC): 
    @abstractmethod 
    def make_sound(self): 
        pass 

# Lớp con thực hiện (định nghĩa phương thức cụ thể) 
class Dog(Animal): 
    def make_sound(self): 
        return "Woof!" 

# Lớp con thực hiện (định nghĩa phương thức cụ thể) 
class Cat(Animal): 
    def make_sound(self): 
        return "Meow!" 

# Sử dụng các đối tượng trừu tượng 
dog = Dog() 
cat = Cat()  # Sửa lỗi: thiếu dấu '=' ở đây

print(dog.make_sound()) 
# Kết quả: Woof! 
print(cat.make_sound()) 
# Kết quả: Meow!

   





