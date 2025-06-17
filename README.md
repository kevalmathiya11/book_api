# 📚 Book Catalog API – Django REST Framework

A RESTful API for managing a book catalog system with authentication and cover image uploads.

---

## 🚀 Tech Stack
- Python 
- Django 
- Django REST Framework
- Pillow
- python-decouple

---

## 🔧 Setup Instructions

1. **Clone the Repository** 
   git clone https://github.com/kevalmathiya11/book_api.git
   cd book_api
   
2. **Create Virtual Environment**
   
python -m venv .venv
source .venv/bin/activate  or .venv\Scripts\activate -> on Windows

3.**Install Dependencies**

pip install -r requirements.txt

4.**Create .env File**

API_KEY=your-api-key-here

5.**Run Migrations**

python manage.py makemigrations
python manage.py migrate

6.**Start the Server**

python manage.py runserver

# 🔐 API Authentication
Use X-API-Key header in requests to protected endpoints.


# Screenshorts of API testing in Postman
google-drive-link : https://drive.google.com/drive/folders/1jRIOg2IABwwtYCX7MjHjTsKCsKAO1bIX?usp=sharing

