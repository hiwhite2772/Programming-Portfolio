class Restaurant:
    def __init__(self):
        self.menu = {
            "Phở Bò" : 35000,
            "Phở Gà" : 35000,
            "Bún Chả" : 40000,
            "Bánh Đa Cua" : 25000,
            "Hủ Tiếu" : 35000,
            "Cháo Lươn" : 35000,
            "Nem Nướng" : 45000,
            "Bánh Tráng Trộn" : 20000,
            "Bánh Tráng Nướng" : 25000,
            "Chè Bưởi" : 15000,
            "Chè Sầu Riêng" : 15000,
            "Trà Đá" : 7000,
            "Trà Đào" : 20000,
            "Trà Tắc" : 20000,
            "Trà Sữa" : 20000,
            "Nước Suối": 10000
        }
        self.orders = {}

    def display_menu(self):
        print("\n================THỰC ĐƠN================")
        for i, (order_name, price) in enumerate(self.menu.items(), start=1):
            print(f"{i:2} - {order_name:<20} {price:>10,} VND")
        print("Chọn Q để thanh toán và thoát")
        print("==========================================")
    
    def add_order(self, order_name, quantity):
        if order_name in self.orders:
            self.orders[order_name] += quantity
        else:
            self.orders[order_name] = quantity
        
        price = self.menu[order_name]
        subtotal = price * quantity

        print(f"Đã thêm: {order_name} x {quantity} = {subtotal:,} VND")

    def print_bill(self):
        print("\n=================HOÁ ĐƠN=================")
        print(f"{"Tên món":<20} {"SL":<7} {"Giá tiền":>10} {"Thành tiền":>15}")
        total_quantity = 0
        total_price = 0
        for order_name, quantity in self.orders.items():
            price = self.menu[order_name]
            subtotal = price * quantity

            total_quantity += quantity
            total_price += subtotal
        
            print(f"{order_name:<20} {quantity:<5} {price:>10} {subtotal:>15}")
        print("==========================================")
        print(f"Tổng số lượng: {total_quantity}")
        print(f"Tổng tiền: {total_price:,} VND")
        print("Cảm ơn quý khách. Chúc quý khách ngon miệng!")
        print("==========================================")

    def order_menu(self):
        menu_items = list(self.menu.items())
        self.display_menu()
        while True:
            choice = input("\nNhập số món hoặc Q để dừng lại: ").strip()

            if choice.upper() == "Q":
                if not self.orders:
                    print("\nQuý khách chưa gọi món nào!")
                    continue
                self.print_bill()
                break

            if not choice.isdigit():
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")
                continue
        
            choice_number = int(choice)

            if choice_number < 1 or choice_number > len(menu_items):
                print("Số món không hợp lệ. Vui lòng nhập số món lại!")
                continue

            order_name = menu_items[choice_number - 1][0]
            quantity_input = input(f"Nhập số lượng của {order_name}: ").strip()

            if not quantity_input.isdigit():
                print("Số lượng phải là số nguyên. Vui lòng nhập số lại!")
                continue
            quantity_number = int(quantity_input)
            if quantity_number <= 0:
                print("Số nguyên phải lớn hơn 0!")
                continue

            self.add_order(order_name, quantity_number)

            
restaurant = Restaurant()
restaurant.order_menu()
