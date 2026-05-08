# 🗄️ SQL — Ngôn Ngữ Truy Vấn Cấu Trúc

> **Structured Query Language** — Nền tảng của mọi hệ thống dữ liệu hiện đại

---

## 📌 Mục Lục

1. [Giới Thiệu](#1-giới-thiệu)
2. [Lịch Sử Hình Thành](#2-lịch-sử-hình-thành)
3. [SQL Hoạt Động Như Thế Nào?](#3-sql-hoạt-động-như-thế-nào)
4. [Các Thao Tác Cơ Bản (CRUD)](#4-các-thao-tác-cơ-bản-crud)
5. [Bài Học SQL Từng Bước](#5-bài-học-sql-từng-bước)
   - [Bài 1 — Tạo Bảng](#bài-1--tạo-bảng-create-table)
   - [Bài 2 — Chèn Dữ Liệu](#bài-2--chèn-dữ-liệu-insert)
   - [Bài 3 — Truy Vấn Dữ Liệu](#bài-3--truy-vấn-dữ-liệu-select)
   - [Bài 4 — Lọc & Sắp Xếp](#bài-4--lọc--sắp-xếp)
   - [Bài 5 — Cập Nhật & Xóa](#bài-5--cập-nhật--xóa)
   - [Bài 6 — JOIN Bảng](#bài-6--join-bảng)
   - [Bài 7 — Hàm Tổng Hợp](#bài-7--hàm-tổng-hợp)
   - [Bài 8 — Subquery](#bài-8--subquery)
   - [Bài 9 — Index & Hiệu Suất](#bài-9--index--hiệu-suất)
   - [Bài 10 — Transaction](#bài-10--transaction)
6. [SQL Trong Công Việc](#6-sql-trong-công-việc)
7. [Các Hệ Quản Trị Phổ Biến](#7-các-hệ-quản-trị-phổ-biến)
8. [Lỗi Thường Gặp & Cách Xử Lý](#8-lỗi-thường-gặp--cách-xử-lý)
9. [Tổng Kết](#9-tổng-kết)
10. [Tài Nguyên Học Thêm](#10-tài-nguyên-học-thêm)

---

## 1. Giới Thiệu

**SQL** (viết tắt của *Structured Query Language*) là ngôn ngữ lập trình đặc biệt dùng để **tương tác với cơ sở dữ liệu quan hệ** (Relational Database). SQL cho phép người dùng:

- 📥 **Truy vấn** dữ liệu từ cơ sở dữ liệu
- ✏️ **Thêm, sửa, xóa** bản ghi
- 🏗️ **Tạo và quản lý** cấu trúc bảng
- 🔒 **Phân quyền** truy cập dữ liệu

SQL không phải ngôn ngữ lập trình thuần túy (như Python hay Java), mà là ngôn ngữ **khai báo** — bạn nói *"cần gì"* thay vì *"làm như thế nào"*.

```sql
-- Ví dụ đơn giản: Lấy danh sách nhân viên có lương > 10 triệu
SELECT ten, luong
FROM nhan_vien
WHERE luong > 10000000
ORDER BY luong DESC;
```

---

## 2. Lịch Sử Hình Thành

```
1970        1974        1979        1986        1992        2003        Hiện tại
 │           │           │           │           │           │           │
 ▼           ▼           ▼           ▼           ▼           ▼           ▼
[Codd]    [SEQUEL]   [Oracle]   [SQL-86]   [SQL-92]   [SQL-2003]  [NoSQL +
Đặt nền   IBM tạo    phát hành  ISO/ANSI   chuẩn hóa   XML, OOP    SQL song
tảng lý   ngôn ngữ   RDBMS      chuẩn hóa  mở rộng    tích hợp    song tồn]
thuyết    đầu tiên   thương mại  đầu tiên
```

| Năm | Sự Kiện |
|-----|---------|
| **1970** | Edgar F. Codd (IBM) công bố mô hình cơ sở dữ liệu quan hệ trong bài báo *"A Relational Model of Data"* |
| **1974** | Donald Chamberlin và Raymond Boyce (IBM) phát triển **SEQUEL** (tiền thân của SQL) |
| **1979** | Oracle Corporation phát hành **hệ quản trị cơ sở dữ liệu thương mại đầu tiên** sử dụng SQL |
| **1986** | **ISO và ANSI** chuẩn hóa SQL lần đầu tiên (SQL-86) |
| **1992** | **SQL-92** ra đời — phiên bản được dùng phổ biến nhất, là nền tảng cho hầu hết RDBMS ngày nay |
| **1999** | SQL:1999 bổ sung tính năng hướng đối tượng, trigger, stored procedure |
| **2003** | SQL:2003 tích hợp XML, thêm window functions |
| **2011** | SQL:2011 hỗ trợ dữ liệu theo thời gian (temporal data) |
| **Nay** | SQL vẫn là kỹ năng **không thể thiếu** trong ngành Data, Backend, DevOps |

> 💡 **Thú vị:** SQL đã hơn 50 tuổi nhưng vẫn là một trong những ngôn ngữ được dùng nhiều nhất thế giới. Theo Stack Overflow Developer Survey 2024, SQL liên tục nằm trong top 3 ngôn ngữ/công nghệ phổ biến nhất.

---

## 3. SQL Hoạt Động Như Thế Nào?

### Kiến Trúc Tổng Quan

```
Người dùng / Ứng dụng
        │
        │  Câu lệnh SQL
        ▼
┌─────────────────────┐
│   SQL Engine        │  ← Phân tích cú pháp (Parser)
│   (Query Processor) │  ← Tối ưu hóa truy vấn (Optimizer)
│                     │  ← Thực thi (Executor)
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Storage Engine     │  ← Đọc/ghi dữ liệu thực tế
│  (Disk / Memory)    │
└─────────────────────┘
        │
        ▼
   Kết quả trả về
```

### Các Nhóm Lệnh SQL

| Nhóm | Tên đầy đủ | Lệnh chính | Mục đích |
|------|-----------|------------|----------|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP` | Định nghĩa cấu trúc |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Thao tác dữ liệu |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Phân quyền |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Quản lý giao dịch |

---

## 4. Các Thao Tác Cơ Bản (CRUD)

**CRUD** = Create · Read · Update · Delete — bốn thao tác nền tảng của mọi ứng dụng dữ liệu.

| Thao tác | SQL | Ý nghĩa |
|----------|-----|---------|
| **C**reate | `INSERT INTO` | Thêm dữ liệu mới |
| **R**ead | `SELECT` | Đọc / truy vấn dữ liệu |
| **U**pdate | `UPDATE` | Cập nhật dữ liệu |
| **D**elete | `DELETE` | Xóa dữ liệu |

---

## 5. Bài Học SQL Từng Bước

> 📂 Chúng ta sẽ xây dựng một hệ thống quản lý **cửa hàng bán lẻ** xuyên suốt các bài học.

---

### Bài 1 — Tạo Bảng (`CREATE TABLE`)

```sql
-- Tạo bảng khách hàng
CREATE TABLE khach_hang (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    ho_ten      VARCHAR(100)    NOT NULL,
    email       VARCHAR(150)    UNIQUE,
    so_dien_thoai VARCHAR(15),
    ngay_tao    DATETIME        DEFAULT CURRENT_TIMESTAMP
);

-- Tạo bảng sản phẩm
CREATE TABLE san_pham (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    ten_sp      VARCHAR(200)    NOT NULL,
    gia         DECIMAL(15, 2)  NOT NULL,
    so_luong    INT             DEFAULT 0,
    danh_muc    VARCHAR(100)
);

-- Tạo bảng đơn hàng
CREATE TABLE don_hang (
    id              INT PRIMARY KEY AUTO_INCREMENT,
    khach_hang_id   INT NOT NULL,
    tong_tien       DECIMAL(15, 2),
    trang_thai      ENUM('cho_xu_ly', 'dang_giao', 'hoan_thanh', 'huy') DEFAULT 'cho_xu_ly',
    ngay_dat        DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(id)
);
```

**Giải thích:**
- `PRIMARY KEY` — khóa chính, định danh duy nhất mỗi bản ghi
- `AUTO_INCREMENT` — tự động tăng số thứ tự
- `NOT NULL` — bắt buộc phải có giá trị
- `UNIQUE` — không được trùng lặp
- `DEFAULT` — giá trị mặc định nếu không nhập
- `FOREIGN KEY` — liên kết với bảng khác (khóa ngoại)

---

### Bài 2 — Chèn Dữ Liệu (`INSERT`)

```sql
-- Thêm một khách hàng
INSERT INTO khach_hang (ho_ten, email, so_dien_thoai)
VALUES ('Nguyễn Văn An', 'an.nguyen@email.com', '0901234567');

-- Thêm nhiều khách hàng cùng lúc
INSERT INTO khach_hang (ho_ten, email, so_dien_thoai)
VALUES
    ('Trần Thị Bình', 'binh.tran@email.com', '0912345678'),
    ('Lê Văn Cường',  'cuong.le@email.com',  '0923456789'),
    ('Phạm Thị Dung', 'dung.pham@email.com',  NULL);

-- Thêm sản phẩm
INSERT INTO san_pham (ten_sp, gia, so_luong, danh_muc)
VALUES
    ('Laptop Dell XPS 15',  35000000, 20, 'Máy tính'),
    ('Chuột Logitech MX3',   1500000, 50, 'Phụ kiện'),
    ('Bàn phím Keychron K2', 2800000, 35, 'Phụ kiện'),
    ('iPhone 16 Pro',        30000000, 15, 'Điện thoại');
```

---

### Bài 3 — Truy Vấn Dữ Liệu (`SELECT`)

```sql
-- Lấy tất cả cột, tất cả bản ghi
SELECT * FROM khach_hang;

-- Lấy các cột cụ thể
SELECT ho_ten, email FROM khach_hang;

-- Đặt alias (tên hiển thị) cho cột
SELECT
    ho_ten      AS 'Họ Tên',
    email       AS 'Email',
    ngay_tao    AS 'Ngày Đăng Ký'
FROM khach_hang;

-- Lấy giá trị không trùng (DISTINCT)
SELECT DISTINCT danh_muc FROM san_pham;

-- Giới hạn số bản ghi trả về
SELECT * FROM san_pham LIMIT 2;

-- Bỏ qua N bản ghi đầu, lấy M bản ghi tiếp theo (phân trang)
SELECT * FROM san_pham LIMIT 2 OFFSET 2;
```

**Cú pháp SELECT đầy đủ:**
```sql
SELECT   [cột hoặc biểu thức]
FROM     [bảng]
WHERE    [điều kiện lọc]
GROUP BY [nhóm theo]
HAVING   [điều kiện sau nhóm]
ORDER BY [sắp xếp]
LIMIT    [giới hạn số dòng];
```

---

### Bài 4 — Lọc & Sắp Xếp

```sql
-- WHERE cơ bản
SELECT * FROM san_pham WHERE gia > 5000000;

-- Nhiều điều kiện với AND / OR
SELECT * FROM san_pham
WHERE danh_muc = 'Phụ kiện' AND gia < 3000000;

-- BETWEEN (khoảng giá trị)
SELECT * FROM san_pham
WHERE gia BETWEEN 1000000 AND 5000000;

-- IN (danh sách giá trị)
SELECT * FROM san_pham
WHERE danh_muc IN ('Máy tính', 'Điện thoại');

-- LIKE (tìm kiếm chuỗi)
SELECT * FROM khach_hang WHERE ho_ten LIKE 'Nguyễn%';  -- bắt đầu bằng "Nguyễn"
SELECT * FROM khach_hang WHERE email LIKE '%@gmail.com'; -- kết thúc bằng "@gmail.com"
SELECT * FROM san_pham  WHERE ten_sp LIKE '%Dell%';     -- chứa từ "Dell"

-- IS NULL / IS NOT NULL
SELECT * FROM khach_hang WHERE so_dien_thoai IS NULL;

-- ORDER BY (sắp xếp)
SELECT * FROM san_pham ORDER BY gia ASC;    -- tăng dần
SELECT * FROM san_pham ORDER BY gia DESC;   -- giảm dần
SELECT * FROM san_pham ORDER BY danh_muc ASC, gia DESC; -- sắp xếp nhiều cột
```

---

### Bài 5 — Cập Nhật & Xóa

```sql
-- UPDATE: cập nhật dữ liệu
UPDATE san_pham
SET gia = 32000000
WHERE id = 1;

-- Cập nhật nhiều cột cùng lúc
UPDATE san_pham
SET gia = gia * 0.9,    -- giảm 10%
    so_luong = so_luong + 5
WHERE danh_muc = 'Phụ kiện';

-- DELETE: xóa bản ghi
DELETE FROM san_pham WHERE id = 4;

-- ⚠️ CẢNH BÁO: Không có WHERE → xóa TOÀN BỘ dữ liệu!
-- DELETE FROM san_pham;  -- NGUY HIỂM!

-- TRUNCATE: xóa toàn bộ và reset auto_increment (nhanh hơn DELETE)
-- TRUNCATE TABLE san_pham;
```

> ⚠️ **Nguyên tắc vàng:** Luôn kiểm tra bằng `SELECT` trước khi chạy `UPDATE` hoặc `DELETE`. Chạy thử điều kiện WHERE trước để xác nhận đúng bản ghi.

---

### Bài 6 — JOIN Bảng

JOIN dùng để **kết hợp dữ liệu từ nhiều bảng** dựa trên cột liên kết.

```
Bảng A          Bảng B
┌──────┐       ┌──────┐
│  1   │       │  1   │
│  2   │       │  2   │
│  3   │       │  4   │
└──────┘       └──────┘

INNER JOIN → {1, 2}         (chỉ phần giao)
LEFT JOIN  → {1, 2, 3}      (tất cả A + phần khớp B)
RIGHT JOIN → {1, 2, 4}      (phần khớp A + tất cả B)
FULL JOIN  → {1, 2, 3, 4}   (tất cả cả hai)
```

```sql
-- INNER JOIN: Lấy đơn hàng kèm thông tin khách hàng
SELECT
    dh.id           AS 'Mã Đơn',
    kh.ho_ten       AS 'Khách Hàng',
    kh.email        AS 'Email',
    dh.tong_tien    AS 'Tổng Tiền',
    dh.trang_thai   AS 'Trạng Thái'
FROM don_hang dh
INNER JOIN khach_hang kh ON dh.khach_hang_id = kh.id;

-- LEFT JOIN: Lấy TẤT CẢ khách hàng, kể cả chưa có đơn hàng
SELECT
    kh.ho_ten,
    COUNT(dh.id) AS so_don_hang
FROM khach_hang kh
LEFT JOIN don_hang dh ON kh.id = dh.khach_hang_id
GROUP BY kh.id, kh.ho_ten;

-- JOIN nhiều bảng
SELECT
    kh.ho_ten,
    sp.ten_sp,
    ct.so_luong,
    ct.don_gia
FROM don_hang dh
JOIN khach_hang kh  ON dh.khach_hang_id = kh.id
JOIN chi_tiet_dh ct ON ct.don_hang_id   = dh.id
JOIN san_pham sp    ON ct.san_pham_id   = sp.id;
```

---

### Bài 7 — Hàm Tổng Hợp

```sql
-- COUNT: đếm số bản ghi
SELECT COUNT(*) AS tong_khach FROM khach_hang;
SELECT COUNT(email) AS co_email FROM khach_hang;  -- không đếm NULL

-- SUM: tổng
SELECT SUM(tong_tien) AS doanh_thu FROM don_hang
WHERE trang_thai = 'hoan_thanh';

-- AVG: trung bình
SELECT AVG(gia) AS gia_trung_binh FROM san_pham;

-- MIN / MAX
SELECT MIN(gia) AS re_nhat, MAX(gia) AS dat_nhat FROM san_pham;

-- GROUP BY: nhóm dữ liệu
SELECT
    danh_muc,
    COUNT(*)    AS so_san_pham,
    AVG(gia)    AS gia_tb,
    SUM(so_luong) AS tong_ton_kho
FROM san_pham
GROUP BY danh_muc;

-- HAVING: lọc SAU khi nhóm (khác với WHERE)
SELECT
    danh_muc,
    COUNT(*) AS so_san_pham
FROM san_pham
GROUP BY danh_muc
HAVING COUNT(*) > 1;  -- chỉ lấy danh mục có hơn 1 sản phẩm

-- So sánh WHERE vs HAVING:
-- WHERE  → lọc TRƯỚC khi nhóm (trên từng dòng)
-- HAVING → lọc SAU khi nhóm  (trên kết quả nhóm)
```

---

### Bài 8 — Subquery

Subquery là **câu lệnh SQL lồng bên trong** câu lệnh SQL khác.

```sql
-- Subquery trong WHERE: Lấy sản phẩm có giá cao hơn giá trung bình
SELECT ten_sp, gia
FROM san_pham
WHERE gia > (SELECT AVG(gia) FROM san_pham);

-- Subquery trong FROM (derived table)
SELECT danh_muc, gia_tb
FROM (
    SELECT danh_muc, AVG(gia) AS gia_tb
    FROM san_pham
    GROUP BY danh_muc
) AS bang_tb
WHERE gia_tb > 5000000;

-- EXISTS: kiểm tra sự tồn tại
SELECT ho_ten
FROM khach_hang kh
WHERE EXISTS (
    SELECT 1 FROM don_hang dh
    WHERE dh.khach_hang_id = kh.id
);

-- NOT EXISTS: khách hàng chưa có đơn hàng nào
SELECT ho_ten
FROM khach_hang kh
WHERE NOT EXISTS (
    SELECT 1 FROM don_hang dh
    WHERE dh.khach_hang_id = kh.id
);
```

---

### Bài 9 — Index & Hiệu Suất

```sql
-- Tạo index để tăng tốc độ tìm kiếm
CREATE INDEX idx_sp_danh_muc ON san_pham(danh_muc);
CREATE INDEX idx_kh_email    ON khach_hang(email);

-- Index đa cột (composite index)
CREATE INDEX idx_dh_kh_ngay ON don_hang(khach_hang_id, ngay_dat);

-- Xem các index của bảng
SHOW INDEX FROM san_pham;

-- Xóa index
DROP INDEX idx_sp_danh_muc ON san_pham;

-- EXPLAIN: xem kế hoạch thực thi truy vấn
EXPLAIN SELECT * FROM san_pham WHERE danh_muc = 'Phụ kiện';
```

**Nguyên tắc sử dụng Index:**

| Nên tạo Index | Không nên tạo Index |
|--------------|---------------------|
| Cột dùng trong `WHERE` thường xuyên | Bảng nhỏ (< 1000 dòng) |
| Cột dùng trong `JOIN` | Cột ít giá trị phân biệt (VD: cột boolean) |
| Cột dùng trong `ORDER BY` | Cột cập nhật cực kỳ thường xuyên |
| Cột `FOREIGN KEY` | Quá nhiều index trên một bảng |

---

### Bài 10 — Transaction

Transaction đảm bảo các thao tác **hoặc là thành công hoàn toàn, hoặc là không có gì thay đổi** (tính ACID).

```sql
-- Ví dụ: Chuyển tiền giữa hai tài khoản
START TRANSACTION;

UPDATE tai_khoan SET so_du = so_du - 1000000 WHERE id = 1;  -- trừ tài khoản A
UPDATE tai_khoan SET so_du = so_du + 1000000 WHERE id = 2;  -- cộng tài khoản B

-- Nếu cả hai đều thành công
COMMIT;

-- Nếu có lỗi xảy ra → hoàn tác tất cả
ROLLBACK;

-- SAVEPOINT: tạo điểm lưu giữa chừng
START TRANSACTION;
INSERT INTO don_hang ...;
SAVEPOINT sau_tao_don;

INSERT INTO chi_tiet_dh ...;  -- Nếu bước này lỗi
ROLLBACK TO SAVEPOINT sau_tao_don;  -- Quay về sau khi tạo đơn, không mất đơn hàng

COMMIT;
```

**Tính chất ACID của Transaction:**

| Tính chất | Ý nghĩa |
|-----------|---------|
| **A**tomicity (Nguyên tử) | Tất cả hoặc không có gì |
| **C**onsistency (Nhất quán) | Dữ liệu luôn hợp lệ trước và sau |
| **I**solation (Độc lập) | Các transaction không ảnh hưởng nhau |
| **D**urability (Bền vững) | Dữ liệu đã COMMIT không bị mất |

---

## 6. SQL Trong Công Việc

### 👨‍💼 Cần SQL Cho Vai Trò Nào?

```
Data Analyst          Data Engineer         Backend Developer
    ★★★★★                 ★★★★★                  ★★★★☆
  Bắt buộc           Không thể thiếu         Cần thiết hàng ngày

Business Analyst      QA / Tester           DevOps / DBA
    ★★★★☆                 ★★★☆☆                  ★★★★★
  Rất cần thiết       Hữu ích để kiểm tra    Chuyên sâu
```

### 📋 Công Việc Hàng Ngày Với SQL

**Data Analyst / Business Analyst:**
```sql
-- Báo cáo doanh thu theo tháng
SELECT
    DATE_FORMAT(ngay_dat, '%Y-%m') AS thang,
    SUM(tong_tien)                 AS doanh_thu,
    COUNT(*)                       AS so_don
FROM don_hang
WHERE trang_thai = 'hoan_thanh'
GROUP BY thang
ORDER BY thang;
```

**Backend Developer:**
```sql
-- Tìm kiếm sản phẩm có phân trang (cho API)
SELECT id, ten_sp, gia, danh_muc
FROM san_pham
WHERE (ten_sp LIKE '%laptop%' OR danh_muc = 'Máy tính')
  AND so_luong > 0
ORDER BY gia ASC
LIMIT 20 OFFSET 0;
```

**Data Engineer:**
```sql
-- ETL: chuyển dữ liệu từ bảng nguồn sang bảng tổng hợp
INSERT INTO bao_cao_doanh_thu_thang (thang, tong_doanh_thu, cap_nhat_luc)
SELECT
    DATE_FORMAT(ngay_dat, '%Y-%m'),
    SUM(tong_tien),
    NOW()
FROM don_hang
WHERE trang_thai = 'hoan_thanh'
  AND MONTH(ngay_dat) = MONTH(NOW() - INTERVAL 1 MONTH)
GROUP BY DATE_FORMAT(ngay_dat, '%Y-%m')
ON DUPLICATE KEY UPDATE
    tong_doanh_thu = VALUES(tong_doanh_thu),
    cap_nhat_luc   = VALUES(cap_nhat_luc);
```

**DBA (Database Administrator):**
```sql
-- Kiểm tra hiệu suất: tìm query chậm
SHOW PROCESSLIST;

-- Phân quyền người dùng
GRANT SELECT, INSERT ON cua_hang.* TO 'nhan_vien'@'localhost';
GRANT ALL PRIVILEGES ON cua_hang.* TO 'admin'@'localhost';
REVOKE DELETE ON cua_hang.* FROM 'nhan_vien'@'localhost';
```

---

## 7. Các Hệ Quản Trị Phổ Biến

| Tên | Loại | Phù hợp với | Điểm nổi bật |
|-----|------|------------|--------------|
| **MySQL** | Mã nguồn mở | Web app, startup | Phổ biến nhất, cộng đồng lớn |
| **PostgreSQL** | Mã nguồn mở | Ứng dụng phức tạp | Mạnh nhất về tính năng, tuân thủ chuẩn tốt |
| **SQLite** | Nhúng (embedded) | Mobile, desktop app | Không cần server, nhẹ, nhanh |
| **SQL Server** | Microsoft | Doanh nghiệp dùng Windows | Tích hợp tốt với hệ sinh thái Microsoft |
| **Oracle** | Thương mại | Ngân hàng, tập đoàn lớn | Cực kỳ mạnh, đắt tiền |
| **MariaDB** | Mã nguồn mở | Tương tự MySQL | Fork của MySQL, cải tiến hơn một số điểm |
| **BigQuery** | Cloud (Google) | Big Data, Analytics | Xử lý petabyte dữ liệu |
| **Redshift** | Cloud (AWS) | Data Warehouse | Tối ưu cho phân tích quy mô lớn |

> 💡 **Gợi ý:** Học MySQL hoặc PostgreSQL là lựa chọn tốt nhất khi bắt đầu. Kiến thức SQL cốt lõi có thể áp dụng cho tất cả các hệ thống trên.

---

## 8. Lỗi Thường Gặp & Cách Xử Lý

### ❌ Lỗi Cú Pháp Phổ Biến

```sql
-- ❌ Sai: Thiếu dấu nháy cho chuỗi
SELECT * FROM khach_hang WHERE ho_ten = Nguyen;

-- ✅ Đúng:
SELECT * FROM khach_hang WHERE ho_ten = 'Nguyen';

-- ❌ Sai: Thứ tự mệnh đề sai
SELECT * FROM san_pham HAVING gia > 1000 WHERE danh_muc = 'Máy tính';

-- ✅ Đúng:
SELECT * FROM san_pham WHERE danh_muc = 'Máy tính' HAVING gia > 1000;

-- ❌ Sai: GROUP BY thiếu cột
SELECT danh_muc, ten_sp, COUNT(*) FROM san_pham GROUP BY danh_muc;

-- ✅ Đúng:
SELECT danh_muc, COUNT(*) FROM san_pham GROUP BY danh_muc;
```

### ⚠️ Lỗi Logic Nguy Hiểm

```sql
-- ❌ Nguy hiểm: UPDATE / DELETE không có WHERE
UPDATE san_pham SET gia = 0;        -- Cập nhật TẤT CẢ sản phẩm!
DELETE FROM khach_hang;             -- Xóa TẤT CẢ khách hàng!

-- ✅ Luôn kiểm tra bằng SELECT trước:
SELECT * FROM san_pham WHERE danh_muc = 'Phụ kiện';  -- Xem trước
UPDATE san_pham SET gia = gia * 0.9 WHERE danh_muc = 'Phụ kiện'; -- Rồi mới cập nhật

-- ❌ Sai: So sánh NULL bằng dấu =
SELECT * FROM khach_hang WHERE so_dien_thoai = NULL;  -- Không bao giờ có kết quả!

-- ✅ Đúng:
SELECT * FROM khach_hang WHERE so_dien_thoai IS NULL;
```

### 🔐 SQL Injection — Lỗi Bảo Mật Nghiêm Trọng

```sql
-- ❌ KHÔNG BAO GIỜ ghép chuỗi trực tiếp từ input người dùng:
-- "SELECT * FROM users WHERE username = '" + input + "'"
-- Hacker nhập: ' OR '1'='1  → truy cập toàn bộ dữ liệu!

-- ✅ Dùng Parameterized Query (Prepared Statement):
-- Python: cursor.execute("SELECT * FROM users WHERE username = %s", (input,))
-- PHP:    $stmt->prepare("SELECT * FROM users WHERE username = ?")
-- Java:   PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE username = ?")
```

---

## 9. Tổng Kết

### 🗺️ Lộ Trình Học SQL

```
Giai đoạn 1 — Cơ bản (2–4 tuần)
├── SELECT, WHERE, ORDER BY, LIMIT
├── INSERT, UPDATE, DELETE
├── CREATE TABLE, các kiểu dữ liệu
└── Các hàm chuỗi, số, ngày tháng

Giai đoạn 2 — Trung cấp (1–2 tháng)
├── JOIN (INNER, LEFT, RIGHT)
├── GROUP BY, HAVING
├── Subquery
├── INDEX cơ bản
└── Transaction cơ bản

Giai đoạn 3 — Nâng cao (2–4 tháng)
├── Window Functions (ROW_NUMBER, RANK, LAG, LEAD...)
├── CTE (Common Table Expression) - WITH clause
├── Stored Procedure, Function
├── Trigger
├── Tối ưu hóa Query & Execution Plan
└── Bảo mật, phân quyền

Giai đoạn 4 — Chuyên sâu (liên tục)
├── Database Design & Normalization
├── Partitioning & Sharding
├── Replication & High Availability
└── Cloud Databases (BigQuery, Redshift, Snowflake)
```

### ✅ Checklist Kỹ Năng SQL

- [ ] Thành thạo SELECT với WHERE, ORDER BY, LIMIT
- [ ] Hiểu và dùng được tất cả loại JOIN
- [ ] Sử dụng GROUP BY và các hàm tổng hợp
- [ ] Viết được Subquery
- [ ] Biết tạo và quản lý Index
- [ ] Hiểu Transaction và ACID
- [ ] Biết EXPLAIN và đọc Execution Plan
- [ ] Viết được Stored Procedure cơ bản
- [ ] Hiểu SQL Injection và cách phòng chống
- [ ] Có thể thiết kế schema cho bài toán thực tế

### 💼 SQL Là Kỹ Năng Không Thể Thiếu Vì

1. **Phổ biến tuyệt đối** — Hầu hết mọi hệ thống đều dùng database quan hệ
2. **Lương cao hơn** — Kỹ năng SQL được yêu cầu trong hầu hết JD ngành Tech và Data
3. **Chuyển dịch linh hoạt** — Biết MySQL thì dễ học PostgreSQL, SQL Server...
4. **Không bao giờ lỗi thời** — SQL đã 50 năm và vẫn đang phát triển mạnh
5. **Tư duy phân tích** — SQL rèn luyện cách nghĩ theo tập hợp và logic

---

## 10. Tài Nguyên Học Thêm

### 🌐 Thực Hành Online (Miễn Phí)

| Nền tảng | Link | Nội dung |
|----------|------|---------|
| SQLZoo | [sqlzoo.net](https://sqlzoo.net) | Bài tập tương tác theo cấp độ |
| LeetCode | [leetcode.com/problemset/database](https://leetcode.com/problemset/database/) | SQL phỏng vấn kỹ thuật |
| HackerRank | [hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql) | Bài tập có chứng chỉ |
| Mode Analytics | [mode.com/sql-tutorial](https://mode.com/sql-tutorial/) | SQL cho Data Analysis |
| W3Schools SQL | [w3schools.com/sql](https://www.w3schools.com/sql/) | Tài liệu + thực hành |

### 📚 Tài Liệu Tham Khảo

- **PostgreSQL Documentation** — [postgresql.org/docs](https://www.postgresql.org/docs/) — Tài liệu chính thức đầy đủ nhất
- **MySQL Reference Manual** — [dev.mysql.com/doc](https://dev.mysql.com/doc/) — Tài liệu MySQL chính thức
- **Use The Index, Luke** — [use-the-index-luke.com](https://use-the-index-luke.com/) — Hướng dẫn tối ưu Index miễn phí

### 🛠️ Công Cụ Làm Việc Với SQL

| Công cụ | Dùng cho | Ghi chú |
|---------|---------|---------|
| **DBeaver** | Tất cả DB | Miễn phí, mạnh nhất |
| **TablePlus** | Mac/Win | Giao diện đẹp, nhẹ |
| **DataGrip** | Chuyên nghiệp | Trả phí, JetBrains |
| **pgAdmin** | PostgreSQL | Miễn phí, chính thức |
| **MySQL Workbench** | MySQL | Miễn phí, chính thức |
| **VS Code + Extensions** | Mọi loại | Nhẹ, tích hợp tốt |

---

<div align="center">

**📖 Tài liệu được tạo cho mục đích học tập và tham khảo**

*SQL — Học một lần, dùng cả đời*

</div>
