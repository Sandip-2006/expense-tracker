# 💰 Expense Tracker

A simple and secure Expense Tracker web application built with **Django**.  
This project helps users manage their daily expenses with authentication (signup/login), add/view expenses, and track spending easily.



## 🚀 Features
- 🔐 User Authentication (Signup, Login, Logout)
- ➕ Add new expenses
- 📃 View all expenses (user-specific only)
- 🗑 Delete expenses
- 📊 Track expenses by date & category
- 🖥️ Responsive design with clean UI


## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default, can be changed to MySQL/PostgreSQL)
- **Version Control:** Git & GitHub


## 📂 Project Structure
expenses_tracker/
│── expenses_tracker/ # Project settings (settings.py, urls.py, wsgi.py)
│── expenses/ # Main app (models, views, templates, forms)
│── static/ # CSS, JS, Images
│── db.sqlite3 # Database file
│── manage.py # Django management script






## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run server**
   ```bash
   python manage.py runserver
   ```


## 🔑 Usage

   - Open http://127.0.0.1:8000/

   - Register a new user or login with existing credentials

   - Add and track your expenses
   - Logout securely

## 👨‍💻 Author

- Sandip Rathod
- BCA Student | Python & Full stack Devlopment