# ðŸŽŸï¸ Events API

A RESTful API for event management built with FastAPI and Python. Registered users can create and manage events, purchase tickets, and handle their accounts securely with JWT authentication.

---

## ðŸš€ Tech Stack

- **Python** + **FastAPI**
- **SQLAlchemy** + **SQLite**
- **JWT Authentication** (python-jose)
- **Pydantic v2** for data validation
- **Alembic** for database migrations
- **Pytest** + **httpx** for testing

---

## âš™ï¸ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ivanfndz5/EVENTSAPI.git
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

## ðŸ“– API Documentation

Interactive documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

---

## ðŸ” Authentication

This API uses **Bearer JWT tokens**. After registering or logging in, include the token in the `Authorization` header:

```
Authorization: Bearer <your_token>
```

---

## ðŸ“Œ Endpoints

### Auth
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/register` | âŒ | Register a new user |
| POST | `/auth/login` | âŒ | Login and receive JWT token |

### Events
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/events/` | âŒ | Get all events |
| GET | `/events/{id}` | âŒ | Get a single event |
| POST | `/events/` | âœ… | Create a new event |
| PUT | `/events/{id}` | âœ… | Update an event |
| DELETE | `/events/{id}` | âœ… | Delete an event |

### Users
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/users/` | âŒ | Create a user |
| GET | `/users/` | âœ… | Get all users |
| GET | `/users/{id}` | âœ… | Get a single user |
| DELETE | `/users/{id}` | âœ… | Delete a user |

### Tickets
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/tickets/` | âœ… | Create a ticket |

### Purchases
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/purchases/` | âœ… | Get all purchases |
| GET | `/purchases/{id}` | âœ… | Get a single purchase |
| POST | `/purchases/` | âœ… | Create a purchase |

---

## ðŸ§ª Running Tests

```bash
pytest app/tests/ -v
```

---

## ðŸ“ Project Structure

```
app/
â”œâ”€â”€ core/
â”‚   â”œâ”€â”€ database.py       # Database connection and session
â”‚   â””â”€â”€ security.py       # JWT authentication logic
â”œâ”€â”€ models/               # SQLAlchemy models
â”œâ”€â”€ routers/              # API route handlers
â”œâ”€â”€ schemas/              # Pydantic schemas
â”œâ”€â”€ services/             # Business logic
â””â”€â”€ tests/                # Pytest test suite
migrations/               # Alembic migrations
```

---

## ðŸ‘¤ Author

Built by Ivan Fernandez, aspiring backend developer based in Rotterdam ðŸ‡³ðŸ‡±
