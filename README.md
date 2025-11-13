
# 🛒 Online Shop

A simple e-commerce web application built with Django, designed to handle user registration, product management, shopping cart, order processing, and payment functionality.

## ✨ Features

- User registration and login
- Product listing with images and descriptions
- Add to cart and view cart
- Place orders and simulate payment
- Responsive and Persian-translated UI
- Admin panel for managing users and orders

## 🧰 Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Languages:** CSS (64%), JavaScript (22%), HTML (8%), Python (5%)

## 📁 Project Structure

- `accounts/` – User authentication and profile management
- `cart/` – Shopping cart logic
- `orders/` – Order tracking and processing
- `products/` – Product models and views
- `payment/` – Payment simulation
- `pages/` – Static and general pages
- `persian_translate/` – Persian language support
- `templates/` – HTML templates
- `static/` and `staticfiles/` – Static assets

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Hamzei0/online-shop.git
cd online-shop





2. Create a virtual environment and install dependencies:



python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt




3. Run the development server:



python manage.py runserver




4. Open your browser and visit:



http://127.0.0.1:8000




📌 Notes


* The `db.sqlite3` file includes sample data for testing.
* Security settings like `SECRET_KEY` and `DEBUG` should be configured via environment variables.
* Persian translations are located in the `persian_translate/` directory.



