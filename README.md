# Tên Dự Án

Ứng dụng tạo quiz với các câu hỏi và câu trả lời.

## Tính Năng Chính

- 🎨 **Tailwind CSS** - Framework CSS linh hoạt và tùy biến cao
- 🐍 **Django** - Framework web Python mạnh mẽ và an toàn
- ⚡ **HTMX** - Công cụ hiện đại cho tương tác động không cần JavaScript
- 🔐 **Authentication** - Hệ thống xác thực người dùng tích hợp
- 📊 **Admin One** - Giao diện quản trị viên đẹp mắt dựa trên [Admin One Tailwind](https://github.com/justboil/admin-one-tailwind)

## Yêu Cầu Hệ Thống

- Python 3.8+
- Node.js & npm (cho Tailwind CSS)
- pip

## Cài Đặt

1. Clone repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Tạo và kích hoạt môi trường ảo:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/MacOS
```

3. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
npm install
```

## Khởi Chạy Ứng Dụng

1. Kích hoạt môi trường ảo:
```bash
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/MacOS
```

2. Chạy migrations:
```bash
python manage.py migrate
```

3. Khởi động server:
```bash
python manage.py runserver
```

Truy cập ứng dụng tại `http://localhost:8000`

4. rebuild assets:
```bash
npx tailwindcss -i ./framework/static/css/main.css -o ./framework/static/css/main.min.css

# watch
npx tailwindcss -i ./framework/static/css/main.css -o ./framework/static/css/main.min.css --watch
```


## Đóng Góp

Mô tả cách người khác có thể đóng góp vào dự án của bạn.

## Giấy Phép

[MIT License](LICENSE) hoặc giấy phép phù hợp khác

## Liên Hệ

- Tên: Bính Lê
- Email: letatbinh130794@gmail.com
