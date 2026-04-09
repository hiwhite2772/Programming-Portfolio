# Git & GitHub – Hướng dẫn cơ bản

## Mục lục
1. [Giới thiệu Git](#1-giới-thiệu-git)
2. [Giới thiệu GitHub](#2-giới-thiệu-github)
3. [So sánh Git và GitHub](#3-so-sánh-git-và-github)
4. [Git & GitHub dùng để làm gì?](#4-git--github-dùng-để-làm-gì)
5. [Git & GitHub dành cho ai?](#5-git--github-dành-cho-ai)
6. [Một số lệnh Git cơ bản](#6-một-số-lệnh-git-cơ-bản)

---

## 1. Giới thiệu Git

- **Git** là một **hệ thống quản lý phiên bản phân tán (VCS - Version Control System)**.  
- Nó giúp **lưu trữ lịch sử thay đổi của code hoặc file**, theo dõi ai đã làm gì, khi nào, và có thể **quay lại trạng thái trước đó**.  
- Git chạy **cục bộ trên máy của bạn**, không bắt buộc kết nối Internet.

**Ví dụ:**
```bash
git init       # Khởi tạo repository git
git add file   # Thêm file vào staging area
git commit -m "Initial commit"  # Lưu phiên bản
```

**Ưu điểm:**

- Lưu toàn bộ lịch sử dự án
- Hỗ trợ làm việc nhóm, merge code
- Phân nhánh (branch) và thử nghiệm dễ dàng

---

## 2. Giới thiệu GitHub
- GitHub là dịch vụ lưu trữ trực tuyến (cloud) cho Git repository.
- Cho phép chia sẻ code, làm việc nhóm, quản lý dự án.
- GitHub dùng Git làm nền tảng, nhưng thêm nhiều tính năng:
  - Giao diện web thân thiện
  - Issue tracker, pull request
  - GitHub Actions (CI/CD)
  - Hosting website (GitHub Pages)

Ví dụ:  
Bạn push repository local lên GitHub:
```base
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

---

## 3. So sánh Git và GitHub
|Tiêu chí |	Git |  GitHub |  
|:---------|:-----|:---------|  
| Loại |	Phần mềm cài trên máy	| Dịch vụ web/cloud |  
| Chức năng chính |	Quản lý phiên bản |	Lưu trữ Git repo trực tuyến, hợp tác |  
| Chạy offline | ✅	| ❌ (cần Internet để push/pull) |  
| Quản lý nhóm | ✅ (merge, branch) | ✅ (pull request, review) |  
| Giá trị |	Dành cho cá nhân hoặc nhóm nhỏ | Dễ chia sẻ, hợp tác, portfolio |

**Tóm tắt:**
- **Git** = “công cụ”  
- **GitHub** = “nền tảng” để chia sẻ công cụ và code với mọi người

---

## 4. Git & GitHub dùng để làm gì?
- **Quản lý code**: Theo dõi thay đổi, revert, branch
- **Làm việc nhóm**: Merge, pull request, review code
- **Portfolio cá nhân**: Trưng bày dự án lập trình
- **Học tập & open source**: Contribute vào dự án trên thế giới
- **Quản lý dự án**: Issue, milestone, wiki

---

## 5. Git & GitHub dành cho ai?
**Developer / Lập trình viên**  
**Sinh viên CNTT / học lập trình**  
**Nhóm làm dự án / công ty**  
**Data Scientist / ML Engineer**: quản lý notebook, script  
**Mọi người muốn version control file**  

⚡ Git & GitHub không chỉ cho code, bạn có thể dùng cho văn bản, markdown, hay cả file Excel lớn.

---

## 6. Một số lệnh Git cơ bản
| Lệnh Git | Mô tả |
| -------- | -------- |
| `git init` | Khởi tạo repo Git cục bộ |
| `git status` | Kiểm tra trạng thái file |
| `git add <file>` | Thêm file vào staging area |
| `git commit -m "msg"` | Lưu thay đổi với thông điệp |
| `git log` | Xem lịch sử commit |
| `git branch` | Xem hoặc tạo nhánh |
| `git checkout <branch>` | Chuyển nhánh |
| `git merge <branch>` | Gộp nhánh vào hiện tại |
| `git remote add origin <url>` | Thêm repo GitHub |
| `git push` | Đẩy code lên GitHub |
| `git pull` | Lấy code mới từ GitHub |

---

### ✅ Lời khuyên
- Học Git trước, GitHub sau
- Commit thường xuyên, thông điệp rõ ràng
- Branch cho mỗi tính năng / bugfix
- Sử dụng GitHub để chia sẻ portfolio và học hỏi open source