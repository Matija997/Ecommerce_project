# E-Commerce Project

A full-stack e-commerce web app with a Vue 3 storefront and a Flask/SQLite backend. Includes browsing by category, product pages with per-size availability and image galleries, checkout, Google sign-in, and an admin panel for managing the product catalog (including discount tiers).

## Tech Stack

**Frontend**
- Vue 3 (`<script setup>` SFCs)
- Vite
- Vue Router
- Font Awesome

**Backend**
- Flask
- Flask-SQLAlchemy (SQLite)
- Flask-Bcrypt (password hashing)
- Flask-JWT-Extended (authentication)
- Google Sign-In (OAuth token verification)

## Project Structure

```
ecommerce_project/
├── src/                # Vue frontend
│   ├── views/          # Page components (Home, CategoryPage, ProductPage, Checkout, Admin, ...)
│   ├── components/     # Reusable UI components
│   ├── router/         # Vue Router routes
│   ├── store/          # App state
│   └── data/           # Static/reference data
├── backend/            # Flask API
│   ├── app.py          # App entry point, blueprint registration
│   ├── config.py       # App configuration (DB URI, secrets, Google client ID)
│   ├── models/         # SQLAlchemy models (User, Product)
│   ├── routes/         # API blueprints (auth, users, admin, products)
│   ├── seed_products.py
│   └── create_admin.py
└── public/
```

## Prerequisites

- Node.js 18+
- Python 3.11+

## Setup

### Frontend

```bash
npm install
```

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

The SQLite database is created automatically on first run at `backend/instance/store.db`.

To seed sample products or create an admin user:

```bash
python seed_products.py
python create_admin.py
```

## Running the App

The simplest way to run everything is from the project root:

```bash
npm run dev:all
```

This starts the Flask backend (`http://localhost:5000`) and the Vite frontend (`http://localhost:5173`) together, with each process's output prefixed in the terminal.

Alternatively, run them separately in two terminals:

```bash
# terminal 1, from backend/, with the virtual environment activated
python app.py
```

```bash
# terminal 2, from the project root
npm run dev
```

## Available Scripts

| Command | Description |
|---|---|
| `npm run dev:all` | Start the backend and frontend together |
| `npm run dev` | Start the Vite dev server only |
| `npm run backend` | Start the Flask backend only (uses `backend/venv`) |
| `npm run build` | Build the frontend for production |
| `npm run preview` | Preview the production build locally |

## Configuration Notes

- Backend secrets (`SECRET_KEY`, `JWT_SECRET_KEY`) and the Google OAuth client ID are currently set in `backend/config.py`. Move these to environment variables before deploying.
- `backend/instance/` (SQLite DB) and `backend/venv/` are git-ignored.
