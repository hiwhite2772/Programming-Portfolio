# 🐍 Python Learning Roadmap — Beginner → Advanced

> Tài liệu này dành cho **tất cả mọi người** — dù bạn chưa biết gì về lập trình, đã biết ngôn ngữ khác, hay là sinh viên CNTT. Học theo thứ tự từ trên xuống sẽ hiệu quả nhất.

---

## 📌 Mục lục

1. [Python là gì?](#1-python-là-gì)
2. [Cài đặt & Tạo file đầu tiên](#2-cài-đặt--tạo-file-đầu-tiên)
3. [Giai đoạn 1 — Cơ bản](#3-giai-đoạn-1--cơ-bản-beginner)
4. [Giai đoạn 2 — Trung cấp](#4-giai-đoạn-2--trung-cấp-intermediate)
5. [Giai đoạn 3 — Nâng cao](#5-giai-đoạn-3--nâng-cao-advanced)
6. [Định hướng chuyên sâu](#6-định-hướng-chuyên-sâu)
7. [Lỗi thường gặp khi mới học](#7-lỗi-thường-gặp-khi-mới-học)
8. [Lộ trình đề xuất 8–12 tuần](#8-lộ-trình-đề-xuất-812-tuần)
9. [Checklist tự đánh giá](#9-checklist-tự-đánh-giá)
10. [Project gợi ý theo level](#10-project-gợi-ý-theo-level)
11. [Công cụ & Tài nguyên](#11-công-cụ--tài-nguyên)
12. [Tips học nhanh](#12-tips-học-nhanh)

---

## 1. Python là gì?

Python là ngôn ngữ lập trình bậc cao, dễ đọc và đa mục đích. Nó được dùng trong:

- 🌐 **Web**: Django, Flask, FastAPI
- 📊 **Data Science / AI**: Pandas, NumPy, TensorFlow, PyTorch
- 🤖 **Automation**: Selenium, scripting hệ thống
- 🎮 **Game & App**: Pygame, Tkinter

**Tại sao nên chọn Python để bắt đầu?**
- Cú pháp gần với tiếng Anh → dễ đọc, dễ hiểu
- Cộng đồng khổng lồ → dễ tìm tài liệu, giải đáp lỗi
- Chạy được trên mọi hệ điều hành (Windows, macOS, Linux)

---

## 2. Cài đặt & Tạo file đầu tiên

### Bước 1 — Cài Python

Tải tại [python.org/downloads](https://www.python.org/downloads/) → chọn phiên bản mới nhất.

> ⚠️ **Windows**: Khi cài, nhớ tick vào ô **"Add Python to PATH"** — nếu bỏ qua bước này sẽ không chạy được lệnh `python` trong terminal.

Kiểm tra đã cài thành công chưa:

```bash
python --version
# hoặc trên macOS/Linux:
python3 --version
```

Kết quả sẽ hiện: `Python 3.x.x`

---

### Bước 2 — Cài IDE (trình soạn thảo code)

Dành cho người mới, khuyên dùng **VS Code** (miễn phí, nhẹ):

1. Tải tại [code.visualstudio.com](https://code.visualstudio.com/)
2. Mở VS Code → vào **Extensions** (Ctrl+Shift+X)
3. Tìm và cài **"Python"** của Microsoft

---

### Bước 3 — Tạo file `.py` đầu tiên

1. Tạo thư mục mới, ví dụ: `my-python`
2. Mở thư mục đó trong VS Code (`File → Open Folder`)
3. Tạo file mới tên `hello.py`
4. Gõ đoạn code sau:

```python
print("Hello, World!")
print("Tôi đang học Python!")
```

5. Chạy file bằng cách nhấn **▶ (Run)** ở góc trên phải, hoặc mở terminal và gõ:

```bash
python hello.py
```

**Kết quả mong đợi:**
```
Hello, World!
Tôi đang học Python!
```

🎉 Xin chúc mừng — bạn đã chạy được chương trình Python đầu tiên!

---

## 3. Giai đoạn 1 — Cơ bản (Beginner)

**🎯 Mục tiêu:** Hiểu cách Python hoạt động và viết được chương trình đơn giản.

### Nội dung cần học

- **Biến & kiểu dữ liệu**: `int`, `float`, `str`, `bool`
- **Input / Output**: `input()`, `print()`
- **Toán tử**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Điều kiện**: `if`, `elif`, `else`
- **Vòng lặp**: `for`, `while`, `break`, `continue`
- **Cấu trúc dữ liệu**: `list`, `tuple`, `set`, `dict`
- **Hàm**: `def`, tham số, giá trị trả về `return`

### Ví dụ

```python
# Hàm chào hỏi
def greet(name):
    return f"Xin chào, {name}!"

print(greet("Python"))  # → Xin chào, Python!

# Vòng lặp cơ bản
fruits = ["táo", "cam", "xoài"]
for fruit in fruits:
    print(f"Tôi thích {fruit}")
```

### Bài tập gợi ý

- Máy tính đơn giản (cộng, trừ, nhân, chia)
- Kiểm tra số nguyên tố
- Game đoán số (người dùng đoán số máy chọn ngẫu nhiên)
- Đổi nhiệt độ Celsius ↔ Fahrenheit

---

## 4. Giai đoạn 2 — Trung cấp (Intermediate)

**🎯 Mục tiêu:** Tổ chức code tốt hơn và làm việc với dữ liệu thực tế.

### Nội dung cần học

- **OOP — Lập trình hướng đối tượng**: `class`, `object`, `__init__`
- **Kế thừa (Inheritance)**, Encapsulation, Polymorphism
- **Modules & Packages**: `import`, `from ... import`
- **File handling**: đọc/ghi file `.txt`, `.json`, `.csv`
- **Exception handling**: `try`, `except`, `finally`
- **List comprehension**: cách viết ngắn gọn hơn
- **Lambda function**
- **Virtual Environment**: `venv` — tách biệt môi trường dự án

### Ví dụ

```python
# Lớp đơn giản
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}): Woof!")

# Kế thừa
class GuideDog(Dog):
    def guide(self):
        print(f"{self.name} đang dẫn đường.")

rex = GuideDog("Rex", "Labrador")
rex.bark()    # → Rex (Labrador): Woof!
rex.guide()   # → Rex đang dẫn đường.
```

```python
# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # → [1, 4, 9, 16, 25]

# Đọc file
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### Project gợi ý

- To-do list (thêm, xóa, lưu vào file)
- File organizer (tự động sắp xếp file theo đuôi)
- Web scraping đơn giản với `requests` + `BeautifulSoup`

---

## 5. Giai đoạn 3 — Nâng cao (Advanced)

**🎯 Mục tiêu:** Viết code chuyên nghiệp, hiểu sâu hệ sinh thái Python.

### Nội dung cần học

- **Decorators**: `@property`, `@staticmethod`, tự viết decorator
- **Generators**: `yield`, tiết kiệm bộ nhớ
- **Multithreading / Multiprocessing**: xử lý song song
- **Async / Await**: lập trình bất đồng bộ
- **Design Patterns**: Singleton, Factory, Observer...
- **Testing**: `pytest`, viết unit test
- **Logging**: thay thế `print()` bằng `logging`
- **Type hints**: `def add(a: int, b: int) -> int`

### Ví dụ

```python
import asyncio

async def fetch_data(name):
    print(f"Bắt đầu fetch {name}...")
    await asyncio.sleep(1)  # mô phỏng gọi API
    print(f"Xong {name}!")

async def main():
    await asyncio.gather(
        fetch_data("API 1"),
        fetch_data("API 2"),
        fetch_data("API 3"),
    )

asyncio.run(main())
```

```python
# Decorator đơn giản
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Gọi hàm: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

add(3, 5)  # → Gọi hàm: add → 8
```

---

## 6. Định hướng chuyên sâu

Sau khi nắm vững nền tảng, chọn **1 hướng** phù hợp mục tiêu của bạn:

| Hướng | Thư viện cần học | Phù hợp với |
|---|---|---|
| 📊 Data Science / AI | NumPy, Pandas, Matplotlib, Scikit-learn, PyTorch | Người thích phân tích dữ liệu, nghiên cứu |
| 🌐 Web Development | Flask / Django, REST API, SQL/MongoDB | Người muốn làm backend, fullstack |
| 🤖 Automation / DevOps | Selenium, paramiko, Docker SDK | Người thích tự động hóa, hệ thống |
| 🎮 Game / App | Pygame, Tkinter, PyQt | Người muốn làm app desktop hoặc game |

---

## 7. Lỗi thường gặp khi mới học

Đây là những lỗi **gần như ai cũng gặp** khi bắt đầu — đừng nản lòng!

### `SyntaxError` — Lỗi cú pháp

```python
# ❌ Sai
print("Hello"   # thiếu dấu )

# ✅ Đúng
print("Hello")
```

### `IndentationError` — Lỗi thụt lề

```python
# ❌ Sai — Python yêu cầu thụt lề nhất quán
def greet():
print("Hello")  # thiếu indent

# ✅ Đúng
def greet():
    print("Hello")  # 4 dấu cách
```

### `NameError` — Dùng biến chưa khai báo

```python
# ❌ Sai
print(name)  # name chưa được tạo

# ✅ Đúng
name = "Python"
print(name)
```

### `TypeError` — Sai kiểu dữ liệu

```python
# ❌ Sai
age = input("Tuổi của bạn: ")
print(age + 1)  # input() trả về str, không cộng được với int

# ✅ Đúng
age = int(input("Tuổi của bạn: "))
print(age + 1)
```

### `IndexError` — Truy cập vị trí không tồn tại

```python
# ❌ Sai
fruits = ["táo", "cam"]
print(fruits[5])  # chỉ có index 0 và 1

# ✅ Đúng
print(fruits[0])  # → táo
```

### `FileNotFoundError` — File không tồn tại

```python
# ❌ Sai
with open("data.txt") as f:  # nếu file chưa có
    pass

# ✅ Đúng — kiểm tra trước
import os
if os.path.exists("data.txt"):
    with open("data.txt") as f:
        pass
```

---

## 8. Lộ trình đề xuất 8–12 tuần

| Tuần | Nội dung | Mục tiêu cuối tuần |
|------|----------|--------------------|
| 1 | Cài đặt, cú pháp cơ bản, biến, in/nhập | Chạy được file `.py` đầu tiên |
| 2 | Điều kiện, vòng lặp, toán tử | Viết được game đoán số |
| 3 | List, Dict, Set, Tuple | Làm việc được với dữ liệu nhóm |
| 4 | Hàm, scope, tham số | Chia code thành các hàm rõ ràng |
| 5 | OOP cơ bản: class, object | Tạo được ít nhất 1 class tự viết |
| 6 | File handling, Exception, Modules | Lưu/đọc dữ liệu từ file |
| 7–8 | Project nhỏ tự chọn | Hoàn thành 1 project hoàn chỉnh |
| 9–12 | Chọn hướng chuyên sâu | Bắt đầu học thư viện cụ thể |

---

## 9. Checklist tự đánh giá

Dùng checklist này để biết mình đang ở đâu trong lộ trình.

### ✅ Giai đoạn 1 — Cơ bản

- [ ] Cài Python và chạy được file `.py` đầu tiên
- [ ] Hiểu và dùng được các kiểu dữ liệu cơ bản (`int`, `str`, `list`, `dict`)
- [ ] Viết được câu lệnh `if/elif/else`
- [ ] Dùng được vòng lặp `for` và `while`
- [ ] Định nghĩa được hàm với `def` và `return`
- [ ] Hoàn thành ít nhất 1 bài tập (máy tính, game đoán số...)

### ✅ Giai đoạn 2 — Trung cấp

- [ ] Tạo được `class` và `object`
- [ ] Hiểu kế thừa (inheritance)
- [ ] Đọc/ghi file `.txt` hoặc `.json`
- [ ] Xử lý lỗi bằng `try/except`
- [ ] Viết được list comprehension
- [ ] Tạo và dùng virtual environment (`venv`)
- [ ] Hoàn thành ít nhất 1 project (to-do app, scraper...)

### ✅ Giai đoạn 3 — Nâng cao

- [ ] Viết và hiểu được decorator
- [ ] Dùng được generator với `yield`
- [ ] Hiểu async/await cơ bản
- [ ] Viết được unit test đơn giản với `pytest`
- [ ] Dùng `logging` thay cho `print()`
- [ ] Hoàn thành 1 project nâng cao hoặc contribute open-source

---

## 10. Project gợi ý theo level

### 🟢 Beginner

- **Calculator CLI** — máy tính dòng lệnh
- **Password Generator** — tạo mật khẩu ngẫu nhiên theo yêu cầu
- **Number Guessing Game** — game đoán số với gợi ý "cao hơn/thấp hơn"
- **Unit Converter** — đổi đơn vị (km↔mile, kg↔lb...)

### 🟡 Intermediate

- **To-do App** — thêm/xóa/lưu task vào file JSON
- **Web Scraper** — crawl dữ liệu từ một trang web
- **Simple REST API** — dùng Flask tạo API CRUD cơ bản
- **File Organizer** — tự động sắp xếp file trong thư mục theo đuôi

### 🔴 Advanced

- **Chat App** — dùng socket hoặc WebSocket
- **Machine Learning Model** — phân loại ảnh hoặc dự đoán dữ liệu
- **CLI Tool** — công cụ dòng lệnh tự viết (dùng `argparse` hoặc `typer`)
- **Discord/Telegram Bot** — bot tự động trả lời hoặc xử lý lệnh

---

## 11. Công cụ & Tài nguyên

### Công cụ

| Công cụ | Dùng để làm gì |
|---------|---------------|
| [VS Code](https://code.visualstudio.com/) | Viết code (IDE nhẹ, miễn phí) |
| [PyCharm](https://www.jetbrains.com/pycharm/) | IDE chuyên cho Python (có bản Free) |
| [Git](https://git-scm.com/) | Quản lý version code |
| [GitHub](https://github.com/) | Lưu và chia sẻ code online |
| [Jupyter Notebook](https://jupyter.org/) | Chạy code từng cell, hay dùng cho Data Science |

### Tài nguyên học miễn phí

| Tên | Loại | Link |
|-----|------|------|
| Python Docs (chính thức) | Tài liệu | [docs.python.org](https://docs.python.org/3/) |
| freeCodeCamp Python | Video | [freecodecamp.org](https://www.freecodecamp.org/) |
| CS50P — Harvard | Khóa học | [cs50.harvard.edu/python](https://cs50.harvard.edu/python/2022/) |
| Real Python | Bài viết | [realpython.com](https://realpython.com/) |
| LeetCode | Luyện bài tập | [leetcode.com](https://leetcode.com/) |
| Kaggle | Data Science thực hành | [kaggle.com](https://www.kaggle.com/) |

---

## 12. Tips học nhanh

- **Code mỗi ngày** — dù chỉ 30 phút, quan trọng là đều đặn
- **Làm project sớm** — đừng chờ "học đủ" mới làm, project là cách học tốt nhất
- **Debug nhiều → hiểu sâu** — khi gặp lỗi, đừng copy-paste giải pháp ngay; đọc hiểu tại sao
- **Đọc code người khác** — vào GitHub tìm project Python nhỏ, đọc và học cách họ viết
- **Dùng Google & Stack Overflow** — đây là kỹ năng thực tế, không phải gian lận
- **Giải thích lại code** — nếu giải thích được cho người khác, tức là bạn đã thực sự hiểu

---

## 🎯 Kết luận

Python là lựa chọn tuyệt vời để bắt đầu lập trình. Hai điều quan trọng nhất:
> **Học đi đôi với làm project** — lý thuyết không thể thay thế việc tự tay viết code.
> **Kiên trì hơn tốc độ** — không cần học nhanh, cần học chắc.

Chúc bạn học tốt! 🚀

---
