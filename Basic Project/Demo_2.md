# 📌 Hệ Thống Quản Lý Thông Tin Cá Nhân

## 1. Mục tiêu

Xây dựng một chương trình bằng Python nhằm quản lý thông tin cá nhân cơ bản.
Hệ thống cho phép người dùng thực hiện các thao tác thêm, chỉnh sửa, xoá và xem dữ liệu, đồng thời lưu trữ thông tin vào tệp tin.

---

## 2. Mô tả dự án

Hệ thống quản lý danh sách các cá nhân với các thông tin:

* Họ tên
* Ngày sinh
* Nghề nghiệp
* Loại đối tượng (học sinh, sinh viên, học viên, nhân viên)

Dữ liệu sẽ được lưu trữ vào tệp tin để đảm bảo không bị mất khi chương trình kết thúc.

---

## 3. Thiết kế hệ thống (OOP)

### 3.1. Lớp đối tượng chính: Person

**Đại diện cho một cá nhân trong hệ thống.**

**Thuộc tính:**

* name: Họ tên
* birthday: Ngày sinh
* job: Nghề nghiệp
* category: Loại đối tượng

---

### 3.2. Lớp quản lý: PersonManager

**Quản lý danh sách các đối tượng Person.**

**Chức năng chính:**

* Thêm cá nhân mới
* Hiển thị danh sách
* Cập nhật thông tin
* Xoá cá nhân
* Đếm số lượng hiện tại
* Đọc dữ liệu từ tệp
* Ghi dữ liệu vào tệp

---

## 4. Chức năng hệ thống

### 4.1. Thêm mới

* Nhập thông tin cá nhân
* Lưu vào danh sách và tệp tin

### 4.2. Hiển thị danh sách

* In toàn bộ danh sách hiện có

### 4.3. Chỉnh sửa

* Chọn đối tượng theo vị trí (index)
* Cập nhật thông tin mới

### 4.4. Xoá

* Xoá một cá nhân khỏi danh sách

### 4.5. Thống kê

* Hiển thị tổng số lượng cá nhân

---

## 5. Lưu trữ dữ liệu

* Sử dụng tệp tin `.txt`
* Mỗi dòng tương ứng với một cá nhân
* Dữ liệu được phân tách bằng ký tự đặc biệt (ví dụ: `|`)

**Ví dụ:**
Tên | Ngày sinh | Nghề nghiệp | Loại

---

## 6. Quy trình hoạt động

**1. Khi chương trình chạy:**

   * Kiểm tra tệp tin
   * Đọc dữ liệu nếu tồn tại

**2. Người dùng chọn chức năng từ menu:**

   * Thêm / Xem / Sửa / Xoá

**3. Sau mỗi thay đổi:**

   * Ghi lại toàn bộ dữ liệu vào tệp

---

## 7. Độ phức tạp

* Mức độ: Trung bình  
* Áp dụng:

  * Lập trình hướng đối tượng (OOP)
  * Xử lý tệp tin
  * Cấu trúc dữ liệu danh sách

---

## 8. Hướng phát triển

* Thêm chức năng tìm kiếm theo tên
* Lọc theo loại đối tượng
* Kiểm tra dữ liệu đầu vào (validation)
* Xây dựng giao diện người dùng (GUI)
* Nâng cấp lưu trữ sang cơ sở dữ liệu (SQLite)

---

## 9. Kết luận

Dự án giúp củng cố kiến thức về:

* Lập trình Python cơ bản và nâng cao
* Thiết kế hệ thống hướng đối tượng
* Quản lý dữ liệu thực tế

Đây là một bước khởi đầu phù hợp cho sinh viên năm nhất trong lĩnh vực CNTT.

---
