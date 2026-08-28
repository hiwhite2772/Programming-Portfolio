# Đoán mật khẩu bằng thuật toán leo đồi

## 1. Giới thiệu

Đây là chương trình Python mô phỏng quá trình đoán mật khẩu bằng thuật toán **Hill Climbing**. Chương trình tạo một chuỗi ngẫu nhiên và cải thiện chuỗi đó qua từng vòng cho đến khi giống mật khẩu mục tiêu.

## 2. Mục tiêu

Dự án giúp người học hiểu:

- Cách hoạt động của thuật toán Hill Climbing.
- Cách xây dựng hàm đánh giá Fitness.
- Cách xử lý chuỗi và ký tự trong Python.
- Cách kiểm tra mật khẩu phổ biến.

## 3. Chức năng chính

- Nhập mật khẩu mục tiêu.
- Kiểm tra độ dài mật khẩu.
- Cảnh báo mật khẩu phổ biến.
- Tạo chuỗi ngẫu nhiên.
- Đếm ký tự đúng vị trí và sai vị trí.
- Hiển thị quá trình tìm kiếm.

## 4. Cấu trúc dự án

```text
project/
├── main.py
├── passwords.txt
└── README.md
```

- `main.py`: Chương trình chính.
- `passwords.txt`: Danh sách mật khẩu phổ biến.
- `README.md`: Tài liệu dự án.

## 5. Thiết kế chương trình

Chương trình gồm các hàm:

- `feedback()`: Đánh giá độ chính xác.
- `print_status()`: Hiển thị trạng thái.
- `random_wrong_char()`: Tạo ký tự sai ngẫu nhiên.
- `create_next_state()`: Tạo trạng thái tốt hơn.
- `hill_climbing()`: Điều khiển quá trình tìm kiếm.
- `load_common_passwords()`: Đọc danh sách mật khẩu phổ biến.

## 6. Nguyên lý hoạt động

Chương trình bắt đầu bằng một chuỗi ngẫu nhiên có cùng độ dài với mật khẩu. Sau mỗi vòng, các vị trí đúng được giữ lại và một vị trí sai được sửa thành đúng. Quá trình kết thúc khi chuỗi hiện tại trùng với mật khẩu mục tiêu.

## 7. Cách tính Fitness

Fitness là số ký tự đúng và nằm đúng vị trí:

```text
Fitness = Số ký tự đúng vị trí / Tổng số ký tự
```

Chương trình cũng đếm số ký tự đúng nhưng đang nằm sai vị trí.

## 8. Điều kiện mật khẩu

Mật khẩu phải:

- Không được để trống.
- Có từ 4 đến 20 ký tự.
- Không nằm trong danh sách mật khẩu phổ biến.

Mật khẩu được chuyển thành chữ in hoa trước khi xử lý.

## 9. Cách chạy

Đặt `main.py` và `passwords.txt` trong cùng thư mục, sau đó chạy:

```bash
python main.py
```

Nhập mật khẩu mục tiêu khi chương trình yêu cầu.

## 10. Ví dụ kết quả

```text
Hãy nhập mật khẩu mục tiêu: CODE

Bắt đầu: A7PD -> Fitness: 1/4
Vòng 1: C2PD -> Fitness: 2/4
Vòng 2: CO8E -> Fitness: 3/4
Vòng 3: CODE -> Fitness: 4/4

Tìm thấy: CODE sau 3 bước!
```

Kết quả mỗi lần chạy có thể khác nhau do sử dụng dữ liệu ngẫu nhiên.

## 11. Ứng dụng

Dự án phù hợp để:

- Học Python cơ bản.
- Minh họa thuật toán tìm kiếm.
- Thực hành xây dựng hàm Fitness.
- Tìm hiểu cách đánh giá mật khẩu.
- Làm bài tập nhập môn trí tuệ nhân tạo.

## 12. Hướng phát triển

Có thể nâng cấp chương trình bằng cách:

- Hỗ trợ chữ thường và ký tự đặc biệt.
- Thêm giao diện bằng Tkinter hoặc Streamlit.
- Vẽ biểu đồ Fitness theo từng vòng.
- Áp dụng Random Restart.
- So sánh với Genetic Algorithm và Simulated Annealing.

> Đây là chương trình mô phỏng phục vụ học tập. Chương trình biết trước mật khẩu mục tiêu và không phải công cụ bẻ khóa mật khẩu thực tế.