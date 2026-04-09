# Hướng dẫn tải và sử dụng Git & GitHub

## Mục lục
1. [Tải và cài Git](#1-tải-và-cài-git)
2. [Cấu hình Git cơ bản](#2-cấu-hình-git-cơ-bản)
3. [Đăng ký GitHub](#3-đăng-ký-github)
4. [Tạo repository trên GitHub](#4-tạo-repository-trên-github)
5. [Kết nối Git local với GitHub](#5-kết-nối-git-local-với-github)
6. [Quy trình làm việc cơ bản](#6-quy-trình-làm-việc-cơ-bản)
7. [Một số tips](#7-một-số-tips)

## 1. Tải và cài Git

### 1.1 Windows
1. Truy cập trang chính thức: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Chọn Windows → tải `.exe`  
3. Chạy file → nhấn `Next` theo mặc định (khuyến nghị để các option mặc định)  
4. Kiểm tra cài đặt: mở **Command Prompt** hoặc **Git Bash**, gõ:
```bash
git --version
```

- Nếu ra phiên bản Git → cài thành công

---

### 1.2 MacOS

1. Dùng Homebrew:  
```base
brew install git  
```
2. Hoặc tải từ trang Git → cài như Windows  
3. Kiểm tra:
```base
git --version
```

---

### 1.3 Linux  
1. Ubuntu/Debian:  
```base
sudo apt update  
sudo apt install git  
```
2. Fedora:  
```base
sudo dnf install git  
```
3. Kiểm tra:  
```base
git --version  
```

---

## 2. Cấu hình Git cơ bản
Sau khi cài, cấu hình thông tin cá nhân để commit:
```base
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```  
Kiểm tra:
```base
git config --list
```

---

## 3. Đăng ký GitHub
1. Truy cập: **https://github.com**
2. Nhấn Sign up, điền email, username, password
3. Xác thực email
4. GitHub cung cấp repo miễn phí, public/private tùy nhu cầu

---

## 4. Tạo repository trên GitHub
1. Đăng nhập → nhấn New repository
2. Điền: 
Repository name: my-project
3. Public/Private
4. Khởi tạo README (tuỳ chọn)
5. Nhấn Create repository

---

## 5. Kết nối Git local với GitHub
### 5.1 Clone repository từ GitHub
- git clone **https://github.com/username/my-project.git**
- Tạo folder my-project local → đồng bộ với GitHub
### 5.2 Thêm remote cho repo local mới
- git remote add origin **https://github.com/username/my-project.git**

---

## 6. Quy trình làm việc cơ bản
1. Thêm file mới / chỉnh sửa
```base
git add file.txt
```
2. Commit thay đổi
```base
git commit -m "Mô tả thay đổi"
```
3. Đẩy code lên GitHub
```base
git push origin main
```
4. Lấy code mới từ GitHub
```base
git pull origin main
```

⚡ **Lưu ý:** tên nhánh mặc định có thể là main hoặc master tùy repo

---

## 7. Một số tips
1. Dùng Git Bash hoặc Terminal để thao tác Git
2. Commit thường xuyên → dễ quản lý
3. Tạo branch cho mỗi tính năng / bugfix → tránh xung đột
4. GitHub Desktop có giao diện trực quan nếu không muốn dùng terminal

---

### ✅ Kết luận
- Cài Git → cấu hình username/email
- Tạo repo GitHub → kết nối với local
- Quy trình: add → commit → push → pull
- Dùng branch và commit thường xuyên → quản lý code tốt