# QUẢN LÝ MÁY TÍNH TÍNH TOÁN ĐƠN GIẢN
# 1 - Phép tính toán (+, -, *, /)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Lỗi không thể chia cho 0."
    return a / b

# 2 - Chương trình phép tính
if __name__ == "__main__":
    while True:
        
        # 3 - Chương trình phép tính toán
        print("\n========MENU========")
        print("0. Thoát")
        print("1. Phép cộng")
        print("2. Phép trừ")
        print("3. Phép nhân")
        print("4. Phép chia")
        
        try:
            choice = int(input("\nNhập lựa chọn: "))
        except ValueError:
            print("Vui lòng nhập số nguyên!")
            continue

        # 4 - Nếu chọn 0 thì dừng lại đó
        if choice == 0:
            print("Chương trình đã dừng lại")
            break
        
        # 5 - Nếu chọn khác trong chương trình thì báo không hợp lệ
        if choice not in [1, 2, 3, 4]:
            print("Không hợp lệ!")
            continue
        
        # 6 - Nhập dữ liệu số
        while True:
            try:
                a = float(input("Nhập a: "))
                break
            except ValueError:
                print("Vui lòng nhập số!")
            
        while True:
            try:
                b = float(input("Nhập b: "))
                break
            except ValueError:
                print("Vui lòng nhập số!")    

        # 7 - Xuất ra kết quả phép tính đó
        if choice == 1:
            print(f"\nKQ - Tổng: {add(a, b)}")

        elif choice == 2:
            print(f"\nKQ - Hiệu: {subtract(a, b)}")

        elif choice == 3:
            print(f"\nKQ - Tích: {multiply(a, b)}")

        elif choice == 4:
            print(f"\nKQ - Thương: {divide(a, b)}")
