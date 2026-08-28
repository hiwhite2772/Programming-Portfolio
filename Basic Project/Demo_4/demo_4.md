# 🤖 Simple Chatbot & Conversation Data Pipeline

## 1. Giới thiệu

Đây là một dự án cá nhân nhỏ được xây dựng bằng **Python**, bắt đầu từ một chatbot đơn giản sử dụng `dictionary`, `function`, `loop` và xử lý chuỗi.

Mục tiêu ban đầu của dự án là luyện tập các kiến thức Python cơ bản thông qua một sản phẩm có thể tương tác trực tiếp với người dùng.

Về lâu dài, dự án có thể được mở rộng theo hướng **Data Engineering** bằng cách thu thập lịch sử hội thoại, xử lý dữ liệu, lưu trữ vào database và phân tích dữ liệu tương tác của chatbot.

---

## 2. Mục tiêu

### Giai đoạn hiện tại

* Làm quen với Python `dict`
* Sử dụng function
* Sử dụng vòng lặp
* Xử lý input từ người dùng
* Xử lý chuỗi bằng `strip()` và `lower()`
* Xây dựng cơ chế hỏi → trả lời
* Xử lý trường hợp chatbot không hiểu câu hỏi

### Mục tiêu mở rộng

* Quản lý nhiều intent
* Hỗ trợ nhiều cách hỏi khác nhau
* Lưu lịch sử hội thoại
* Thu thập dữ liệu tương tác
* Xử lý dữ liệu bằng Python
* Lưu dữ liệu vào SQLite/PostgreSQL
* Truy vấn dữ liệu bằng SQL
* Xây dựng pipeline ETL
* Phân tích dữ liệu bằng Power BI

---

## 3. Công nghệ

### Current

* Python
* Dictionary
* Function
* Loop
* String processing
* `datetime`

### Planned

* JSON
* CSV
* SQLite / PostgreSQL
* SQL
* ETL
* Power BI
* Git / GitHub

---

## 4. Kiến trúc dự kiến

```text
User
  ↓
Chatbot
  ↓
Conversation Logger
  ↓
Raw Data
(JSON / CSV)
  ↓
ETL with Python
  ↓
Database
(SQLite / PostgreSQL)
  ↓
SQL Analysis
  ↓
Power BI Dashboard
```

---

## 5. Dữ liệu hội thoại dự kiến

Mỗi interaction có thể được lưu với các trường:

| Field     | Description                      |
| --------- | -------------------------------- |
| timestamp | Thời điểm người dùng đặt câu hỏi |
| question  | Câu hỏi của người dùng           |
| intent    | Nhóm ý định của câu hỏi          |
| response  | Câu trả lời của chatbot          |
| status    | Chatbot hiểu / không hiểu        |

Ví dụ:

```json
{
    "timestamp": "2026-08-23 20:13:20",
    "question": "dsa là gì",
    "intent": "dsa_definition",
    "response": "DSA là Data Structures and Algorithms...",
    "status": "success"
}
```

---

## 6. Các giai đoạn phát triển

### Phase 1 — Basic Python Chatbot

* [x] Dictionary chứa câu hỏi và câu trả lời
* [x] Function xử lý câu hỏi
* [x] Normalize input
* [x] Vòng lặp chatbot
* [x] Exit command
* [x] Default response

### Phase 2 — Improve Chatbot

* [ ] Multiple responses
* [ ] Keyword matching
* [ ] Intent classification đơn giản
* [ ] Better error handling
* [ ] Tách chatbot logic thành các function riêng

### Phase 3 — Conversation Logging

* [ ] Ghi timestamp
* [ ] Lưu câu hỏi
* [ ] Lưu câu trả lời
* [ ] Lưu intent
* [ ] Lưu trạng thái success / failed
* [ ] Export dữ liệu sang JSON hoặc CSV

### Phase 4 — Data Engineering

* [ ] Xây dựng ETL pipeline
* [ ] Data cleaning
* [ ] Data transformation
* [ ] Thiết kế database
* [ ] Import dữ liệu vào SQLite/PostgreSQL
* [ ] Viết SQL queries

### Phase 5 — Data Analytics

* [ ] Phân tích câu hỏi phổ biến
* [ ] Phân tích số lượng conversation theo ngày
* [ ] Phân tích tỷ lệ chatbot không hiểu
* [ ] Phân tích intent phổ biến
* [ ] Xây dựng Power BI dashboard

---

## 7. Ví dụ câu hỏi hiện tại

```text
User: chào

Bot: Xin chào bạn, hôm nay tôi có thể giúp gì cho bạn?
```

```text
User: ai là gì

Bot: AI là trí tuệ nhân tạo...
```

```text
User: dsa là gì

Bot: DSA (Data Structures and Algorithms)...
```

---

## 8. Hướng phát triển

Dự án không tập trung vào việc xây dựng một AI/LLM hoàn chỉnh.

Thay vào đó, chatbot được sử dụng như một **nguồn tạo dữ liệu**, từ đó phát triển thành một project thực hành về:

```text
Python
   ↓
Data Collection
   ↓
Data Processing
   ↓
ETL
   ↓
Database
   ↓
SQL
   ↓
Analytics
```

Mục tiêu cuối cùng là xây dựng một hệ thống nhỏ có khả năng **thu thập, xử lý, lưu trữ và phân tích dữ liệu hội thoại**.

---

## 9. Learning Goals

Thông qua dự án này, tôi muốn cải thiện:

* Python programming
* Data structures
* File handling
* Data processing
* SQL
* Database fundamentals
* ETL concepts
* Data pipeline thinking
* Data analysis
* Git/GitHub

---

## 10. Project Status

**Current status:** Basic Python chatbot

**Next milestone:** Conversation logging → JSON/CSV

**Long-term direction:** Simple Chatbot + Data Pipeline + Analytics
