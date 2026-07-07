# 🔗 URL Shortener

live shortener link - https://dolfin2.pythonanywhere.com/

A simple URL Shortener built with **Python**, **Flask**, and **JSON** for storing links. The application allows users to shorten long URLs, redirect using a unique short code, track the number of clicks, and view all shortened links from a dashboard.

---

## ✨ Features

* Shorten long URLs into unique links
* Redirect users to the original website
* Track click count for every shortened URL
* Dashboard to view all generated links
* REST API to retrieve all stored links in JSON format
* Custom 404 page for invalid routes and short codes
* Data stored locally using a JSON file

---

## 🛠️ Technologies Used

* Python 3
* Flask
* HTML5
* CSS3
* JSON

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── data.json
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── 404.html
│
└── README.md
```

---

## 🚀 Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Move into the project directory.

```bash
cd <project-folder>
```

3. Install Flask.

```bash
pip install flask
```

4. Run the application.

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

<img width="1311" height="679" alt="image" src="https://github.com/user-attachments/assets/f73e3462-0017-4e7e-9413-56b1ac22ee08" />


---

### Dashboard

<img width="1310" height="673" alt="image" src="https://github.com/user-attachments/assets/20938002-48cb-4c82-9b08-0e9675c8d40b" />


---

### Custom 404 Page

<img width="1094" height="504" alt="image" src="https://github.com/user-attachments/assets/8d22cae4-9033-44b1-8ef1-56660d6b90c5" />


---

## 📡 API Endpoint

| Method | Endpoint     | Description                               |
| ------ | ------------ | ----------------------------------------- |
| GET    | `/api/links` | Returns all shortened URLs in JSON format |

---

## 💡 Future Improvements

* User authentication
* QR code generation
* Custom short URLs
* URL expiration dates
* Search and filter links
* Database support (SQLite/MySQL/PostgreSQL)

---

## 👨‍💻 Author

Developed as a Flask learning project.
