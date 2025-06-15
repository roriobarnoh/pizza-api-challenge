# 🍕 Pizza Restaurant API

A RESTful API for managing restaurants and pizzas, built using **Flask**, **SQLAlchemy**, and **Flask-Migrate**.

---

## 📦 Features

- Manage restaurants and pizzas with full CRUD operations
- Join table `RestaurantPizza` handles pricing of specific pizzas at specific restaurants
- MVC project structure
- Cascading delete support
- Built-in validations (e.g. price range 1–30)
- API tested using Postman

---

## 📁 Project Structure

├── server/
│ ├── app.py # Flask app setup
│ ├── config.py # DB and app config
│ ├── models/ # SQLAlchemy models
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/ # Route logic
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
│ ├── seed.py # Seed data
├── migrations/ # Alembic migrations
├── challenge-1-pizzas.postman_collection.json
└── README.md

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/pizza-api-challenge.git
cd pizza-api-challenge

### 2.  Create virtual environment and install dependencies
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

### 3. Set up the database
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 4. Seed the database
python server/seed.py
