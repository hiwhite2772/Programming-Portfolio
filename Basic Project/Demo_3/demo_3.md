# 📌 Hệ Thống Quản Lý Gọi Món Nhà Hàng

> Dự án cá nhân được xây dựng bằng Python nhằm mô phỏng quy trình gọi món, quản lý đơn hàng, thanh toán, lưu trữ hóa đơn và thống kê hoạt động kinh doanh của một nhà hàng.

## Trạng thái dự án

* [x] **Phần 1:** Hệ thống gọi món và thanh toán cơ bản
* [ ] **Phần 2:** Quản lý đơn hàng và giảm giá
* [ ] **Phần 3:** Lưu trữ, thống kê và xây dựng giao diện

**Thời gian phát triển dự kiến:** 6 tháng.

**Trạng thái hiện tại:** Đã hoàn thành chức năng cốt lõi của Phần 1.

---

<a id="muc-luc"></a>

## 📑 Mục lục

1. [Tổng quan dự án](#tong-quan-du-an)
2. [Mục tiêu dự án](#muc-tieu-du-an)
3. [Đối tượng sử dụng](#doi-tuong-su-dung)
4. [Phạm vi dự án](#pham-vi-du-an)
5. [Công nghệ sử dụng](#cong-nghe-su-dung)
6. [Thiết kế hướng đối tượng](#thiet-ke-huong-doi-tuong)
7. [Cấu trúc dữ liệu](#cau-truc-du-lieu)
8. [Phần 1 – Hệ thống gọi món cơ bản](#phan-1)
9. [Phần 2 – Quản lý đơn hàng và giảm giá](#phan-2)
10. [Phần 3 – Lưu trữ, thống kê và giao diện](#phan-3)
11. [Quy trình hoạt động tổng quát](#quy-trinh-hoat-dong)
12. [Kiểm tra dữ liệu đầu vào](#kiem-tra-du-lieu)
13. [Kế hoạch phát triển trong 6 tháng](#ke-hoach-6-thang)
14. [Cấu trúc thư mục dự kiến](#cau-truc-thu-muc)
15. [Ứng dụng thực tế](#ung-dung-thuc-te)
16. [Giới hạn hiện tại](#gioi-han-hien-tai)
17. [Kiến thức áp dụng](#kien-thuc-ap-dung)
18. [Tiêu chí hoàn thành dự án](#tieu-chi-hoan-thanh)
19. [Hướng phát triển mở rộng](#huong-phat-trien)
20. [Kết luận](#ket-luan)

---

<a id="tong-quan-du-an"></a>

## 1. Tổng quan dự án

**Hệ Thống Quản Lý Gọi Món Nhà Hàng** là chương trình Python mô phỏng quy trình tiếp nhận món ăn và thanh toán trong một nhà hàng.

Ở phiên bản đầu tiên, chương trình hoạt động trên giao diện dòng lệnh — Console. Người dùng có thể xem thực đơn, chọn món bằng số thứ tự, nhập số lượng và thanh toán sau khi hoàn tất gọi món.

Dự án được xây dựng theo ba phần:

| Phần   | Nội dung                       | Trạng thái      |
| ------ | ------------------------------ | --------------- |
| Phần 1 | Gọi món và thanh toán cơ bản   | Đã hoàn thành   |
| Phần 2 | Quản lý đơn hàng và giảm giá   | Chưa hoàn thành |
| Phần 3 | Lưu trữ, thống kê và giao diện | Chưa hoàn thành |

Mục tiêu của dự án không chỉ là tạo một chương trình chạy được, mà còn rèn luyện khả năng phân tích yêu cầu, thiết kế hệ thống hướng đối tượng và phát triển phần mềm theo từng giai đoạn.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="muc-tieu-du-an"></a>

## 2. Mục tiêu dự án

### 2.1. Mục tiêu nghiệp vụ

Chương trình hướng đến việc mô phỏng các hoạt động cơ bản trong quy trình phục vụ nhà hàng:

* Hiển thị thực đơn cho khách hàng.
* Tiếp nhận món khách lựa chọn.
* Ghi nhận số lượng từng món.
* Cập nhật đơn hàng khi khách gọi thêm.
* Cho phép chỉnh sửa đơn hàng trước khi thanh toán.
* Áp dụng giảm giá hoặc phí dịch vụ.
* Tính tổng tiền chính xác.
* Lưu thông tin hóa đơn.
* Thống kê doanh thu và món ăn bán chạy.

### 2.2. Mục tiêu học tập

Dự án giúp người thực hiện luyện tập:

* Python cơ bản và nâng cao.
* Lập trình hướng đối tượng.
* Phân tích và chia nhỏ bài toán.
* Sử dụng cấu trúc dữ liệu phù hợp.
* Kiểm tra dữ liệu đầu vào.
* Xử lý tệp tin.
* Làm việc với cơ sở dữ liệu.
* Thiết kế giao diện người dùng.
* Quản lý phiên bản bằng Git và GitHub.
* Viết tài liệu README cho dự án.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="doi-tuong-su-dung"></a>

## 3. Đối tượng sử dụng

Phiên bản mô phỏng có thể được sử dụng bởi:

* Nhân viên phục vụ.
* Nhân viên thu ngân.
* Khách hàng gọi món tại quầy.
* Khách hàng sử dụng máy gọi món tự phục vụ.
* Người quản lý muốn theo dõi hóa đơn và doanh thu.

Trong phiên bản hiện tại, người dùng trực tiếp thao tác với chương trình thông qua bàn phím và giao diện Console.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="pham-vi-du-an"></a>

## 4. Phạm vi dự án

### 4.1. Phạm vi hiện tại

Phiên bản hiện tại tập trung vào:

* Hiển thị danh sách món ăn.
* Chọn món bằng số thứ tự.
* Nhập số lượng.
* Cộng dồn số lượng món.
* Tính thành tiền.
* In hóa đơn.
* Tính tổng số lượng và tổng tiền.

### 4.2. Phạm vi dự kiến

Trong các phần tiếp theo, dự án sẽ bổ sung:

* Xem đơn hàng hiện tại.
* Sửa số lượng món.
* Xóa món.
* Hủy đơn hàng.
* Áp dụng mã giảm giá.
* Lưu hóa đơn.
* Đọc lịch sử giao dịch.
* Thống kê doanh thu.
* Thống kê món bán chạy.
* Xây dựng giao diện Tkinter hoặc giao diện web.

### 4.3. Ngoài phạm vi ban đầu

Một số chức năng chưa được ưu tiên trong phiên bản đầu:

* Thanh toán trực tuyến.
* Kết nối máy in hóa đơn.
* Kết nối hệ thống giao hàng.
* Quản lý nhiều chi nhánh.
* Phân quyền người dùng phức tạp.
* Đồng bộ dữ liệu thời gian thực.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="cong-nghe-su-dung"></a>

## 5. Công nghệ sử dụng

### 5.1. Công nghệ hiện tại

* **Ngôn ngữ:** Python 3
* **Giao diện:** Console
* **Mô hình:** Lập trình hướng đối tượng
* **Cấu trúc dữ liệu:** Dictionary và List
* **Quản lý mã nguồn:** Git và GitHub
* **Tài liệu dự án:** Markdown

### 5.2. Công nghệ dự kiến

Tùy theo quá trình phát triển, dự án có thể sử dụng:

* JSON hoặc CSV để lưu dữ liệu.
* SQLite để quản lý hóa đơn.
* Tkinter để xây dựng giao diện máy tính.
* Flask hoặc Django nếu phát triển thành website.
* Pandas để xử lý dữ liệu thống kê.
* Matplotlib để trực quan hóa doanh thu.

Trong phạm vi sáu tháng, dự án nên ưu tiên **một loại giao diện chính**, chẳng hạn Tkinter hoặc web, thay vì thực hiện cả hai cùng lúc.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="thiet-ke-huong-doi-tuong"></a>

## 6. Thiết kế hướng đối tượng

### 6.1. Lớp hiện tại: `Restaurant`

Lớp `Restaurant` đại diện cho hệ thống gọi món của nhà hàng.

#### Thuộc tính

* `menu`: Lưu tên món và giá bán.
* `orders`: Lưu tên món và số lượng khách đã gọi.

#### Phương thức

* `display_menu()`: Hiển thị thực đơn.
* `add_order()`: Thêm món vào đơn hàng.
* `print_bill()`: Tính toán và in hóa đơn.
* `order_menu()`: Điều khiển luồng hoạt động chính.

### 6.2. Các lớp dự kiến bổ sung

Khi dự án phát triển lớn hơn, có thể tách thành các lớp riêng.

#### `MenuItem`

Đại diện cho một món ăn hoặc đồ uống.

Thuộc tính dự kiến:

* Mã món.
* Tên món.
* Giá bán.
* Danh mục.
* Trạng thái còn bán hoặc hết hàng.

#### `OrderItem`

Đại diện cho một món nằm trong đơn hàng.

Thuộc tính dự kiến:

* Món ăn.
* Số lượng.
* Đơn giá.
* Thành tiền.

#### `Order`

Đại diện cho một đơn hàng.

Thuộc tính dự kiến:

* Mã đơn hàng.
* Danh sách món.
* Tổng số lượng.
* Tổng tiền ban đầu.
* Số tiền giảm giá.
* Tổng tiền thanh toán.
* Ngày giờ tạo.
* Trạng thái đơn hàng.

#### `RestaurantManager`

Đại diện cho bộ phận quản lý hệ thống.

Chức năng dự kiến:

* Quản lý thực đơn.
* Quản lý hóa đơn.
* Quản lý doanh thu.
* Quản lý bàn.
* Quản lý trạng thái món.

Việc tách lớp sẽ giúp mã nguồn dễ đọc, dễ kiểm thử và dễ mở rộng hơn.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="cau-truc-du-lieu"></a>

## 7. Cấu trúc dữ liệu

### 7.1. Thực đơn

Thực đơn hiện được lưu bằng `dictionary`.

```text
Tên món : Giá tiền
```

Ví dụ:

```text
Phở Bò : 35000
Trà Đào : 20000
Bánh Đa Cua : 25000
```

Trong đó:

* Tên món là `key`.
* Giá tiền là `value`.

### 7.2. Đơn hàng

Đơn hàng cũng được lưu bằng `dictionary`.

```text
Tên món : Số lượng
```

Ví dụ:

```text
Phở Bò : 2
Trà Đào : 1
```

Nếu khách gọi thêm một món đã tồn tại, chương trình cộng thêm số lượng thay vì tạo mục mới.

Ví dụ:

```text
Phở Bò ban đầu : 2
Khách gọi thêm : 1
Số lượng mới   : 3
```

### 7.3. Dữ liệu hóa đơn dự kiến

Trong Phần 3, hóa đơn có thể bao gồm:

* Mã hóa đơn.
* Ngày giờ tạo.
* Danh sách món.
* Số lượng.
* Đơn giá.
* Thành tiền.
* Giảm giá.
* Thuế hoặc phí phục vụ.
* Tổng tiền cuối cùng.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="phan-1"></a>

## 8. Phần 1 — Hệ thống gọi món cơ bản

### 8.1. Trạng thái

**Đã hoàn thành chức năng chính.**

### 8.2. Mục tiêu

Xây dựng nền tảng gọi món và thanh toán trên giao diện Console.

### 8.3. Chức năng đã hoàn thành

* Hiển thị thực đơn.
* Đánh số thứ tự từng món.
* Hiển thị giá tiền.
* Chọn món bằng số.
* Nhập số lượng.
* Kiểm tra dữ liệu nhập.
* Thêm món vào đơn hàng.
* Cộng dồn số lượng món đã gọi.
* Tính thành tiền của món.
* In hóa đơn.
* Tính tổng số lượng.
* Tính tổng tiền.
* Không cho thanh toán nếu đơn hàng trống.

### 8.4. Quy trình gọi món

1. Chương trình hiển thị thực đơn.
2. Người dùng nhập số thứ tự món.
3. Chương trình kiểm tra số món.
4. Người dùng nhập số lượng.
5. Chương trình kiểm tra số lượng.
6. Món được thêm vào đơn hàng.
7. Người dùng tiếp tục gọi món.
8. Người dùng nhập `Q` để thanh toán.
9. Chương trình in hóa đơn và kết thúc.

### 8.5. Kết quả của Phần 1

Phần 1 đã tạo được luồng cơ bản:

```text
Hiển thị thực đơn
        ↓
Chọn món
        ↓
Nhập số lượng
        ↓
Kiểm tra dữ liệu
        ↓
Thêm vào đơn hàng
        ↓
Thanh toán
        ↓
In hóa đơn
```

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="phan-2"></a>

## 9. Phần 2 — Quản lý đơn hàng và giảm giá

### 9.1. Trạng thái

**Chưa hoàn thành — đang trong kế hoạch phát triển.**

### 9.2. Mục tiêu

Mở rộng chương trình để người dùng có thể kiểm tra và chỉnh sửa đơn hàng trước khi thanh toán.

### 9.3. Chức năng dự kiến

#### Quản lý đơn hàng

* Xem toàn bộ đơn hàng hiện tại.
* Hiển thị tổng tiền tạm tính.
* Thay đổi số lượng món.
* Tăng số lượng món.
* Giảm số lượng món.
* Xóa một món khỏi đơn hàng.
* Hủy toàn bộ đơn hàng.
* Tiếp tục gọi thêm món.
* Xác nhận trước khi thanh toán.

#### Quản lý giảm giá

* Nhập mã giảm giá.
* Kiểm tra mã giảm giá hợp lệ.
* Áp dụng giảm giá theo phần trăm.
* Áp dụng giảm giá theo số tiền cố định.
* Giới hạn mức giảm tối đa.
* Không cho sử dụng mã hết hạn.
* Hiển thị số tiền trước và sau giảm giá.

#### Tính phí

Có thể bổ sung:

* Thuế giá trị gia tăng.
* Phí phục vụ.
* Phí đóng gói mang về.

### 9.4. Công thức thanh toán dự kiến

```text
Tạm tính = Tổng thành tiền của các món

Tiền giảm = Tạm tính × Tỷ lệ giảm giá

Tổng thanh toán = Tạm tính - Tiền giảm + Thuế + Phí phục vụ
```

### 9.5. Kết quả mong đợi

Sau Phần 2, người dùng có thể kiểm soát đơn hàng đầy đủ trước khi thanh toán và hạn chế sai sót khi gọi món.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="phan-3"></a>

## 10. Phần 3 — Lưu trữ, thống kê và giao diện

### 10.1. Trạng thái

**Chưa hoàn thành — dự kiến thực hiện sau Phần 2.**

### 10.2. Mục tiêu

Chuyển chương trình từ mô phỏng Console thành một ứng dụng có khả năng lưu dữ liệu, xem lịch sử và thống kê hoạt động kinh doanh.

### 10.3. Lưu trữ hóa đơn

Các chức năng dự kiến:

* Tạo mã hóa đơn tự động.
* Ghi nhận ngày giờ thanh toán.
* Lưu danh sách món.
* Lưu số lượng từng món.
* Lưu tổng tiền.
* Lưu giảm giá.
* Lưu thuế và phí.
* Đọc lại hóa đơn đã lưu.
* Tìm kiếm hóa đơn theo mã hoặc ngày.

### 10.4. Phương án lưu dữ liệu

#### Giai đoạn đầu

* Tệp `.txt`
* Tệp `.csv`
* Tệp `.json`

#### Giai đoạn hoàn thiện

* Cơ sở dữ liệu SQLite

Các bảng dự kiến:

* `MENU_ITEM`
* `CATEGORY`
* `ORDER`
* `ORDER_DETAIL`
* `DISCOUNT`
* `TABLE`
* `EMPLOYEE`

### 10.5. Thống kê dữ liệu

Hệ thống dự kiến có thể thống kê:

* Tổng số hóa đơn.
* Doanh thu theo ngày.
* Doanh thu theo tháng.
* Số lượng món đã bán.
* Món ăn bán chạy nhất.
* Món ăn ít được lựa chọn.
* Giá trị trung bình của một hóa đơn.
* Mức giảm giá đã sử dụng.
* Khung thời gian có nhiều đơn hàng.

### 10.6. Giao diện

Dự án có thể lựa chọn một trong hai hướng:

#### Hướng 1: Tkinter

Phù hợp với:

* Ứng dụng máy tính.
* Phạm vi dự án cá nhân.
* Thời gian phát triển ngắn.
* Không cần máy chủ.

#### Hướng 2: Website

Có thể sử dụng Flask hoặc Django.

Phù hợp với:

* Truy cập bằng trình duyệt.
* Gọi món bằng máy tính hoặc điện thoại.
* Phát triển thành hệ thống nhiều người dùng.

Trong kế hoạch sáu tháng, nên chọn một hướng chính để bảo đảm hoàn thành dự án.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="quy-trinh-hoat-dong"></a>

## 11. Quy trình hoạt động tổng quát

```text
Khởi động chương trình
          ↓
Đọc thực đơn
          ↓
Hiển thị danh sách món
          ↓
Người dùng chọn món
          ↓
Nhập số lượng
          ↓
Kiểm tra dữ liệu
          ↓
Thêm món vào đơn hàng
          ↓
Xem hoặc chỉnh sửa đơn hàng
          ↓
Áp dụng giảm giá
          ↓
Xác nhận thanh toán
          ↓
Tính tổng tiền
          ↓
Lưu hóa đơn
          ↓
Cập nhật dữ liệu thống kê
          ↓
Kết thúc giao dịch
```

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="kiem-tra-du-lieu"></a>

## 12. Kiểm tra dữ liệu đầu vào

Chương trình cần xử lý các trường hợp sau:

### 12.1. Lựa chọn món không hợp lệ

* Nhập chữ thay vì số.
* Nhập số âm.
* Nhập số bằng 0.
* Nhập số lớn hơn tổng số món.

### 12.2. Số lượng không hợp lệ

* Nhập chữ.
* Nhập số thập phân.
* Nhập số âm.
* Nhập số lượng bằng 0.
* Nhập khoảng trắng.

### 12.3. Đơn hàng không hợp lệ

* Thanh toán khi chưa gọi món.
* Xóa món không tồn tại.
* Giảm số lượng xuống dưới 1.
* Áp dụng mã giảm giá sai.
* Áp dụng mã đã hết hạn.

### 12.4. Dữ liệu lưu trữ không hợp lệ

* Tệp dữ liệu không tồn tại.
* Tệp bị trống.
* Dữ liệu sai định dạng.
* Không thể kết nối cơ sở dữ liệu.
* Hóa đơn bị trùng mã.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="ke-hoach-6-thang"></a>

## 13. Kế hoạch phát triển trong 6 tháng

### Tháng 1 — Hoàn thiện nền tảng Phần 1

Mục tiêu:

* Hoàn thiện chương trình gọi món Console.
* Kiểm tra toàn bộ dữ liệu đầu vào.
* Chỉnh sửa cách hiển thị thực đơn.
* Chỉnh sửa định dạng hóa đơn.
* Tổ chức lại mã nguồn.
* Viết README.
* Đưa dự án lên GitHub.

Sản phẩm đầu ra:

* Chương trình gọi món cơ bản hoạt động ổn định.
* README mô tả dự án.
* Lịch sử commit rõ ràng.

### Tháng 2 — Kiểm thử và cải thiện OOP

Mục tiêu:

* Tách trách nhiệm của các phương thức.
* Xem xét tách thêm lớp.
* Viết các trường hợp kiểm thử.
* Sửa lỗi phát sinh.
* Cải thiện tên biến và cấu trúc mã nguồn.
* Thêm chú thích cho các phần khó hiểu.

Sản phẩm đầu ra:

* Mã nguồn dễ đọc hơn.
* Hạn chế lỗi nhập liệu.
* Cấu trúc OOP rõ ràng hơn.

### Tháng 3 — Phát triển quản lý đơn hàng

Mục tiêu:

* Xem đơn hàng hiện tại.
* Thay đổi số lượng.
* Xóa món.
* Hủy đơn.
* Tiếp tục gọi thêm món.
* Xác nhận trước khi thanh toán.

Sản phẩm đầu ra:

* Hoàn thiện phần quản lý đơn hàng của Phần 2.

### Tháng 4 — Phát triển giảm giá và thanh toán

Mục tiêu:

* Xây dựng mã giảm giá.
* Kiểm tra điều kiện áp dụng.
* Tính số tiền được giảm.
* Bổ sung thuế hoặc phí phục vụ.
* Hiển thị hóa đơn chi tiết.
* Kiểm thử các trường hợp thanh toán.

Sản phẩm đầu ra:

* Hoàn thành Phần 2.

### Tháng 5 — Lưu trữ và thống kê

Mục tiêu:

* Tạo mã hóa đơn.
* Lưu thời gian thanh toán.
* Lưu hóa đơn bằng JSON hoặc SQLite.
* Đọc lịch sử hóa đơn.
* Tính doanh thu.
* Thống kê món bán chạy.

Sản phẩm đầu ra:

* Hệ thống có khả năng lưu dữ liệu.
* Có báo cáo thống kê cơ bản.

### Tháng 6 — Xây dựng giao diện và hoàn thiện dự án

Mục tiêu:

* Chọn Tkinter hoặc web.
* Xây dựng giao diện thực đơn.
* Xây dựng giao diện đơn hàng.
* Xây dựng giao diện thanh toán.
* Kết nối giao diện với dữ liệu.
* Kiểm thử toàn bộ hệ thống.
* Cập nhật README.
* Bổ sung ảnh minh họa.
* Hoàn thiện phiên bản phát hành đầu tiên.

Sản phẩm đầu ra:

* Hoàn thành Phần 3.
* Có phiên bản ứng dụng sử dụng được.
* Có tài liệu dự án đầy đủ trên GitHub.

### Bảng tiến độ tổng quát

| Thời gian | Nội dung chính            | Phần   |
| --------- | ------------------------- | ------ |
| Tháng 1   | Hoàn thiện gọi món cơ bản | Phần 1 |
| Tháng 2   | Kiểm thử và cải thiện OOP | Phần 1 |
| Tháng 3   | Quản lý đơn hàng          | Phần 2 |
| Tháng 4   | Giảm giá và thanh toán    | Phần 2 |
| Tháng 5   | Lưu trữ và thống kê       | Phần 3 |
| Tháng 6   | Giao diện và hoàn thiện   | Phần 3 |

> Tiến độ có thể thay đổi tùy lịch học. Chất lượng và mức độ hiểu mã nguồn được ưu tiên hơn việc hoàn thành quá nhanh.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="cau-truc-thu-muc"></a>

## 14. Cấu trúc thư mục dự kiến

### 14.1. Phiên bản hiện tại

```text
restaurant-order-management/
│
├── restaurant.py
└── README.md
```

### 14.2. Phiên bản mở rộng

```text
restaurant-order-management/
│
├── main.py
├── README.md
├── requirements.txt
│
├── models/
│   ├── menu_item.py
│   ├── order_item.py
│   └── order.py
│
├── services/
│   ├── menu_service.py
│   ├── order_service.py
│   └── report_service.py
│
├── data/
│   ├── menu.json
│   └── restaurant.db
│
├── ui/
│   └── restaurant_ui.py
│
├── tests/
│   ├── test_order.py
│   └── test_discount.py
│
└── screenshots/
```

Cấu trúc trên là định hướng dài hạn, không bắt buộc phải áp dụng ngay từ Phần 1.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="ung-dung-thuc-te"></a>

## 15. Ứng dụng thực tế

Ý tưởng của dự án có thể được áp dụng vào:

* Hệ thống gọi món tại quầy.
* Máy gọi món tự phục vụ.
* Ứng dụng gọi món tại bàn.
* Hệ thống bán hàng cho quán ăn.
* Phần mềm thu ngân.
* Hệ thống quản lý hóa đơn.
* Hệ thống quản lý thực đơn.
* Hệ thống thống kê doanh thu.
* Hệ thống phân tích món ăn bán chạy.
* Hệ thống hỗ trợ quyết định kinh doanh.

Dữ liệu từ hệ thống có thể giúp nhà hàng:

* Biết món nào được gọi nhiều nhất.
* Phát hiện món bán chậm.
* Lập kế hoạch nhập nguyên liệu.
* Đánh giá hiệu quả chương trình giảm giá.
* Theo dõi doanh thu theo thời gian.
* Tối ưu hóa thực đơn.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="gioi-han-hien-tai"></a>

## 16. Giới hạn hiện tại

Phiên bản hiện tại vẫn còn các giới hạn:

* Chỉ chạy trên Console.
* Thực đơn nằm trực tiếp trong mã nguồn.
* Chưa quản lý danh mục món.
* Chưa có chức năng tìm kiếm.
* Chưa xem được đơn hàng tạm thời.
* Chưa sửa số lượng món.
* Chưa xóa món.
* Chưa có mã giảm giá.
* Chưa có thuế hoặc phí phục vụ.
* Chưa lưu hóa đơn.
* Chưa sử dụng cơ sở dữ liệu.
* Chưa có giao diện.
* Chưa quản lý bàn.
* Chưa quản lý nhân viên.
* Chưa phân quyền người dùng.

Các giới hạn này sẽ được giải quyết dần trong Phần 2 và Phần 3.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="kien-thuc-ap-dung"></a>

## 17. Kiến thức áp dụng

### Kiến thức hiện tại

* Biến và kiểu dữ liệu.
* Dictionary.
* List.
* Vòng lặp `for`.
* Vòng lặp `while`.
* Câu lệnh `if`.
* Hàm và phương thức.
* Lớp và đối tượng.
* Phương thức `__init__`.
* Xử lý chuỗi.
* Chuyển đổi kiểu dữ liệu.
* F-string.
* Kiểm tra dữ liệu nhập.
* Tính toán hóa đơn.

### Kiến thức dự kiến

* Xử lý ngoại lệ bằng `try-except`.
* Xử lý tệp tin.
* JSON và CSV.
* SQLite.
* Truy vấn SQL.
* Thiết kế nhiều lớp OOP.
* Kiểm thử chương trình.
* Thiết kế giao diện.
* Phân tích dữ liệu.
* Trực quan hóa dữ liệu.
* Git và GitHub.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="tieu-chi-hoan-thanh"></a>

## 18. Tiêu chí hoàn thành dự án

Dự án được xem là hoàn thành phiên bản đầu tiên khi đáp ứng được:

* [ ] Hiển thị và quản lý thực đơn.
* [ ] Gọi nhiều món trong một đơn hàng.
* [ ] Xem và chỉnh sửa đơn hàng.
* [ ] Xóa món hoặc hủy đơn.
* [ ] Áp dụng giảm giá.
* [ ] Tính tổng tiền chính xác.
* [ ] Tạo mã hóa đơn.
* [ ] Lưu hóa đơn.
* [ ] Đọc lịch sử hóa đơn.
* [ ] Thống kê doanh thu.
* [ ] Thống kê món bán chạy.
* [ ] Có giao diện sử dụng.
* [ ] Kiểm tra dữ liệu đầu vào.
* [ ] Có tài liệu README.
* [ ] Có lịch sử commit rõ ràng trên GitHub.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="huong-phat-trien"></a>

## 19. Hướng phát triển mở rộng

Sau khi hoàn thành kế hoạch sáu tháng, dự án có thể tiếp tục phát triển:

* Quản lý nhiều bàn.
* Quản lý nhân viên.
* Đăng nhập và phân quyền.
* Quản lý nguyên liệu.
* Cảnh báo món hết hàng.
* Kết nối máy in hóa đơn.
* Gọi món bằng mã QR.
* Thanh toán trực tuyến.
* Quản lý nhiều chi nhánh.
* Xây dựng dashboard quản trị.
* Dự đoán nhu cầu món ăn.
* Đề xuất món ăn theo lịch sử gọi món.

Đây là các hướng mở rộng dài hạn và không bắt buộc trong phiên bản đầu tiên.

[⬆ Quay lại mục lục](#muc-luc)

---

<a id="ket-luan"></a>

## 20. Kết luận

Hệ Thống Quản Lý Gọi Món Nhà Hàng là dự án cá nhân giúp mô phỏng một quy trình kinh doanh thực tế bằng Python.

Phần 1 tập trung xây dựng nền tảng gọi món và thanh toán cơ bản.

Phần 2 sẽ bổ sung khả năng xem, chỉnh sửa, hủy đơn hàng và áp dụng giảm giá.

Phần 3 sẽ tập trung vào lưu trữ dữ liệu, thống kê hoạt động kinh doanh và xây dựng giao diện người dùng.

Dự án được phát triển trong khoảng sáu tháng theo từng bước nhỏ. Mục tiêu quan trọng nhất là hiểu rõ quá trình xây dựng hệ thống, tự giải quyết lỗi và hoàn thiện sản phẩm dựa trên tiến độ thực tế.

[⬆ Quay lại mục lục](#muc-luc)
