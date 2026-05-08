# 🗄️ SQL — Ngôn Ngữ Truy Vấn Cấu Trúc
### Từ Cơ Bản Đến Nâng Cao

> **Structured Query Language** — Nền tảng của mọi hệ thống dữ liệu hiện đại

---

## 📌 Mục Lục

- [1. Giới Thiệu](#1-giới-thiệu)
- [2. Lịch Sử Hình Thành](#2-lịch-sử-hình-thành)
- [3. SQL Hoạt Động Như Thế Nào?](#3-sql-hoạt-động-như-thế-nào)
- [4. Quy Tắc Viết Hoa / Thường](#4-quy-tắc-viết-hoa--thường)
- [5. Các Thao Tác Cơ Bản — CRUD](#5-các-thao-tác-cơ-bản--crud)
- [6. 🟢 Bài Học Cơ Bản](#6--bài-học-cơ-bản)
- [7. 🟡 Bài Học Trung Cấp](#7--bài-học-trung-cấp)
- [8. 🔴 Bài Học Cao Cấp](#8--bài-học-cao-cấp)
- [9. SQL Trong Công Việc](#9-sql-trong-công-việc)
- [10. Các Hệ Quản Trị Phổ Biến](#10-các-hệ-quản-trị-phổ-biến)
- [11. Lỗi Thường Gặp & Cách Xử Lý](#11-lỗi-thường-gặp--cách-xử-lý)
- [12. Tổng Kết & Lộ Trình](#12-tổng-kết--lộ-trình)
- [13. Tài Nguyên Học Thêm](#13-tài-nguyên-học-thêm)

---

## 1. Giới Thiệu

**SQL** (viết tắt của *Structured Query Language*) là ngôn ngữ lập trình đặc biệt dùng để **tương tác với cơ sở dữ liệu quan hệ** (Relational Database).

SQL không phải ngôn ngữ lập trình thuần túy như Python hay Java, mà là ngôn ngữ **khai báo** — bạn nói *"cần lấy gì"* thay vì *"lấy như thế nào"*.

```sql
-- Ví dụ: Lấy top 5 sản phẩm bán chạy nhất tháng này
SELECT ten_sp, SUM(so_luong) AS tong_ban
FROM chi_tiet_don_hang
WHERE MONTH(ngay_dat) = MONTH(NOW())
GROUP BY ten_sp
ORDER BY tong_ban DESC
LIMIT 5;
```

**SQL cho phép:**

| Khả năng | Mô tả |
|----------|-------|
| 📥 Truy vấn | Lấy dữ liệu theo điều kiện bất kỳ |
| ✏️ Thao tác | Thêm, sửa, xóa bản ghi |
| 🏗️ Định nghĩa | Tạo và quản lý cấu trúc bảng |
| 🔒 Phân quyền | Kiểm soát ai được làm gì |
| 🔄 Giao dịch | Đảm bảo toàn vẹn dữ liệu |

---

## 2. Lịch Sử Hình Thành

| Năm | Sự Kiện |
|-----|---------|
| **1970** | Edgar F. Codd (IBM) công bố mô hình cơ sở dữ liệu quan hệ trong bài báo nổi tiếng |
| **1974** | Donald Chamberlin & Raymond Boyce (IBM) phát triển **SEQUEL** — tiền thân của SQL |
| **1979** | Oracle phát hành RDBMS thương mại đầu tiên sử dụng SQL |
| **1986** | ISO và ANSI chuẩn hóa SQL lần đầu tiên **(SQL-86)** |
| **1992** | **SQL-92** ra đời — phiên bản nền tảng được dùng phổ biến nhất đến nay |
| **1999** | SQL:1999 bổ sung trigger, stored procedure, hướng đối tượng |
| **2003** | SQL:2003 tích hợp XML, thêm **Window Functions** |
| **2011** | SQL:2011 hỗ trợ dữ liệu theo thời gian (temporal data) |
| **Nay** | SQL vẫn top 3 ngôn ngữ/công nghệ phổ biến nhất — Stack Overflow Survey 2024 |

```
1970      1974      1979      1986      1992      2003      Nay
 │         │         │         │         │         │         │
[Codd]  [SEQUEL]  [Oracle]  [SQL-86]  [SQL-92]  [Window   [Cloud
 lý       IBM       RDBMS    chuẩn     nền       Func.]    DB +
 thuyết   tạo ra    đầu      hóa       tảng               NoSQL
                   tiên                                    song song]
```

> 💡 SQL ra đời năm 1974 — tính đến 2026 đã gần **52 năm** tuổi, nhưng vẫn là kỹ năng không thể thiếu trong ngành Tech & Data.

---

## 3. SQL Hoạt Động Như Thế Nào?

### Kiến Trúc Tổng Quan

```
 Người dùng / Ứng dụng
         │
         │  Câu lệnh SQL
         ▼
 ┌────────────────────────┐
 │      SQL Engine        │
 │  ┌──────────────────┐  │
 │  │  Parser          │  │  ← Kiểm tra cú pháp
 │  └────────┬─────────┘  │
 │  ┌────────▼─────────┐  │
 │  │  Optimizer       │  │  ← Tìm cách thực thi nhanh nhất
 │  └────────┬─────────┘  │
 │  ┌────────▼─────────┐  │
 │  │  Executor        │  │  ← Thực thi thực sự
 │  └──────────────────┘  │
 └────────────────────────┘
         │
         ▼
 ┌────────────────────────┐
 │    Storage Engine      │  ← Đọc/ghi dữ liệu trên đĩa/RAM
 └────────────────────────┘
         │
         ▼
    Kết quả trả về
```

### Các Nhóm Lệnh SQL

| Nhóm | Tên đầy đủ | Lệnh chính | Mục đích |
|------|-----------|------------|----------|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Định nghĩa cấu trúc |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Thao tác dữ liệu |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Phân quyền truy cập |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Quản lý giao dịch |

---

## 4. Quy Tắc Viết Hoa / Thường

SQL có **3 loại thành phần** và mỗi loại có quy tắc hoàn toàn khác nhau.

---

### 4.1 — Từ Khóa SQL: KHÔNG phân biệt

```sql
-- Ba cách viết này cho kết quả GIỐNG HỆT NHAU:
SELECT * FROM san_pham WHERE gia > 1000000;
select * from san_pham where gia > 1000000;
Select * From san_pham Where gia > 1000000;
```

✅ **Quy ước chuẩn:** Viết **HOA** từ khóa SQL, viết **thường** tên bảng/cột.
Lý do: dễ đọc, phân biệt rõ đâu là lệnh SQL, đâu là tên do mình đặt.

---

### 4.2 — Tên Bảng & Tên Cột: Tùy hệ quản trị

| Hệ quản trị | Mặc định | Ghi chú |
|-------------|---------|---------|
| **MySQL** (Linux) | ✅ Phân biệt | `SanPham` ≠ `sanpham` |
| **MySQL** (Windows/macOS) | ❌ Không phân biệt | `SanPham` = `sanpham` |
| **PostgreSQL** | Tự chuyển thường | `SanPham` → lưu thành `sanpham` |
| **SQL Server** | ❌ Không phân biệt | Mặc định |
| **Oracle** | Tự chuyển HOA | `sanpham` → lưu thành `SANPHAM` |
| **SQLite** | ❌ Không phân biệt | — |

```sql
-- ⚠️ Bẫy phổ biến với PostgreSQL:
CREATE TABLE SanPham (id INT);       -- PostgreSQL lưu thành "sanpham"
SELECT * FROM "SanPham";             -- ❌ Lỗi!
SELECT * FROM sanpham;               -- ✅ Đúng

-- Muốn giữ hoa/thường → dùng nháy kép (nhưng phải dùng MÃI MÃI):
CREATE TABLE "SanPham" (id INT);
SELECT * FROM "SanPham";             -- ✅ Phải luôn có nháy kép
```

> 💡 **Lời khuyên:** Dùng `snake_case` toàn chữ thường cho tên bảng/cột để an toàn trên mọi hệ quản trị: `san_pham`, `khach_hang`, `ngay_tao`

---

### 4.3 — Giá Trị Chuỗi: Phụ thuộc Collation

Đây là loại **hay gây bug nhất** trong thực tế.

```sql
-- Mặc định thường PHÂN BIỆT hoa/thường với giá trị chuỗi:
SELECT * FROM khach_hang WHERE ho_ten = 'Nguyen Van A';  -- ✅ Tìm thấy
SELECT * FROM khach_hang WHERE ho_ten = 'nguyen van a';  -- ❌ Không thấy!

-- Giải pháp: Dùng LOWER() để chuẩn hóa trước khi so sánh
SELECT * FROM khach_hang
WHERE LOWER(ho_ten) = LOWER('nguyen van a');
```

| Collation | Ý nghĩa |
|-----------|---------|
| `utf8mb4_general_ci` | **ci** = case-insensitive → `'a' = 'A'` TRUE |
| `utf8mb4_bin` | So sánh nhị phân → `'a' = 'A'` FALSE |
| `utf8mb4_unicode_ci` | Unicode, không phân biệt → `'a' = 'A'` TRUE |

---

### 4.4 — Tóm Tắt

| Loại | Phân biệt hoa/thường? | Khuyến nghị |
|------|-----------------------|-------------|
| Từ khóa SQL (`SELECT`, `FROM`, `WHERE`…) | ❌ Không | Viết HOA cho dễ đọc |
| Tên bảng / tên cột | ⚠️ Tùy hệ quản trị | Dùng `snake_case` thường |
| Giá trị chuỗi (`'Nguyen'`, `'nguyen'`…) | ⚠️ Tùy Collation | Dùng `LOWER()` khi tìm kiếm |

---

## 5. Các Thao Tác Cơ Bản — CRUD

**CRUD** = Create · Read · Update · Delete — bốn thao tác nền tảng của mọi ứng dụng.

| Thao tác | SQL | Nhóm |
|----------|-----|------|
| **C**reate — Tạo | `INSERT INTO` | DML |
| **R**ead — Đọc | `SELECT` | DML |
| **U**pdate — Sửa | `UPDATE` | DML |
| **D**elete — Xóa | `DELETE` | DML |

> 📂 Xuyên suốt tài liệu này chúng ta sẽ dùng hệ thống **quản lý cửa hàng bán lẻ** làm ví dụ thực tế.

---

## 6. 🟢 Bài Học Cơ Bản

> **Mục tiêu:** Nắm vững nền tảng, đọc hiểu và viết được các câu lệnh SQL thông dụng.

---

### Bài 1 — Kiểu Dữ Liệu (Data Types)

Trước khi tạo bảng, cần hiểu các kiểu dữ liệu phổ biến:

#### Kiểu Số

| Kiểu | Mô tả | Ví dụ |
|------|-------|-------|
| `INT` | Số nguyên (-2 tỷ đến 2 tỷ) | `id`, `so_luong` |
| `BIGINT` | Số nguyên rất lớn | `dân số thế giới` |
| `TINYINT` | Số nguyên nhỏ (0–255) | `tuoi`, `is_active` |
| `DECIMAL(p,s)` | Số thập phân chính xác | `gia DECIMAL(15,2)` |
| `FLOAT` / `DOUBLE` | Số thập phân (có thể sai số nhỏ) | `nhiet_do` |

#### Kiểu Chuỗi

| Kiểu | Mô tả | Ví dụ |
|------|-------|-------|
| `VARCHAR(n)` | Chuỗi độ dài biến thiên, tối đa n ký tự | `ho_ten VARCHAR(100)` |
| `CHAR(n)` | Chuỗi độ dài cố định n ký tự | `ma_tinh CHAR(2)` |
| `TEXT` | Chuỗi dài không giới hạn | `mo_ta`, `noi_dung` |
| `ENUM(...)` | Tập giá trị cố định | `gioi_tinh ENUM('Nam','Nu')` |

#### Kiểu Ngày Giờ

| Kiểu | Mô tả | Ví dụ |
|------|-------|-------|
| `DATE` | Ngày (YYYY-MM-DD) | `2024-01-15` |
| `TIME` | Giờ (HH:MM:SS) | `08:30:00` |
| `DATETIME` | Ngày + Giờ | `2024-01-15 08:30:00` |
| `TIMESTAMP` | Ngày + Giờ (tự cập nhật được) | Ghi lại thời gian sửa |

#### Kiểu Khác

| Kiểu | Mô tả |
|------|-------|
| `BOOLEAN` / `TINYINT(1)` | True/False (1/0) |
| `JSON` | Lưu dữ liệu JSON (MySQL 5.7+, PostgreSQL) |
| `BLOB` | Lưu file nhị phân (ảnh, PDF...) |

---

### Bài 2 — Tạo & Xóa Bảng

```sql
-- ===== TẠO BẢNG =====

CREATE TABLE khach_hang (
    id              INT             PRIMARY KEY AUTO_INCREMENT,
    ho_ten          VARCHAR(100)    NOT NULL,
    email           VARCHAR(150)    UNIQUE,
    so_dien_thoai   VARCHAR(15),
    ngay_sinh       DATE,
    dia_chi         TEXT,
    is_active       TINYINT(1)      DEFAULT 1,
    ngay_tao        DATETIME        DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat   DATETIME        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE danh_muc (
    id      INT          PRIMARY KEY AUTO_INCREMENT,
    ten     VARCHAR(100) NOT NULL,
    mo_ta   TEXT
);

CREATE TABLE san_pham (
    id          INT             PRIMARY KEY AUTO_INCREMENT,
    ten_sp      VARCHAR(200)    NOT NULL,
    gia         DECIMAL(15, 2)  NOT NULL CHECK (gia >= 0),
    so_luong    INT             DEFAULT 0 CHECK (so_luong >= 0),
    danh_muc_id INT,
    mo_ta       TEXT,
    ngay_tao    DATETIME        DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (danh_muc_id) REFERENCES danh_muc(id)
);

CREATE TABLE don_hang (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    khach_hang_id   INT NOT NULL,
    tong_tien       DECIMAL(15, 2)  DEFAULT 0,
    trang_thai      ENUM('cho_xu_ly','dang_giao','hoan_thanh','huy') DEFAULT 'cho_xu_ly',
    ghi_chu         TEXT,
    ngay_dat        DATETIME        DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(id)
);

CREATE TABLE chi_tiet_don_hang (
    id          INT             PRIMARY KEY AUTO_INCREMENT,
    don_hang_id INT             NOT NULL,
    san_pham_id INT             NOT NULL,
    so_luong    INT             NOT NULL CHECK (so_luong > 0),
    don_gia     DECIMAL(15, 2)  NOT NULL,
    FOREIGN KEY (don_hang_id) REFERENCES don_hang(id),
    FOREIGN KEY (san_pham_id) REFERENCES san_pham(id)
);
```

```sql
-- ===== SỬA CẤU TRÚC BẢNG (ALTER) =====

ALTER TABLE khach_hang ADD COLUMN diem_tich_luy INT DEFAULT 0;
ALTER TABLE san_pham MODIFY COLUMN mo_ta VARCHAR(500);
ALTER TABLE san_pham RENAME COLUMN mo_ta TO ghi_chu;
ALTER TABLE khach_hang DROP COLUMN dia_chi;
ALTER TABLE san_pham ADD CONSTRAINT chk_gia CHECK (gia > 0);

-- ===== XÓA BẢNG =====

DROP TABLE IF EXISTS chi_tiet_don_hang;         -- Xóa cả cấu trúc + dữ liệu
TRUNCATE TABLE don_hang;                         -- Xóa dữ liệu, giữ cấu trúc, reset AUTO_INCREMENT
```

**Ràng buộc (Constraints) quan trọng:**

| Ràng buộc | Ý nghĩa |
|-----------|---------|
| `PRIMARY KEY` | Khóa chính — định danh duy nhất mỗi dòng |
| `FOREIGN KEY` | Khóa ngoại — liên kết với bảng khác |
| `NOT NULL` | Bắt buộc phải có giá trị |
| `UNIQUE` | Giá trị không được trùng nhau |
| `DEFAULT` | Giá trị mặc định nếu không nhập |
| `CHECK` | Điều kiện hợp lệ cho giá trị |
| `AUTO_INCREMENT` | Tự động tăng số (MySQL) / `SERIAL` (PostgreSQL) |

---

### Bài 3 — Chèn Dữ Liệu (`INSERT`)

```sql
-- Thêm một bản ghi
INSERT INTO danh_muc (ten, mo_ta)
VALUES ('Máy tính', 'Laptop, máy tính để bàn và phụ kiện');

-- Thêm nhiều bản ghi cùng lúc
INSERT INTO danh_muc (ten, mo_ta)
VALUES
    ('Điện thoại', 'Smartphone và phụ kiện điện thoại'),
    ('Phụ kiện',   'Chuột, bàn phím, tai nghe'),
    ('Màn hình',   'Monitor các loại');

-- Thêm sản phẩm
INSERT INTO san_pham (ten_sp, gia, so_luong, danh_muc_id)
VALUES
    ('Laptop Dell XPS 15',       35000000, 20, 1),
    ('Laptop MacBook Pro M3',    55000000, 10, 1),
    ('iPhone 16 Pro',            30000000, 15, 2),
    ('Samsung Galaxy S25',       22000000, 25, 2),
    ('Chuột Logitech MX Master',  1800000, 50, 3),
    ('Bàn phím Keychron K2',      2800000, 35, 3),
    ('Tai nghe Sony WH-1000XM5',  8500000, 20, 3),
    ('Màn hình Dell 27" 4K',     18000000, 12, 4);

-- INSERT ... SELECT: chèn dữ liệu từ bảng khác
INSERT INTO san_pham_archive (ten_sp, gia, ngay_archive)
SELECT ten_sp, gia, NOW()
FROM san_pham
WHERE so_luong = 0;

-- Upsert (INSERT ... ON DUPLICATE KEY UPDATE) — MySQL
INSERT INTO san_pham (id, ten_sp, gia, so_luong)
VALUES (1, 'Laptop Dell XPS 15', 33000000, 25)
ON DUPLICATE KEY UPDATE
    gia      = VALUES(gia),
    so_luong = VALUES(so_luong);
```

---

### Bài 4 — Truy Vấn `SELECT`

```sql
SELECT * FROM san_pham;
SELECT ten_sp, gia, so_luong FROM san_pham;

-- Đặt alias và tính toán trong SELECT
SELECT
    ten_sp          AS 'Tên Sản Phẩm',
    gia             AS 'Giá (VNĐ)',
    gia * 1.1       AS gia_sau_thue,
    so_luong * gia  AS gia_tri_ton_kho
FROM san_pham;

-- DISTINCT, LIMIT, OFFSET
SELECT DISTINCT danh_muc_id FROM san_pham;
SELECT * FROM san_pham LIMIT 3;
SELECT * FROM san_pham LIMIT 3 OFFSET 3;   -- Trang 2

-- Cấu trúc SELECT đầy đủ theo thứ tự:
SELECT   [cột hoặc biểu thức]
FROM     [bảng]
WHERE    [điều kiện lọc hàng]
GROUP BY [nhóm theo cột]
HAVING   [lọc sau khi nhóm]
ORDER BY [sắp xếp kết quả]
LIMIT    [giới hạn số dòng]
OFFSET   [bỏ qua N dòng đầu];
```

---

### Bài 5 — Lọc `WHERE`

```sql
-- Toán tử so sánh: =  !=  >  >=  <  <=
SELECT * FROM san_pham WHERE gia > 10000000;
SELECT * FROM san_pham WHERE gia != 1800000;

-- AND / OR / NOT
SELECT * FROM san_pham WHERE danh_muc_id = 3 AND gia < 3000000;
SELECT * FROM san_pham WHERE danh_muc_id = 1 OR danh_muc_id = 2;
SELECT * FROM san_pham WHERE (danh_muc_id = 1 OR danh_muc_id = 2) AND gia < 30000000;

-- BETWEEN
SELECT * FROM san_pham WHERE gia BETWEEN 1000000 AND 5000000;

-- IN / NOT IN
SELECT * FROM san_pham WHERE danh_muc_id IN (1, 2);

-- LIKE: %  = nhiều ký tự bất kỳ,  _  = đúng 1 ký tự
SELECT * FROM san_pham  WHERE ten_sp LIKE 'Laptop%';
SELECT * FROM san_pham  WHERE ten_sp LIKE '%Sony%';
SELECT * FROM khach_hang WHERE email LIKE '%@gmail.com';

-- IS NULL / IS NOT NULL
SELECT * FROM khach_hang WHERE email IS NULL;
SELECT * FROM khach_hang WHERE email IS NOT NULL;
```

---

### Bài 6 — Sắp Xếp `ORDER BY`

```sql
SELECT * FROM san_pham ORDER BY gia ASC;
SELECT * FROM san_pham ORDER BY gia DESC;

-- Nhiều cột: ưu tiên theo danh_muc_id, sau đó theo gia giảm dần
SELECT * FROM san_pham ORDER BY danh_muc_id ASC, gia DESC;

-- Sắp xếp theo alias
SELECT ten_sp, gia * 1.1 AS gia_sau_thue
FROM san_pham
ORDER BY gia_sau_thue DESC;

-- NULL khi sắp xếp: MySQL → NULL lên đầu với ASC, PostgreSQL → NULL xuống cuối
SELECT * FROM khach_hang ORDER BY email ASC NULLS LAST;  -- PostgreSQL
```

---

### Bài 7 — Cập Nhật `UPDATE`

```sql
UPDATE san_pham SET gia = 32000000 WHERE id = 1;

-- Nhiều cột cùng lúc
UPDATE san_pham SET gia = 33000000, so_luong = 18 WHERE id = 1;

-- Dựa trên giá trị hiện tại
UPDATE san_pham SET gia      = gia * 0.9       WHERE danh_muc_id = 3;
UPDATE san_pham SET so_luong = so_luong + 10   WHERE id = 5;

-- Điều kiện phức tạp
UPDATE don_hang
SET trang_thai = 'huy'
WHERE trang_thai = 'cho_xu_ly'
  AND ngay_dat < DATE_SUB(NOW(), INTERVAL 7 DAY);
```

> ⚠️ **Nguyên tắc vàng:** Luôn có mệnh đề `WHERE` khi `UPDATE`. Thiếu `WHERE` → cập nhật **toàn bộ** bảng!

---

### Bài 8 — Xóa `DELETE`

```sql
DELETE FROM san_pham WHERE id = 8;
DELETE FROM don_hang WHERE trang_thai = 'huy' AND ngay_dat < '2023-01-01';
DELETE FROM chi_tiet_don_hang WHERE don_hang_id IN (10, 11, 12);
```

**So sánh DELETE / TRUNCATE / DROP:**

| Lệnh | Điều kiện | Rollback | AUTO_INCREMENT |
|------|-----------|----------|----------------|
| `DELETE` | ✅ Có WHERE | ✅ Được | Giữ nguyên |
| `TRUNCATE` | ❌ Không | ❌ Không | Reset về 1 |
| `DROP` | — | ❌ Không | Xóa cả bảng |

> ⚠️ **Quy trình an toàn:** SELECT trước → đếm COUNT(*) → xóa trong TRANSACTION → COMMIT/ROLLBACK.

---

## 7. 🟡 Bài Học Trung Cấp

> **Mục tiêu:** Xử lý dữ liệu phức tạp, kết hợp nhiều bảng, tối ưu cơ bản.

---

### Bài 9 — Hàm Xử Lý Chuỗi

```sql
SELECT UPPER('hello world');                    -- 'HELLO WORLD'
SELECT LOWER('NGUYEN VAN AN');                  -- 'nguyen van an'
SELECT TRIM('  hello  ');                       -- 'hello'
SELECT CONCAT(ho_ten, ' - ', email) AS thong_tin FROM khach_hang;
SELECT CONCAT_WS(', ', ho_ten, email, so_dien_thoai) FROM khach_hang;

SELECT SUBSTRING('Nguyen Van An', 1, 6);        -- 'Nguyen'
SELECT REPLACE('Hello World', 'World', 'SQL');  -- 'Hello SQL'
SELECT LEFT('0901234567', 3);                   -- '090'
SELECT RIGHT('0901234567', 7);                  -- '1234567'
SELECT LPAD('42', 5, '0');                      -- '00042'
SELECT FORMAT(35000000, 0);                     -- '35,000,000'
```

---

### Bài 10 — Hàm Xử Lý Số & Ngày

```sql
-- Hàm số
SELECT ROUND(3.14159, 2);   -- 3.14
SELECT CEIL(3.2);            -- 4
SELECT FLOOR(3.9);           -- 3
SELECT ABS(-15);             -- 15
SELECT MOD(10, 3);           -- 1

-- Hàm ngày giờ
SELECT NOW();                -- '2026-05-08 10:30:00'
SELECT CURDATE();            -- '2026-05-08'
SELECT YEAR('2026-05-08');   -- 2026
SELECT MONTH('2026-05-08');  -- 5
SELECT DATE_FORMAT(NOW(), '%d/%m/%Y %H:%i');           -- '08/05/2026 10:30'
SELECT DATE_ADD('2026-05-08', INTERVAL 7 DAY);         -- '2026-05-15'
SELECT DATEDIFF('2026-12-31', '2026-05-08');           -- 237 ngày
SELECT TIMESTAMPDIFF(YEAR, ngay_sinh, NOW()) AS tuoi FROM khach_hang;
```

---

### Bài 11 — Hàm Tổng Hợp & `GROUP BY`

```sql
SELECT COUNT(*), COUNT(email), COUNT(DISTINCT danh_muc_id) FROM san_pham;
SELECT SUM(tong_tien), AVG(gia), MIN(gia), MAX(gia) FROM don_hang;

-- GROUP BY: thống kê theo danh mục
SELECT
    d.ten                   AS danh_muc,
    COUNT(sp.id)            AS so_san_pham,
    MIN(sp.gia)             AS gia_thap_nhat,
    MAX(sp.gia)             AS gia_cao_nhat,
    ROUND(AVG(sp.gia), 0)   AS gia_trung_binh
FROM san_pham sp
JOIN danh_muc d ON sp.danh_muc_id = d.id
GROUP BY d.id, d.ten
ORDER BY so_san_pham DESC;

-- HAVING: lọc SAU khi GROUP BY
SELECT danh_muc_id, SUM(gia * so_luong) AS gia_tri_ton_kho
FROM san_pham
GROUP BY danh_muc_id
HAVING SUM(gia * so_luong) > 50000000;

-- WHERE (lọc trước) vs HAVING (lọc sau nhóm)
SELECT danh_muc_id, COUNT(*) AS so_sp
FROM san_pham
WHERE gia > 1000000          -- lọc dòng trước khi nhóm
GROUP BY danh_muc_id
HAVING COUNT(*) > 1;         -- lọc nhóm sau khi GROUP BY
```

---

### Bài 12 — JOIN Bảng

```sql
-- INNER JOIN: chỉ lấy dòng có liên kết ở cả hai bảng
SELECT sp.ten_sp, sp.gia, d.ten AS danh_muc
FROM san_pham sp
INNER JOIN danh_muc d ON sp.danh_muc_id = d.id;

-- LEFT JOIN: tất cả bên trái, NULL nếu không khớp bên phải
SELECT kh.ho_ten, COUNT(dh.id) AS so_don_hang
FROM khach_hang kh
LEFT JOIN don_hang dh ON kh.id = dh.khach_hang_id
GROUP BY kh.id, kh.ho_ten;

-- Tìm khách hàng CHƯA có đơn hàng
SELECT kh.ho_ten
FROM khach_hang kh
LEFT JOIN don_hang dh ON kh.id = dh.khach_hang_id
WHERE dh.id IS NULL;

-- JOIN nhiều bảng
SELECT kh.ho_ten, dh.id AS ma_don, sp.ten_sp, ct.so_luong * ct.don_gia AS thanh_tien
FROM don_hang dh
JOIN khach_hang kh        ON dh.khach_hang_id = kh.id
JOIN chi_tiet_don_hang ct ON ct.don_hang_id   = dh.id
JOIN san_pham sp           ON ct.san_pham_id   = sp.id
WHERE dh.trang_thai = 'hoan_thanh';

-- SELF JOIN: nhân viên - quản lý
SELECT nv.ho_ten AS nhan_vien, ql.ho_ten AS quan_ly
FROM nhan_vien nv
LEFT JOIN nhan_vien ql ON nv.quan_ly_id = ql.id;
```

---

### Bài 13 — Subquery

```sql
-- Subquery trong WHERE
SELECT ten_sp, gia FROM san_pham
WHERE gia > (SELECT AVG(gia) FROM san_pham)
ORDER BY gia DESC;

-- Subquery trong FROM (Derived Table)
SELECT danh_muc, gia_tb
FROM (
    SELECT d.ten AS danh_muc, AVG(sp.gia) AS gia_tb
    FROM san_pham sp JOIN danh_muc d ON sp.danh_muc_id = d.id
    GROUP BY d.id, d.ten
) AS bang_thong_ke
WHERE gia_tb > 5000000;

-- Scalar Subquery trong SELECT
SELECT ten_sp, gia,
    (SELECT AVG(gia) FROM san_pham) AS gia_tb_cua_hang,
    gia - (SELECT AVG(gia) FROM san_pham) AS chenh_lech
FROM san_pham;

-- EXISTS / NOT EXISTS
SELECT ho_ten FROM khach_hang kh
WHERE EXISTS (SELECT 1 FROM don_hang dh WHERE dh.khach_hang_id = kh.id);

SELECT ten_sp FROM san_pham sp
WHERE NOT EXISTS (SELECT 1 FROM chi_tiet_don_hang ct WHERE ct.san_pham_id = sp.id);
```

---

### Bài 14 — Index & Hiệu Suất

```sql
-- Tạo index
CREATE INDEX idx_sp_danh_muc   ON san_pham(danh_muc_id);
CREATE INDEX idx_kh_email      ON khach_hang(email);
CREATE INDEX idx_dh_kh_ngay    ON don_hang(khach_hang_id, ngay_dat);  -- composite
CREATE UNIQUE INDEX idx_kh_email_unique ON khach_hang(email);

SHOW INDEX FROM san_pham;
DROP INDEX idx_sp_danh_muc ON san_pham;

-- EXPLAIN: xem kế hoạch thực thi
EXPLAIN SELECT * FROM san_pham WHERE danh_muc_id = 1;
-- type = const/ref → tốt | type = ALL → full scan, cần xem lại
```

**Khi nào nên / không nên tạo index:**

| ✅ NÊN | ❌ KHÔNG NÊN |
|--------|------------|
| Cột WHERE thường xuyên | Bảng nhỏ < 1000 dòng |
| Cột JOIN (Foreign Key) | Cột ít giá trị phân biệt (is_active) |
| Cột ORDER BY | Cột cập nhật liên tục |

---

### Bài 15 — Transaction

```sql
-- Transaction đảm bảo ACID:
-- Atomicity (nguyên tử) · Consistency (nhất quán) · Isolation (độc lập) · Durability (bền vững)

-- Ví dụ: Đặt hàng (tạo đơn + trừ tồn kho)
START TRANSACTION;

INSERT INTO don_hang (khach_hang_id, tong_tien) VALUES (1, 35000000);
INSERT INTO chi_tiet_don_hang (don_hang_id, san_pham_id, so_luong, don_gia)
VALUES (LAST_INSERT_ID(), 1, 1, 35000000);
UPDATE san_pham SET so_luong = so_luong - 1 WHERE id = 1;

COMMIT;    -- Nếu thành công
ROLLBACK;  -- Nếu có lỗi → hoàn tác toàn bộ

-- SAVEPOINT: điểm lưu trung gian
START TRANSACTION;
INSERT INTO don_hang (khach_hang_id, tong_tien) VALUES (2, 10000000);
SAVEPOINT sau_tao_don;
-- ... thao tác tiếp theo có lỗi ...
ROLLBACK TO SAVEPOINT sau_tao_don;  -- Chỉ rollback về điểm đã lưu
COMMIT;
```

---

## 8. 🔴 Bài Học Cao Cấp

> **Mục tiêu:** Xử lý bài toán phức tạp, tối ưu hệ thống, xây dựng logic trong database.

---

### Bài 16 — View

View là **bảng ảo** tạo ra từ câu lệnh SELECT. Không lưu dữ liệu thực, chỉ lưu định nghĩa truy vấn.

```sql
-- Tạo view
CREATE VIEW v_thong_ke_khach_hang AS
SELECT
    kh.id, kh.ho_ten, kh.email,
    COUNT(dh.id)       AS so_don_hang,
    SUM(dh.tong_tien)  AS tong_chi_tieu,
    MAX(dh.ngay_dat)   AS don_hang_cuoi
FROM khach_hang kh
LEFT JOIN don_hang dh ON kh.id = dh.khach_hang_id
    AND dh.trang_thai = 'hoan_thanh'
GROUP BY kh.id, kh.ho_ten, kh.email;

-- Dùng view như bảng thường
SELECT * FROM v_thong_ke_khach_hang WHERE so_don_hang >= 2;

-- Sửa / Xóa view
CREATE OR REPLACE VIEW v_thong_ke_khach_hang AS SELECT ...;
DROP VIEW IF EXISTS v_thong_ke_khach_hang;

-- View bảo mật: ẩn cột nhạy cảm
CREATE VIEW v_khach_hang_cong_khai AS
SELECT id, ho_ten, ngay_tao FROM khach_hang;
```

**Lợi ích:** đơn giản hóa truy vấn phức tạp · bảo mật cột nhạy cảm · tái sử dụng logic.

---

### Bài 17 — CTE (`WITH` Clause)

CTE là **bảng tạm thời** chỉ tồn tại trong phạm vi một câu lệnh SQL. Dễ đọc hơn Subquery.

```sql
-- CTE cơ bản
WITH gia_tb_theo_danh_muc AS (
    SELECT danh_muc_id, AVG(gia) AS gia_tb
    FROM san_pham GROUP BY danh_muc_id
)
SELECT sp.ten_sp, sp.gia, gtb.gia_tb,
    CASE
        WHEN sp.gia > gtb.gia_tb THEN 'Trên trung bình'
        WHEN sp.gia < gtb.gia_tb THEN 'Dưới trung bình'
        ELSE 'Bằng trung bình'
    END AS xep_loai
FROM san_pham sp
JOIN gia_tb_theo_danh_muc gtb ON sp.danh_muc_id = gtb.danh_muc_id;

-- Nhiều CTE
WITH
don_hang_hoan_thanh AS (SELECT * FROM don_hang WHERE trang_thai = 'hoan_thanh'),
khach_vip AS (
    SELECT khach_hang_id, SUM(tong_tien) AS tong_chi_tieu
    FROM don_hang_hoan_thanh
    GROUP BY khach_hang_id
    HAVING SUM(tong_tien) > 50000000
)
SELECT kh.ho_ten, kv.tong_chi_tieu
FROM khach_hang kh JOIN khach_vip kv ON kh.id = kv.khach_hang_id
ORDER BY kv.tong_chi_tieu DESC;

-- Recursive CTE: duyệt cấu trúc phân cấp (phòng ban, danh mục lồng nhau...)
WITH RECURSIVE cap_bac AS (
    SELECT id, ho_ten, quan_ly_id, 0 AS cap
    FROM nhan_vien WHERE quan_ly_id IS NULL
    UNION ALL
    SELECT nv.id, nv.ho_ten, nv.quan_ly_id, cb.cap + 1
    FROM nhan_vien nv JOIN cap_bac cb ON nv.quan_ly_id = cb.id
)
SELECT REPEAT('  ', cap) || ho_ten AS so_do_to_chuc FROM cap_bac ORDER BY cap;
```

---

### Bài 18 — Window Functions

Window Functions tính toán **trên tập hàng liên quan** mà không gộp chúng lại (khác GROUP BY). Rất mạnh cho phân tích dữ liệu.

```sql
-- Xếp hạng
SELECT ten_sp, danh_muc_id, gia,
    ROW_NUMBER()  OVER (PARTITION BY danh_muc_id ORDER BY gia DESC) AS stt,
    RANK()        OVER (ORDER BY gia DESC) AS hang,          -- bỏ số khi trùng: 1,1,3
    DENSE_RANK()  OVER (ORDER BY gia DESC) AS hang_lien_tuc  -- liên tục: 1,1,2
FROM san_pham;

-- Lấy sản phẩm đắt nhất mỗi danh mục
WITH xep_hang AS (
    SELECT ten_sp, danh_muc_id, gia,
        ROW_NUMBER() OVER (PARTITION BY danh_muc_id ORDER BY gia DESC) AS rn
    FROM san_pham
)
SELECT ten_sp, danh_muc_id, gia FROM xep_hang WHERE rn = 1;

-- LAG / LEAD: so sánh với dòng trước/sau
SELECT DATE_FORMAT(ngay_dat, '%Y-%m') AS thang,
    SUM(tong_tien) AS doanh_thu,
    LAG(SUM(tong_tien), 1) OVER (ORDER BY DATE_FORMAT(ngay_dat, '%Y-%m')) AS thang_truoc
FROM don_hang WHERE trang_thai = 'hoan_thanh'
GROUP BY DATE_FORMAT(ngay_dat, '%Y-%m');

-- Tổng chạy (Running Total)
SELECT ngay_dat, tong_tien,
    SUM(tong_tien) OVER (ORDER BY ngay_dat) AS doanh_thu_luy_ke
FROM don_hang WHERE trang_thai = 'hoan_thanh';

-- NTILE: chia khách hàng thành 4 nhóm theo chi tiêu
SELECT kh.ho_ten, SUM(dh.tong_tien) AS tong_chi_tieu,
    NTILE(4) OVER (ORDER BY SUM(dh.tong_tien) DESC) AS nhom
FROM khach_hang kh JOIN don_hang dh ON kh.id = dh.khach_hang_id
GROUP BY kh.id, kh.ho_ten;
```

---

### Bài 19 — Stored Procedure & Function

```sql
-- ===== STORED PROCEDURE =====
DELIMITER $$

CREATE PROCEDURE sp_dat_hang(
    IN  p_khach_hang_id INT,
    IN  p_san_pham_id   INT,
    IN  p_so_luong      INT,
    OUT p_ket_qua       VARCHAR(100)
)
BEGIN
    DECLARE v_gia     DECIMAL(15,2);
    DECLARE v_ton_kho INT;
    DECLARE v_don_id  INT;

    SELECT gia, so_luong INTO v_gia, v_ton_kho
    FROM san_pham WHERE id = p_san_pham_id;

    IF v_ton_kho < p_so_luong THEN
        SET p_ket_qua = 'Lỗi: Không đủ hàng tồn kho';
    ELSE
        START TRANSACTION;
        INSERT INTO don_hang (khach_hang_id, tong_tien) VALUES (p_khach_hang_id, v_gia * p_so_luong);
        SET v_don_id = LAST_INSERT_ID();
        INSERT INTO chi_tiet_don_hang (don_hang_id, san_pham_id, so_luong, don_gia)
        VALUES (v_don_id, p_san_pham_id, p_so_luong, v_gia);
        UPDATE san_pham SET so_luong = so_luong - p_so_luong WHERE id = p_san_pham_id;
        COMMIT;
        SET p_ket_qua = CONCAT('Đặt hàng thành công! Mã đơn: ', v_don_id);
    END IF;
END$$
DELIMITER ;

CALL sp_dat_hang(1, 3, 1, @ket_qua);
SELECT @ket_qua;


-- ===== FUNCTION =====
DELIMITER $$

CREATE FUNCTION fn_phan_loai_khach(p_tong DECIMAL(15,2))
RETURNS VARCHAR(20) DETERMINISTIC
BEGIN
    DECLARE v_loai VARCHAR(20);
    IF    p_tong >= 100000000 THEN SET v_loai = 'Kim Cương';
    ELSEIF p_tong >= 50000000 THEN SET v_loai = 'Vàng';
    ELSEIF p_tong >= 20000000 THEN SET v_loai = 'Bạc';
    ELSE                           SET v_loai = 'Đồng';
    END IF;
    RETURN v_loai;
END$$
DELIMITER ;

-- Dùng trong SELECT
SELECT kh.ho_ten, SUM(dh.tong_tien) AS tong,
    fn_phan_loai_khach(SUM(dh.tong_tien)) AS hang_khach_hang
FROM khach_hang kh JOIN don_hang dh ON kh.id = dh.khach_hang_id
WHERE dh.trang_thai = 'hoan_thanh'
GROUP BY kh.id, kh.ho_ten;
```

---

### Bài 20 — Trigger

Trigger là code SQL **tự động chạy** khi có sự kiện INSERT / UPDATE / DELETE xảy ra trên bảng.

```sql
-- Tự động cập nhật tổng tiền đơn hàng sau khi thêm chi tiết
DELIMITER $$
CREATE TRIGGER trg_cap_nhat_tong_tien
AFTER INSERT ON chi_tiet_don_hang FOR EACH ROW
BEGIN
    UPDATE don_hang
    SET tong_tien = (SELECT SUM(so_luong * don_gia) FROM chi_tiet_don_hang WHERE don_hang_id = NEW.don_hang_id)
    WHERE id = NEW.don_hang_id;
END$$
DELIMITER ;

-- Ghi log khi giá sản phẩm thay đổi
DELIMITER $$
CREATE TRIGGER trg_log_gia
BEFORE UPDATE ON san_pham FOR EACH ROW
BEGIN
    IF OLD.gia != NEW.gia THEN
        INSERT INTO log_gia_san_pham (san_pham_id, gia_cu, gia_moi)
        VALUES (OLD.id, OLD.gia, NEW.gia);
    END IF;
END$$
DELIMITER ;

-- Kiểm tra tồn kho trước khi đặt hàng
DELIMITER $$
CREATE TRIGGER trg_kiem_tra_ton_kho
BEFORE INSERT ON chi_tiet_don_hang FOR EACH ROW
BEGIN
    DECLARE v_ton_kho INT;
    SELECT so_luong INTO v_ton_kho FROM san_pham WHERE id = NEW.san_pham_id;
    IF v_ton_kho < NEW.so_luong THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Lỗi: Số lượng yêu cầu vượt quá tồn kho!';
    END IF;
END$$
DELIMITER ;

SHOW TRIGGERS FROM cua_hang;
DROP TRIGGER IF EXISTS trg_log_gia;
```

---

### Bài 21 — Tối Ưu Hóa Query

```sql
-- EXPLAIN ANALYZE (MySQL 8.0+)
EXPLAIN ANALYZE
SELECT sp.ten_sp, d.ten FROM san_pham sp
JOIN danh_muc d ON sp.danh_muc_id = d.id
WHERE sp.gia > 10000000;
-- rows ít + type = ref/const = tốt | type = ALL = full scan = cần index

-- ❌ Hàm bao ngoài cột trong WHERE → phá index
SELECT * FROM don_hang WHERE YEAR(ngay_dat) = 2026;

-- ✅ Viết lại để dùng index
SELECT * FROM don_hang WHERE ngay_dat >= '2026-01-01' AND ngay_dat < '2027-01-01';

-- ❌ LIKE bắt đầu bằng % → full scan
SELECT * FROM san_pham WHERE ten_sp LIKE '%Dell%';

-- ✅ Dùng FULLTEXT INDEX cho tìm kiếm full-text
ALTER TABLE san_pham ADD FULLTEXT INDEX ft_ten_sp (ten_sp);
SELECT * FROM san_pham WHERE MATCH(ten_sp) AGAINST('Dell' IN BOOLEAN MODE);

-- ✅ Chỉ SELECT các cột cần thiết, tránh SELECT * trong production
SELECT id, khach_hang_id, tong_tien, trang_thai FROM don_hang;

-- Xem query đang chạy
SHOW PROCESSLIST;
KILL QUERY [process_id];
```

---

### Bài 22 — Thiết Kế Schema & Chuẩn Hóa

```
Chuẩn hóa (Normalization) là quá trình tổ chức dữ liệu để:
- Giảm trùng lặp
- Đảm bảo tính nhất quán
- Dễ bảo trì
```

#### Các Dạng Chuẩn (Normal Forms)

**1NF — Mỗi ô chứa một giá trị nguyên tử**
```sql
-- ❌ Vi phạm 1NF: Nhiều giá trị trong một ô
CREATE TABLE don_hang_sai (
    id          INT,
    san_pham    VARCHAR(500)  -- 'Laptop, Chuột, Bàn phím' ← SAI
);

-- ✅ Đúng 1NF: Tách ra bảng chi tiết
CREATE TABLE chi_tiet_don_hang (
    don_hang_id INT,
    san_pham_id INT,
    so_luong    INT
);
```

**2NF — 1NF + Mọi cột phụ thuộc HOÀN TOÀN vào khóa chính**
```sql
-- ❌ Vi phạm 2NF: ten_san_pham chỉ phụ thuộc vào san_pham_id, không phụ thuộc don_hang_id
CREATE TABLE chi_tiet_sai (
    don_hang_id     INT,
    san_pham_id     INT,
    ten_san_pham    VARCHAR(200),  -- ← phụ thuộc một phần
    so_luong        INT,
    don_gia         DECIMAL(15,2),
    PRIMARY KEY (don_hang_id, san_pham_id)
);

-- ✅ Đúng 2NF: Tên sản phẩm thuộc bảng san_pham
CREATE TABLE chi_tiet_don_hang (
    don_hang_id INT, san_pham_id INT,
    so_luong INT, don_gia DECIMAL(15,2),
    PRIMARY KEY (don_hang_id, san_pham_id)
);
-- ten_san_pham giữ ở bảng san_pham, JOIN khi cần
```

**3NF — 2NF + Không có phụ thuộc bắc cầu**
```sql
-- ❌ Vi phạm 3NF: ten_tinh phụ thuộc vào ma_tinh, không phụ thuộc trực tiếp vào khach_hang_id
CREATE TABLE khach_hang_sai (
    id          INT PRIMARY KEY,
    ho_ten      VARCHAR(100),
    ma_tinh     CHAR(2),
    ten_tinh    VARCHAR(100)   -- ← phụ thuộc bắc cầu qua ma_tinh
);

-- ✅ Đúng 3NF: Tách bảng tinh_thanh_pho
CREATE TABLE tinh_thanh (ma CHAR(2) PRIMARY KEY, ten VARCHAR(100));
CREATE TABLE khach_hang (id INT PRIMARY KEY, ho_ten VARCHAR(100), ma_tinh CHAR(2),
    FOREIGN KEY (ma_tinh) REFERENCES tinh_thanh(ma));
```

#### Khi Nào Nên Denormalize?

```
Chuẩn hóa cao → Ít trùng lặp, nhất quán, nhưng JOIN nhiều → chậm khi đọc
Denormalize   → Trùng lặp có kiểm soát, đọc nhanh hơn, khó maintain

Nên Denormalize khi:
✅ Read >> Write (báo cáo, analytics, data warehouse)
✅ Query chạy quá chậm dù đã có index
✅ Dữ liệu lịch sử cần lưu trạng thái tại thời điểm (VD: giá lúc mua)

Ví dụ hợp lý:
chi_tiet_don_hang có cột don_gia (giá lúc mua) riêng biệt
→ Dù trùng với san_pham.gia, nhưng cần thiết vì giá có thể thay đổi sau này
```
---

## 9. SQL Trong Công Việc

### 👨‍💼 Vai Trò Nào Cần SQL?

| Vai trò | Mức độ cần | Ghi chú | Loại SQL chủ yếu |
|---------|-----------|---------|-----------------|
| **Data Analyst** | ⭐⭐⭐⭐⭐ | Bắt buộc | SELECT phức tạp, GROUP BY, JOIN, Window Functions |
| **Data Engineer** | ⭐⭐⭐⭐⭐ | Bắt buộc | ETL, DDL, Stored Procedure, Query Optimization |
| **Backend Developer** | ⭐⭐⭐⭐ | Cần thiết | CRUD, JOIN, Transaction, Index |
| **Business Analyst** | ⭐⭐⭐⭐ | Cần thiết | SELECT, GROUP BY, báo cáo |
| **DBA** | ⭐⭐⭐⭐⭐ | Chuyên sâu | Toàn bộ + Replication, Backup |
| **QA / Tester** | ⭐⭐⭐ | Hữu ích | SELECT, kiểm tra dữ liệu |
| **DevOps** | ⭐⭐ | Hữu ích | Query cơ bản, monitoring |

### 📋 Ví Dụ Công Việc Thực Tế

**Data Analyst — Báo cáo doanh thu theo tháng:**
```sql
SELECT
    DATE_FORMAT(ngay_dat, '%Y-%m') AS thang,
    COUNT(*)                       AS so_don,
    SUM(tong_tien)                 AS doanh_thu,
    SUM(tong_tien) - LAG(SUM(tong_tien), 1)
        OVER (ORDER BY DATE_FORMAT(ngay_dat, '%Y-%m')) AS tang_truong
FROM don_hang
WHERE trang_thai = 'hoan_thanh'
GROUP BY DATE_FORMAT(ngay_dat, '%Y-%m')
ORDER BY thang;
```

**Backend Developer — API tìm kiếm sản phẩm có phân trang:**
```sql
SELECT sp.id, sp.ten_sp, sp.gia, d.ten AS danh_muc
FROM san_pham sp JOIN danh_muc d ON sp.danh_muc_id = d.id
WHERE sp.so_luong > 0
  AND (sp.ten_sp LIKE CONCAT('%', ?, '%') OR d.ten = ?)
ORDER BY sp.gia ASC
LIMIT ? OFFSET ?;
```

**Data Engineer — ETL đổ dữ liệu vào bảng tổng hợp:**
```sql
INSERT INTO bao_cao_doanh_thu_ngay (ngay, so_don, doanh_thu, cap_nhat_luc)
SELECT DATE(ngay_dat), COUNT(*), SUM(tong_tien), NOW()
FROM don_hang
WHERE trang_thai = 'hoan_thanh' AND DATE(ngay_dat) = CURDATE() - INTERVAL 1 DAY
GROUP BY DATE(ngay_dat)
ON DUPLICATE KEY UPDATE
    so_don       = VALUES(so_don),
    doanh_thu    = VALUES(doanh_thu),
    cap_nhat_luc = VALUES(cap_nhat_luc);
```

---

## 10. Các Hệ Quản Trị Phổ Biến

| Tên | Loại | Phù hợp | Điểm nổi bật |
|-----|------|---------|--------------|
| **MySQL** | Mã nguồn mở | Web app, startup | Phổ biến nhất, cộng đồng lớn |
| **PostgreSQL** | Mã nguồn mở | Ứng dụng phức tạp | Mạnh nhất về tính năng, JSON tốt |
| **SQLite** | Nhúng (embedded) | Mobile, desktop, testing | Không cần server, 1 file duy nhất |
| **SQL Server** | Microsoft | Doanh nghiệp Windows | Tích hợp tốt hệ sinh thái Microsoft |
| **Oracle** | Thương mại | Ngân hàng, tập đoàn | Cực mạnh, cực đắt |
| **MariaDB** | Mã nguồn mở | Thay thế MySQL | Fork của MySQL, một số cải tiến |
| **BigQuery** | Cloud (Google) | Big Data, Analytics | Xử lý petabyte, pay-per-query |
| **Redshift** | Cloud (AWS) | Data Warehouse | Tối ưu phân tích quy mô lớn |
| **Snowflake** | Cloud (Multi) | Data Cloud | Tách compute & storage, linh hoạt |

> 💡 **Khuyến nghị khi bắt đầu:** Học **PostgreSQL** hoặc **MySQL**. Kiến thức SQL cốt lõi áp dụng được cho tất cả.

---

## 11. Lỗi Thường Gặp & Cách Xử Lý

### ❌ Lỗi Cú Pháp

```sql
WHERE ho_ten = Nguyen;          -- ❌ Thiếu nháy đơn
WHERE ho_ten = 'Nguyen';        -- ✅ Đúng

-- ❌ Sai thứ tự mệnh đề
SELECT * FROM san_pham HAVING gia > 1000 WHERE danh_muc_id = 1;

-- ✅ Đúng: WHERE → GROUP BY → HAVING → ORDER BY
SELECT * FROM san_pham WHERE danh_muc_id = 1 HAVING gia > 1000;

-- ❌ GROUP BY thiếu cột không tổng hợp
SELECT danh_muc_id, ten_sp, COUNT(*) FROM san_pham GROUP BY danh_muc_id;

-- ✅ Đúng
SELECT danh_muc_id, COUNT(*) FROM san_pham GROUP BY danh_muc_id;
```

### ⚠️ Lỗi Logic Nguy Hiểm

```sql
WHERE email = NULL;     -- ❌ Không bao giờ có kết quả
WHERE email IS NULL;    -- ✅ Đúng

UPDATE san_pham SET gia = 0;        -- ❌ Không có WHERE → cập nhật toàn bộ bảng!
DELETE FROM khach_hang;             -- ❌ Không có WHERE → xóa toàn bộ!
```

### 🔐 SQL Injection

```sql
-- ❌ KHÔNG ghép chuỗi trực tiếp từ input người dùng:
-- "SELECT * FROM users WHERE username = '" + input + "'"
-- Nếu input là: ' OR '1'='1  → trả về toàn bộ dữ liệu!

-- ✅ Luôn dùng Parameterized Query:
-- Python:  cursor.execute("SELECT * FROM users WHERE username = %s", (input,))
-- PHP:     $stmt->prepare("SELECT * FROM users WHERE username = ?")
-- Node.js: db.query("SELECT * FROM users WHERE username = ?", [input])
```

---

## 12. Tổng Kết & Lộ Trình

### 🗺️ Lộ Trình Học SQL

```
🟢 CƠ BẢN (2–4 tuần)
├── Kiểu dữ liệu, CREATE / DROP TABLE
├── INSERT, SELECT, UPDATE, DELETE
├── WHERE, ORDER BY, LIMIT
└── Các hàm chuỗi & ngày cơ bản

🟡 TRUNG CẤP (1–2 tháng)
├── Hàm tổng hợp: COUNT, SUM, AVG, MIN, MAX
├── GROUP BY, HAVING
├── JOIN: INNER, LEFT, RIGHT, SELF
├── Subquery, EXISTS
├── INDEX cơ bản
└── Transaction, ACID

🔴 NÂNG CAO (2–4 tháng)
├── View
├── CTE (WITH clause), Recursive CTE
├── Window Functions: ROW_NUMBER, RANK, LAG, LEAD, SUM OVER...
├── Stored Procedure, Function
├── Trigger
├── Query Optimization, EXPLAIN ANALYZE
└── Thiết kế Schema, Normalization

🚀 CHUYÊN GIA (liên tục)
├── Database Design cho hệ thống lớn
├── Partitioning & Sharding
├── Replication & High Availability
├── Cloud Databases (BigQuery, Redshift, Snowflake)
└── Data Modeling (Star Schema, Snowflake Schema)
```

### ✅ Checklist Kỹ Năng SQL

**🟢 Cơ bản:**
- [ ] Tạo bảng với đúng kiểu dữ liệu và ràng buộc
- [ ] Thành thạo SELECT với WHERE, ORDER BY, LIMIT
- [ ] INSERT, UPDATE, DELETE an toàn (luôn có WHERE)
- [ ] Hiểu các hàm chuỗi và ngày tháng thường dùng

**🟡 Trung cấp:**
- [ ] Sử dụng thành thạo tất cả loại JOIN
- [ ] GROUP BY + HAVING + hàm tổng hợp
- [ ] Viết được Subquery phức tạp
- [ ] Biết tạo và quản lý Index
- [ ] Hiểu Transaction và ACID

**🔴 Nâng cao:**
- [ ] Tạo và sử dụng View
- [ ] Viết CTE (bao gồm Recursive CTE)
- [ ] Sử dụng Window Functions (ROW_NUMBER, LAG, LEAD, SUM OVER...)
- [ ] Viết Stored Procedure và Function
- [ ] Đọc hiểu EXPLAIN và tối ưu query
- [ ] Thiết kế schema chuẩn hóa 3NF cho bài toán thực tế

### 💼 SQL Quan Trọng Vì

1. **Phổ biến tuyệt đối** — Hầu hết hệ thống đều dùng database quan hệ
2. **Lương cao hơn** — SQL là kỹ năng được yêu cầu trong hầu hết JD ngành Tech & Data
3. **Chuyển dịch linh hoạt** — Biết MySQL → dễ học PostgreSQL, SQL Server, BigQuery
4. **Không bao giờ lỗi thời** — SQL 50+ năm và vẫn đang phát triển
5. **Tư duy phân tích** — SQL rèn luyện cách suy nghĩ theo tập hợp và logic

---

## 13. Tài Nguyên Học Thêm

### 🛠️ Cài Đặt & Khởi Động Nhanh

**Cài đặt hệ quản trị:**

| Hệ quản trị | Tải về | Ghi chú |
|-------------|--------|---------|
| **MySQL** | [dev.mysql.com/downloads](https://dev.mysql.com/downloads/) | Chọn MySQL Community Server |
| **PostgreSQL** | [postgresql.org/download](https://www.postgresql.org/download/) | Kèm pgAdmin |
| **SQLite** | Không cần cài | Tích hợp sẵn trong Python |

**Dùng SQL trong VS Code:**

1. Cài extension **SQLTools** (Matheus Teixeira) từ Marketplace
2. Cài thêm driver tương ứng: `SQLTools MySQL/MariaDB` hoặc `SQLTools PostgreSQL`
3. Tạo connection → viết file `.sql` → chạy trực tiếp trong editor

**Tạo file SQL trong VS Code:**
- Tạo file mới → đặt tên `ten_file.sql` → VS Code tự nhận diện syntax highlight
- Có thể dùng Ctrl+Shift+E (SQLTools) để chạy câu lệnh ngay trong editor

**Dùng Docker (không cần cài):**
```bash
# Chạy MySQL qua Docker
docker run --name mysql-demo -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql:8

# Chạy PostgreSQL qua Docker
docker run --name pg-demo -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres:16
```

---

### 🌐 Thực Hành Online (Miễn Phí)

| Nền tảng | Link | Nội dung |
|----------|------|---------|
| **SQLZoo** | [sqlzoo.net](https://sqlzoo.net) | Bài tập tương tác theo cấp độ |
| **LeetCode** | [leetcode.com/problemset/database](https://leetcode.com/problemset/database/) | SQL phỏng vấn kỹ thuật |
| **HackerRank** | [hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql) | Bài tập có chứng chỉ |
| **Mode Analytics** | [mode.com/sql-tutorial](https://mode.com/sql-tutorial/) | SQL cho Data Analysis |
| **pgexercises** | [pgexercises.com](https://pgexercises.com) | Bài tập PostgreSQL chuyên sâu |
| **W3Schools SQL** | [w3schools.com/sql](https://www.w3schools.com/sql/) | Tài liệu + thực hành nhanh |

### 📚 Tài Liệu Chính Thức

- **PostgreSQL Docs** — [postgresql.org/docs](https://www.postgresql.org/docs/) — Đầy đủ và chi tiết nhất
- **MySQL Reference** — [dev.mysql.com/doc](https://dev.mysql.com/doc/)
- **Use The Index, Luke** — [use-the-index-luke.com](https://use-the-index-luke.com/) — Tối ưu Index, miễn phí

### 🖥️ Công Cụ Làm Việc

| Công cụ | Dùng cho | Ghi chú |
|---------|---------|---------|
| **DBeaver** | Tất cả DB | Miễn phí, hỗ trợ nhiều DB nhất |
| **TablePlus** | Mac/Win/Linux | Giao diện đẹp, nhẹ, nhanh |
| **DataGrip** | Chuyên nghiệp | Trả phí, JetBrains, mạnh nhất |
| **pgAdmin** | PostgreSQL | Miễn phí, chính thức |
| **MySQL Workbench** | MySQL | Miễn phí, chính thức |
| **VS Code + SQLTools** | Mọi loại | Nhẹ, tích hợp tốt vào workflow |

---

<div align="center">

**📖 Tài liệu SQL — Từ Cơ Bản Đến Nâng Cao**  

***© 2026 | HI White — Tài liệu học tập, chỉ dùng cho mục đích tham khảo của cá nhân.***  

***Học chắc nền tảng · Thực hành đều đặn · Áp dụng vào dự án thực tế***

</div>
