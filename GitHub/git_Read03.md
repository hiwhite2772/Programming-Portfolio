# Git – Xóa, Khôi phục & Kiểm tra File

> 📚 Ghi chú học Git: xử lý file bị xóa, khôi phục file và xóa file khỏi Git history.

---

## 📑 Mục lục

* [1. Hiểu về Git History](#1-hiểu-về-git-history)
* [2. Kiểm tra lịch sử của file](#2-kiểm-tra-lịch-sử-của-file)
* [3. Khôi phục file](#3-khôi-phục-file)

  * [3.1. File vừa xóa, chưa commit](#31-file-vừa-xóa-chưa-commit)
  * [3.2. File đã xóa và đã commit](#32-file-đã-xóa-và-đã-commit)
  * [3.3. Khôi phục file từ commit cũ](#33-khôi-phục-file-từ-commit-cũ)
* [4. Máy tính không còn file](#4-máy-tính-không-còn-file)
* [5. Repository hiện tại không còn file](#5-repository-hiện-tại-không-còn-file)
* [6. Xóa file khỏi Repository](#6-xóa-file-khỏi-repository)

  * [6.1. Xóa file nhưng giữ Git history](#61-xóa-file-nhưng-giữ-git-history)
  * [6.2. Xóa file khỏi toàn bộ Git history](#62-xóa-file-khỏi-toàn-bộ-git-history)
* [7. Trường hợp file đã bị xóa khỏi History](#7-trường-hợp-file-đã-bị-xóa-khỏi-history)
* [8. Tìm file đã mất bằng Git Objects](#8-tìm-file-đã-mất-bằng-git-objects)
* [9. Khi nào Git không thể khôi phục?](#9-khi-nào-git-không-thể-khôi-phục)
* [10. Bảng tình huống nhanh](#10-bảng-tình-huống-nhanh)
* [11. Nguyên tắc xử lý](#11-nguyên-tắc-xử-lý)
* [12. Ba lệnh quan trọng cần nhớ](#12-ba-lệnh-quan-trọng-cần-nhớ)

---

# 1. Hiểu về Git History

Git không chỉ lưu trạng thái hiện tại của project.

Mỗi commit có thể lưu lại trạng thái của file tại thời điểm đó.

Ví dụ:

```text
Commit A
   ↓
Commit B
   ↓
Commit C
   ↓
Current version
```

Một file có thể:

```text
Commit A → có file
Commit B → có file
Commit C → xóa file
Current  → không có file
```

Mặc dù file không còn ở phiên bản hiện tại, Git vẫn có thể khôi phục nó nếu dữ liệu cũ vẫn còn trong history.

---

# 2. Kiểm tra lịch sử của file

## Cú pháp

```cmd
git log --all -- "<PATH/TO/FILE>"
```

## Ví dụ

```cmd
git log --all -- "Project/demo.py"
```

Nếu Git trả về các commit cũ → file vẫn còn trong history.

Ví dụ:

```text
commit abc123
Author: ...
Date: ...

    Add demo project
```

Có thể dùng mã commit (`COMMIT_ID`) đó để kiểm tra hoặc khôi phục file.

---

## Xem nội dung file ở một commit cũ

### Cú pháp

```cmd
git show "<COMMIT_ID>:<PATH/TO/FILE>"
```

### Ví dụ

```cmd
git show "abc123:Project/demo.py"
```

→ Hiển thị nội dung file tại commit `abc123`.

---

# 3. Khôi phục file

## 3.1. File vừa xóa, chưa commit

Nếu bạn vừa xóa file nhưng **chưa commit**, có thể khôi phục:

### Cú pháp

```cmd
git restore "<PATH/TO/FILE>"
```

### Ví dụ

```cmd
git restore "Project/demo.py"
```

Sau đó:

```cmd
git status
```

File sẽ trở lại trạng thái của commit hiện tại.

---

## 3.2. File đã xóa và đã commit

Nếu file đã bị xóa trong một commit nhưng history cũ vẫn còn:

### Bước 1 – Tìm history

```cmd
git log --all -- "<PATH/TO/FILE>"
```

### Bước 2 – Chọn commit còn file

```cmd
git restore --source=<COMMIT_ID> -- "<PATH/TO/FILE>"
```

### Bước 3 – Commit lại

```cmd
git add "<PATH/TO/FILE>"
git commit -m "Restore deleted file"
git push
```

---

## 3.3. Khôi phục file từ một commit cụ thể

### Cú pháp

```cmd
git restore --source=<COMMIT_ID> -- "<PATH/TO/FILE>"
```

### Ví dụ

```cmd
git restore --source=abc123 -- "Project/demo.py"
```

Kiểm tra:

```cmd
git status
```

Sau đó nếu đúng:

```cmd
git add "Project/demo.py"
git commit -m "Restore deleted file"
git push
```

---

# 4. Máy tính không còn file

Việc file không còn trên máy **không có nghĩa là file đã mất hoàn toàn**.

Nếu file từng được commit vào Git, kiểm tra:

```cmd
git log --all -- "<PATH/TO/FILE>"
```

Nếu vẫn còn history:

```cmd
git restore --source=<COMMIT_ID> -- "<PATH/TO/FILE>"
```

Hoặc chỉ xem nội dung:

```cmd
git show "<COMMIT_ID>:<PATH/TO/FILE>"
```

### Ví dụ

Máy tính:

```text
Project/
└── demo.py   ← không còn
```

Nhưng Git history:

```text
Commit abc123
└── Project/demo.py
```

→ Có thể lấy `demo.py` trở lại bằng Git.

---

# 5. Repository hiện tại không còn file

Trường hợp:

```text
Current version:
    demo.py ❌

Old commit:
    demo.py ✅
```

File vẫn có thể khôi phục.

Kiểm tra:

```cmd
git log --all -- "Project/demo.py"
```

Sau đó:

```cmd
git restore --source=<COMMIT_ID> -- "Project/demo.py"
```

---

# 6. Xóa file khỏi Repository

Có hai kiểu xóa quan trọng.

---

## 6.1. Xóa file nhưng giữ Git history

Dùng khi chỉ muốn file biến mất khỏi phiên bản hiện tại.

### Cú pháp

```cmd
git rm "<FILE>"
git commit -m "Remove file"
git push
```

### Ví dụ

```cmd
git rm "Project/demo.py"
git commit -m "Remove demo file"
git push
```

Kết quả:

```text
Current version → file không còn
Old commits     → file vẫn còn
```

✅ Có thể khôi phục file từ commit cũ.

---

# 6.2. Xóa file khỏi toàn bộ Git history

Dùng khi muốn loại bỏ file khỏi lịch sử Git đã được rewrite.

> ⚠️ Đây là thao tác nâng cao và có thể thay đổi lịch sử repository.

### Cú pháp

```cmd
git filter-repo --force --path "<PATH/TO/FILE>" --invert-paths
```

### Ví dụ – một file

```cmd
git filter-repo --force --path "Project/demo.py" --invert-paths
```

### Ví dụ – nhiều file

```cmd
git filter-repo --force ^
  --path "Project/Demo_1/demo_1.py" ^
  --path "Project/Demo_2/demo_2.py" ^
  --path "Project/Demo_3/demo_3.py" ^
  --invert-paths
```

Sau khi rewrite history, kiểm tra:

```cmd
git log --all -- "Project/Demo_1/demo_1.py"
```

Nếu không còn commit nào → file đã được loại khỏi history mà bạn vừa rewrite.

---

## Push history mới

Sau khi kiểm tra kỹ:

```cmd
git push origin --force --all
git push origin --force --tags
```

> ⚠️ `--force` sẽ thay thế lịch sử trên remote. Không nên sử dụng nếu chưa kiểm tra kỹ.

---

# 7. Trường hợp file đã bị xóa khỏi History

Nếu đã chạy:

```cmd
git filter-repo --force --path "<PATH/TO/FILE>" --invert-paths
```

và:

```cmd
git log --all -- "<PATH/TO/FILE>"
```

không còn kết quả:

→ File đã bị loại khỏi history hiện tại.

Trong trường hợp này, `git restore` thường không thể tìm thấy file nữa.

Tuy nhiên, vẫn có thể còn bản sao ở:

```text
Clone cũ
    ↓
Backup
    ↓
Reflog
    ↓
Git objects
```

Vì vậy **đừng vội chạy cleanup hoặc xóa backup** nếu đang cố khôi phục file.

---

# 8. Tìm file đã mất bằng Git Objects

Đây là trường hợp nâng cao.

Nếu file không còn trong branch/history thông thường, có thể kiểm tra reflog:

```cmd
git reflog --all
```

Hoặc kiểm tra các Git objects không còn được tham chiếu:

```cmd
git fsck --full --no-reflogs
```

Có thể xuất hiện:

```text
dangling commit ...
dangling blob ...
```

Những object này đôi khi vẫn chứa dữ liệu cũ.

> ⚠️ Không nên chạy các lệnh cleanup/garbage collection trước khi kiểm tra, vì có thể làm mất những object đang cố khôi phục.

---

# 9. Khi nào Git không thể khôi phục?

Git không phải hệ thống backup tuyệt đối.

Nếu tất cả những nơi sau đều không còn dữ liệu:

```text
Git history
     ↓
Reflog
     ↓
Git objects
     ↓
Clone cũ
     ↓
Backup
     ↓
Máy tính / ổ cứng
```

→ Git không thể tự tạo lại nội dung file đã mất.

---

# 10. Bảng tình huống nhanh

| Tình huống                                              | Có thể khôi phục?     |
| ------------------------------------------------------- | --------------------- |
| File vừa xóa, chưa commit                               | ✅ Có                  |
| File đã xóa và đã commit                                | ✅ Có, nếu history còn |
| File không còn trên máy nhưng Git history còn           | ✅ Có                  |
| File không còn ở phiên bản hiện tại nhưng commit cũ còn | ✅ Có                  |
| Đã `filter-repo` nhưng còn clone/backup cũ              | ✅ Có                  |
| Đã `filter-repo` và dữ liệu cũ đã bị Git dọn            | ❌ Thường không        |
| Không còn history, reflog, objects, clone hoặc backup   | ❌ Không               |

---

# 11. Nguyên tắc xử lý

Khi một file bị mất:

```text
File bị mất
    ↓
git log --all -- "<FILE>"
    ↓
History còn?
    ├── Có
    │    ↓
    │  git restore
    │
    └── Không
         ↓
       Kiểm tra reflog
         ↓
       Kiểm tra Git objects
         ↓
       Kiểm tra clone / backup
         ↓
       Còn dữ liệu?
         ├── Có → Khôi phục
         └── Không → Có thể đã mất hoàn toàn
```

---

# 12. Ba lệnh quan trọng cần nhớ

## 🔎 Tìm file trong history

```cmd
git log --all -- "<FILE>"
```

> File này từng xuất hiện trong những commit nào?

---

## ♻️ Khôi phục file

```cmd
git restore --source=<COMMIT_ID> -- "<FILE>"
```

> Lấy file từ một commit cụ thể trở lại working tree.

---

## 🧹 Xóa file khỏi toàn bộ history

```cmd
git filter-repo --force --path "<FILE>" --invert-paths
```

> Loại file khỏi history được rewrite.

---

## 📌 Ghi nhớ cuối cùng

```text
git rm
    ↓
Xóa file khỏi phiên bản hiện tại
    ↓
History cũ vẫn còn
    ↓
Có thể khôi phục
```

Trong khi:

```text
git filter-repo
    ↓
Rewrite Git history
    ↓
Loại file khỏi history
    ↓
Khó / không thể khôi phục nếu không còn backup hoặc clone cũ
```

> **Trước khi dùng `--force`, luôn kiểm tra kỹ mình đang đứng ở repository nào.**
>
> **Trước khi xóa history, nên có một bản backup/clone riêng.**
>
> **Nếu file chứa secret (API key, password, token...), hãy đổi/revoke secret thay vì chỉ xóa file.**
