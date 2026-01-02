# Bookstore-DRF-API
Here’s a professional, structured README you can copy-paste and adjust slightly for your style:

---

# Bookstore REST API

A fully functional **Bookstore API** built with **Python Django & Django REST Framework (DRF)**.
This project demonstrates building models, serializers, views, authentication, and REST API best practices.

## Features

* **Models**

  * `Book`, `Category`, `Tag`, `Review`, `Order`
  * Relationships: `ForeignKey`, `ManyToManyField`
  * Ratings and reviews attached to books
  * Orders with multiple books and total price calculation
* **Serializers**

  * Nested serializers for Reviews and Categories
  * Validation for ratings (1-5)
  * Read-only fields for sensitive data like username
* **Views & Endpoints**

  * List, Retrieve, and Create APIs for all models
  * Aggregation (`Avg` rating, `Count` total reviews)
  * Pagination for large datasets
  * Authentication for creating Reviews and Orders
* **Other Features**

  * Browsable API via DRF
  * Custom `perform_create` methods
  * Fully tested with `django-admin` and DRF

## Endpoints

| Endpoint       | Method    | Description                                                 |
| -------------- | --------- | ----------------------------------------------------------- |
| `/books/`      | GET       | List all available books                                    |
| `/books/<id>/` | GET       | Retrieve book details including reviews, tags, and category |
| `/categories/` | GET       | List all active categories                                  |
| `/reviews/`    | GET, POST | List reviews or create a review (authenticated only)        |
| `/orders/`     | GET, POST | List user orders or create a new order (authenticated only) |

## Installation

1. Clone the repository:

```bash
git clone <YOUR_REPO_URL>
cd bookstore
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (for admin):

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the API.

## Technologies Used

* Python 3.12+
* Django 6.x
* Django REST Framework
* SQLite (default DB, can be changed)
* DRF Pagination, Aggregation, Annotation

## Future Improvements

* Add filtering and search for books by category, price, author, and tags.
* Add authentication with JWT or token-based login.
* Add frontend to consume API (React / Vue / Next.js).
* Dockerize for deployment.

