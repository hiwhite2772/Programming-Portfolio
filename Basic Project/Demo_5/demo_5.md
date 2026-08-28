# 📔 Personal Diary & Data Management

## 1. Giới thiệu

Đây là một dự án cá nhân nhỏ được xây dựng bằng **Python**, bắt đầu từ một ứng dụng nhật ký chạy trên Terminal/CLI.

Ứng dụng cho phép người dùng viết nhật ký, xem lại nội dung, tìm kiếm theo từ khóa và thống kê dữ liệu đã lưu.

Mục tiêu ban đầu của dự án là luyện tập các kiến thức Python cơ bản như `function`, xử lý file, xử lý chuỗi, `datetime`, exception handling và tổ chức chương trình thành các chức năng riêng.

Về lâu dài, dự án có thể được mở rộng từ một ứng dụng lưu trữ bằng file `.txt` thành một **Personal Diary Data Application**, sử dụng JSON, database và SQL để quản lý dữ liệu có cấu trúc tốt hơn.

---

## 2. Mục tiêu

### Giai đoạn hiện tại

* Làm quen với File Handling trong Python
* Đọc và ghi dữ liệu bằng `open()`
* Sử dụng function
* Sử dụng vòng lặp và menu CLI
* Xử lý chuỗi bằng `strip()`, `lower()` và `split()`
* Sử dụng `datetime` để lưu thời gian
* Tìm kiếm dữ liệu theo từ khóa
* Thống kê dữ liệu
* Xử lý lỗi bằng `try / except`

### Mục tiêu mở rộng

* Sửa nội dung nhật ký
* Xóa mục nhật ký
* Tìm kiếm theo ngày
* Phân loại nhật ký bằng tag/category
* Lưu dữ liệu dạng JSON
* Lưu dữ liệu vào SQLite/PostgreSQL
* Truy vấn nhật ký bằng SQL
* Thống kê dữ liệu theo ngày/tháng
* Xây dựng giao diện cho ứng dụng

---

## 3. Công nghệ

### Current

* Python
* Function
* Loop
* File Handling
* String Processing
* List Comprehension
* Exception Handling
* `datetime`
* TXT

### Planned

* JSON
* CSV
* SQLite
* PostgreSQL
* SQL
* Tkinter
* Git / GitHub

---

## 4. Kiến trúc hiện tại

```text
User
  ↓
CLI Menu
  ↓
Diary Functions
  ↓
Write / Read / Search / Statistics
  ↓
nhat_ky.txt
```

Kiến trúc dự kiến trong tương lai:

```text
User
  ↓
Diary Application
  ↓
Data Validation
  ↓
Diary Data
  ↓
JSON / Database
  ↓
SQL
  ↓
Statistics / Analysis
```

---

## 5. Dữ liệu nhật ký hiện tại

Mỗi mục nhật ký hiện được lưu theo dạng:

```text
[timestamp] content
```

Ví dụ:

```text
[2026-08-27 19:20] Hôm nay học Python
[2026-08-27 20:15] Ôn lại xử lý file
[2026-08-27 21:30] Tìm hiểu thư viện datetime
```

Trong đó:

| Field     | Description            |
| --------- | ---------------------- |
| timestamp | Thời điểm viết nhật ký |
| content   | Nội dung nhật ký       |

Trong tương lai, dữ liệu có thể được chuyển sang JSON:

```json
{
    "timestamp": "2026-08-27 21:30",
    "content": "Tìm hiểu thư viện datetime"
}
```

---

## 6. Chức năng hiện tại

### Viết nhật ký

Người dùng nhập nội dung và chương trình tự động thêm thời gian:

```text
Nội dung: Hôm nay mình học Python
```

Dữ liệu được lưu:

```text
[2026-08-27 21:31] Hôm nay mình học Python
```

### Xem nhật ký

Chương trình đọc toàn bộ nội dung từ `nhat_ky.txt`.

### Tìm kiếm

Người dùng có thể nhập từ khóa:

```text
Từ khoá: Python
```

Chương trình tìm các dòng chứa từ khóa và không phân biệt chữ hoa/chữ thường.

### Thống kê

