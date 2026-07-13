#Lớp thuộc thông tin
class Person:
    #Thuộc tính thông tin
    def __init__(self, name, birthday, job, category):
        self.name = name
        self.birthday = birthday
        self.job = job
        self.category = category
    #In ra thông tin
    def to_string(self):
        return f"{self.name}|{self.birthday}|{self.job}|{self.category}"
    
    @staticmethod
    def from_string(data):
        name, birthday, job, category = data.strip().split("|")
        return Person(name, birthday, job, category)

#Lớp quản lý thông tin
class ManagerPerson:
    def __init__(self, file = "data.txt"):
        self.file = file
        self.people = []
        self.load_from_file()
        
    #Đọc file
    def load_from_file(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                for line in f:
                    self.people.append(Person.from_string(line))
        except FileNotFoundError:
            print("Khong tim thay tep tin. Tao file moi!")
    #Lưu file: Ghi file
    def save_to_file(self):
        with open(self.file, "w", encoding="utf-8") as f:
            for person in self.people:
                f.write(person.to_string() + "\n")
    #Thêm thông tin
    def add_person(self):
        name = input("Nhap ho va ten: ")
        birthday = input("Nhap ngay sinh: ")
        job = input("Nhap ten nghe nghiep: ")
        category = input("Loai doi tuong: ")
        
        p = Person(name, birthday, job, category)
        self.people.append(p)  #Thêm thông tin vào danh sách
        self.save_to_file()  #Lưu thông tin trong file
    #Hiển thị danh sách thông tin
    def show_all(self):
        if not self.people:
            print("Danh sach rong!")
            
        
        for i, p in enumerate(self.people):
            print(f"{i} - {p.name} | {p.birthday} | {p.job} | {p.category}") 
    #Cập nhật thông tin
    def update_infor(self):
        self.show_all()
        
        ix = int(input("\nNhap chinh sua so: "))
        
        if 0 <= ix < len(self.people):
            p = self.people[ix]
            
            p.name = input("Nhap ho va ten: ")
            p.birthday = input("Nhap ngay sinh: ")
            p.job = input("Nhap ten nghe nghiep: ")
            p.category = input("Loai doi tuong: ")
            
            self.save_to_file()
            
        else:
            print("Vi tri khong hop le!")
    #Xoá thông tin
    def delete_infor(self):
        self.show_all()
        
        ix = int(input("\nNhap chinh sua so: "))
        
        if 0 <= ix < len(self.people):
            del self.people[ix]
            print(f"Da xoa thong tin so {ix}")
            self.save_to_file()
        else:
            print("Vi tri khong hop le!")
    #Tổng số thông tin trong danh sách
    def count_all(self):
        print(f"Tong so thong tin: {len(self.people)}")
    

def main():
    manager = ManagerPerson()
    
    while True:
        print("\n==========Menu==========")
        print("1. Them thong tin moi")
        print("2. Hien thi thong tin")
        print("3. Chinh sua thong tin")
        print("4. Xoa thong tin")
        print("5. Tong so thong tin trong danh sach")
        print("0. Thoat!")
        
        try:
            choice = int(input("\nNhap lua chon: ").strip())
            #Nếu lựa chọn không hợp lệ
            if choice not in [1, 2, 3, 4, 5, 0]:
                print("Khong hop le!")
            
            if choice == 1:
                manager.add_person()
            elif choice == 2:
                manager.show_all()
            elif choice == 3:
                manager.update_infor()
            elif choice == 4:
                manager.delete_infor()
            elif choice == 5:
                manager.count_all()
            elif choice == 0:
                print("Da thoat chuong trinh!")
                break
                
        except ValueError:
            print("Vui long nhap so nguyen!")
        
if __name__ == "__main__":
    main()