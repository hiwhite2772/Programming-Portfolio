# 🧮 Chương Trình Quản Lý Phép Tính Cơ Bản

## 1. Mục tiêu

Xây dựng chương trình thực hiện các phép tính toán học cơ bản bao gồm:

* Cộng
* Trừ
* Nhân
* Chia

Chương trình hoạt động thông qua menu và cho phép người dùng lựa chọn phép toán.

---

## 2. Chức năng chính

### 2.1. Các hàm xử lý phép toán

Tạo các hàm riêng biệt cho từng phép tính:

* Hàm cộng: `add(a, b)`
* Hàm trừ: `subtract(a, b)`
* Hàm nhân: `multiply(a, b)`
* Hàm chia: `divide(a, b)`

> Lưu ý: Hàm chia cần kiểm tra trường hợp chia cho 0.

---

### 2.2. Menu chương trình

Hiển thị menu để người dùng lựa chọn:

```
1. Cộng
2. Trừ
3. Nhân
4. Chia
0. Thoát
```

---

### 2.3. Xử lý lựa chọn

* Nếu người dùng chọn đúng (1–4): thực hiện phép toán tương ứng
* Nếu chọn `0`: thoát chương trình
* Nếu nhập sai: thông báo lỗi và yêu cầu nhập lại

---

### 2.4. Nhập dữ liệu

* Người dùng nhập 2 số bất kỳ (có thể là số nguyên hoặc số thực)
* Không yêu cầu 2 số phải khác nhau

---

### 2.5. Trả kết quả

* Thực hiện phép tính dựa trên lựa chọn
* In kết quả ra màn hình

---

## 3. Xử lý ngoại lệ

Chương trình cần xử lý các trường hợp sau:

* ❌ Nhập sai kiểu dữ liệu (ví dụ: nhập chữ thay vì số)
* ❌ Chọn menu không hợp lệ
* ❌ Chia cho 0

---

## 4. Luồng hoạt động

1. Hiển thị menu
2. Người dùng chọn phép toán
3. Kiểm tra tính hợp lệ
4. Nhập 2 số
5. Thực hiện phép tính
6. In kết quả
7. Quay lại menu (trừ khi chọn thoát)

---

## 5. Độ phức tạp

* Mỗi phép toán: O(1)
* Tổng thể chương trình: đơn giản, phù hợp cho người mới học lập trình

---

## 6. Hướng phát triển (mở rộng)

* Lặp menu liên tục cho đến khi thoát
* Lưu lịch sử phép tính
* Viết lại theo hướng lập trình hướng đối tượng (OOP)
* Xây dựng giao diện đồ họa (GUI)

---

## 7. Kết luận

Đây là bài toán cơ bản nhưng quan trọng, giúp rèn luyện:

* Tư duy logic
* Tổ chức chương trình
* Xử lý dữ liệu đầu vào/đầu ra
* Kiểm soát lỗi

---