Ứng dụng có thể thống kê:

```text
Số mục: 5 | Tổng từ: 42
```

---

## 7. Các giai đoạn phát triển

### Phase 1 — Basic Personal Diary

* [x] Menu CLI
* [x] Viết nhật ký
* [x] Ghi dữ liệu vào file
* [x] Tự động thêm timestamp
* [x] Xem toàn bộ nhật ký
* [x] Tìm kiếm theo từ khóa
* [x] Thống kê số mục
* [x] Thống kê tổng số từ
* [x] Xử lý `FileNotFoundError`
* [x] Exit command

### Phase 2 — Improve Diary Management

* [ ] Tìm kiếm theo ngày
* [ ] Sửa một mục nhật ký
* [ ] Xóa một mục nhật ký
* [ ] Validation dữ liệu đầu vào
* [ ] Thêm ID cho mỗi mục
* [ ] Thêm category/tag
* [ ] Tách logic thành các module riêng

### Phase 3 — Structured Data

* [ ] Chuyển dữ liệu TXT sang JSON
* [ ] Thiết kế cấu trúc dữ liệu nhật ký
* [ ] Export dữ liệu sang CSV
* [ ] Đọc dữ liệu JSON bằng Python
* [ ] Xử lý và làm sạch dữ liệu

### Phase 4 — Database

* [ ] Thiết kế bảng `diary_entries`
* [ ] Sử dụng SQLite
* [ ] Thực hiện CRUD
* [ ] Viết SQL queries
* [ ] Tìm kiếm dữ liệu bằng SQL
* [ ] Thống kê dữ liệu từ database
* [ ] Tìm hiểu PostgreSQL

### Phase 5 — Application

* [ ] Xây dựng giao diện bằng Tkinter
* [ ] Form viết nhật ký
* [ ] Danh sách các mục nhật ký
* [ ] Search interface
* [ ] Statistics interface
* [ ] Kết nối giao diện với database

---

## 8. Kiến thức Python được sử dụng

### File Handling

```python
open()
read()
write()
```

Chế độ file:

```text
"a" → append dữ liệu vào cuối file
"r" → đọc dữ liệu từ file
```

### String Processing

```python
strip()
lower()
split()
```

### Datetime

```python
datetime.now()
strftime()
```

Ví dụ:

```python
datetime.now().strftime("%Y-%m-%d %H:%M")
```

### Exception Handling

```python
try:
    ...
except FileNotFoundError:
    ...
```

### List Comprehension

Ví dụ tìm kiếm dữ liệu:

```python
ket_qua = [
    dong for dong in f
    if tu_khoa.lower() in dong.lower()
]
```

---

## 9. Hướng phát triển

Dự án hiện tại không chỉ nhằm tạo một chương trình ghi chú đơn giản.

Mục tiêu là sử dụng ứng dụng nhật ký làm một project để từng bước học cách dữ liệu được:

```text
User Input
    ↓
Python Application
    ↓
Data Collection
    ↓
File Storage
    ↓
Structured Data
    ↓
Database
    ↓
SQL
    ↓
Data Analysis
```

Ở phiên bản đầu tiên, dữ liệu chỉ được lưu trong:

```text
nhat_ky.txt
```

Sau đó project có thể tiến dần:

```text
TXT
 ↓
JSON / CSV
 ↓
SQLite
 ↓
PostgreSQL
 ↓
SQL
 ↓
Application / Analytics
```

Qua đó, một project Python cơ bản có thể trở thành một ứng dụng quản lý dữ liệu cá nhân có cấu trúc.

---

## 10. Learning Goals

Thông qua dự án này, tôi muốn cải thiện:

* Python programming
* Function design
* File handling
* String processing
* Datetime
* Exception handling
* Data structures
* JSON / CSV
* SQL
* Database fundamentals
* CRUD operations
* Data management
* Git / GitHub
* Application development

---

## 11. Project Status

**Current status:** Basic Personal Diary CLI

**Current storage:** TXT file

**Next milestone:** Improve diary management → Search / Edit / Delete

**Data milestone:** TXT → JSON / SQLite

**Long-term direction:** Personal Diary + Database + Data Management Application
