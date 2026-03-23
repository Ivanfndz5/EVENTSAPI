# 🎟️ Events API

A RESTful API for event management built with FastAPI and Python. Registered users can create and manage events, purchase tickets, and handle their accounts securely with JWT authentication.

---

## 🚀 Tech Stack

- **Python** + **FastAPI**
- **SQLAlchemy** + **SQLite**
- **JWT Authentication** (python-jose)
- **Pydantic v2** for data validation
- **Alembic** for database migrations
- **Pytest** + **httpx** for testing

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/events-api.git
cd events-api
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run database migrations
```bash
alembic upgrade head
```

### 6. Start the server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## 📖 API Documentation

Interactive documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

---

## 🔐 Authentication

This API uses **Bearer JWT tokens**. After registering or logging in, include the token in the `Authorization` header:

```
Authorization: Bearer <your_token>
```

---

## 📌 Endpoints

### Auth
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/register` | ❌ | Register a new user |
| POST | `/auth/login` | ❌ | Login and receive JWT token |

### Events
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/events/` | ❌ | Get all events |
| GET | `/events/{id}` | ❌ | Get a single event |
| POST | `/events/` | ✅ | Create a new event |
| PUT | `/events/{id}` | ✅ | Update an event |
| DELETE | `/events/{id}` | ✅ | Delete an event |

### Users
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/users/` | ❌ | Create a user |
| GET | `/users/` | ✅ | Get all users |
| GET | `/users/{id}` | ✅ | Get a single user |
| DELETE | `/users/{id}` | ✅ | Delete a user |

### Tickets
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/tickets/` | ✅ | Create a ticket |

### Purchases
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/purchases/` | ✅ | Get all purchases |
| GET | `/purchases/{id}` | ✅ | Get a single purchase |
| POST | `/purchases/` | ✅ | Create a purchase |

---

## 🧪 Running Tests

```bash
pytest app/tests/ -v
```

---

## 📁 Project Structure

```
app/
├── core/
│   ├── database.py       # Database connection and session
│   └── security.py       # JWT authentication logic
├── models/               # SQLAlchemy models
├── routers/              # API route handlers
├── schemas/              # Pydantic schemas
├── services/             # Business logic
└── tests/                # Pytest test suite
migrations/               # Alembic migrations
```

---

## 👤 Author

Built by Ivan Fernandez, aspiring backend developer based in Rotterdam 🇳🇱