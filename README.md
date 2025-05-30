# 🍕 FastAPI Pizza Delivery API

A RESTful API for a pizza delivery service built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## 🚀 Features

- User authentication (signup & login)
- Order creation, update, and deletion
- Role-based access control (User & Superuser)
- API documentation via Swagger UI (`/docs`)

## 🛠 Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Documentation**: Swagger (auto-generated)

## 📌 API Routes

| Method | Endpoint                            | Description               | Access          |
|--------|-------------------------------------|---------------------------|-----------------|
| POST   | `/auth/signup/`                     | Register a new user       | Public          |
| POST   | `/auth/login/`                      | Login user                | Public          |
| POST   | `/orders/order/`                    | Place an order            | Authenticated   |
| PUT    | `/orders/order/update/{order_id}/`  | Update an order           | Authenticated   |
| PUT    | `/orders/order/status/{order_id}/`  | Update order status       | Superuser only  |
| DELETE | `/orders/order/delete/{order_id}/`  | Delete an order           | Authenticated   |
| GET    | `/orders/user/orders/`              | View current user's orders| Authenticated   |
| GET    | `/orders/orders/`                   | View all orders           | Superuser only  |
| GET    | `/orders/orders/{order_id}/`        | View specific order       | Superuser only  |
| GET    | `/orders/user/order/{order_id}/`    | View user's order by ID   | Authenticated   |
| GET    | `/docs/`                            | API documentation (Swagger UI) | Public     |

## 🔒 Authentication & Authorization

- Only registered users can create, view, or delete orders.
- Only superusers can view or update all orders and statuses.
- JWT-based authentication (mention explicitly if implemented).

## 📄 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/bkandh30/fastapi-pizzaDelivery.git
   cd fastapi-pizzaDelivery
   ```

2. **Activate virtual environment & install dependencies**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Visit** `http://localhost:8000/docs` for the interactive API docs.

## 🧪 Testing

You can use tools like **Postman** or **HTTPie** to test the endpoints, or interact directly via the Swagger UI.
