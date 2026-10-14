#  Free-WiFi-Cafes

A web application built with Flask that helps users discover cafes, explore their facilities, and share ratings. Users can register, log in, add cafes, and manage the cafes they have submitted.

## 📌 About the Project

Cafe Finder makes it easier to find cafes according to their facilities and location. Users can explore available cafes, check information such as Wi-Fi, charging sockets, seating, and call facilities, and rate cafes based on their experience.

Registered users can also add new cafes and manage their own cafe listings.

## ✨ Features

- 🔐 **User Authentication** — Register and log in securely.
- ☕ **Explore Cafes** — View cafe details and available facilities.
- ➕ **Add Cafes** — Registered users can submit new cafe information.
- ✏️ **Update Cafes** — Users can update the cafes they have added.
- ⭐ **Rating System** — Logged-in users can rate cafes from 1 to 5.
- 📊 **Average Ratings** — Ratings are calculated and displayed for each cafe.
- 📍 **Location Information** — View cafe locations through map links.
- 📶 **Facility Details** — Check Wi-Fi, charging sockets, toilets, seating, and call facilities.
- 👤 **User Dashboard** — Manage your submitted cafes.
- 🚪 **Logout** — Securely end the current login session.
- 📱 **Responsive Design** — Bootstrap helps the interface adapt to different screen sizes.

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates

### Backend
- Python
- Flask
- Flask-Login
- Flask-WTF
- Flask-Bootstrap5
- Werkzeug

### Database
- SQLite
- Flask-SQLAlchemy
- SQLAlchemy ORM

## 📂 Project Structure

```text
Cafe-Finder/
│
├── instance/
│   └── cafes.db
│
├── static/
│   ├── styles.css
│   └── scripts.js
│
├── templates/
│   ├── about.html
│   ├── cafe_add.html
│   ├── cafeupdate.html
│   ├── footer.html
│   ├── header.html
│   ├── home.html
│   ├── index.html
│   ├── login.html
│   ├── sing.html
│   └── User.html
│
├── database.py
├── form.py
├── main.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 3. Open the Project Folder

```bash
cd Cafe-Finder
```

Use the actual folder name of your project if it is different.

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install flask flask-bootstrap flask-sqlalchemy flask-login flask-wtf werkzeug
```

### 6. Run the Application

```bash
python main.py
```

### 7. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000/
```

The application should now be running locally.

## 🗄️ Database

The project uses SQLite to store application data.

The database manages three main types of information:

- **Users:** Stores registered users and their password hashes.
- **Cafes:** Stores cafe details, facilities, locations, and ownership information.
- **Ratings:** Stores user ratings for individual cafes.

SQLAlchemy ORM is used to interact with the database through Python.

## 🔒 Authentication and Security

- Flask-Login manages user login sessions.
- Werkzeug password hashing is used to store passwords as hashes rather than plain text.
- Flask-WTF supports form validation and CSRF protection when configured correctly.
- Access restrictions help prevent unauthenticated users from accessing protected pages.

**Security note:** Before deploying the project publicly, use a strong secret key stored in an environment variable, and verify that every form and protected route is configured correctly.

## 🎯 Project Objective

The objective of Cafe Finder is to provide a simple platform where users can discover cafes, compare their facilities, contribute cafe information, and share ratings through an easy-to-use web interface.
c
Developed as a web development project using Python, Flask, Bootstrap, and SQLite.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
