# La Maison — Restaurant Website

A fullstack restaurant website built with **React + Vite + Tailwind CSS** (frontend) and **Flask + SQLAlchemy** (backend).

## Project Structure

```
Restaurant-website/
├── Restaurant-backend/     # Flask API
│   ├── app/
│   │   ├── __init__.py     # App factory
│   │   ├── models.py       # SQLAlchemy models
│   │   └── routes.py       # API routes
│   ├── seed.py             # Database seeder
│   ├── run.py              # Entry point
│   └── requirements.txt
└── Restaurant-frontend/    # React app
    └── src/
        ├── components/     # Navbar, Footer, MenuCard, SectionHeader
        └── pages/          # Home, Menu, Reservations, Contact
```

## Running the Backend

```bash
cd Restaurant-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py        # seed the database (run once)
python run.py         # starts on http://localhost:5000
```

## Running the Frontend

```bash
cd Restaurant-frontend
npm install
npm run dev           # starts on http://localhost:5173
```

## API Endpoints

| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| GET    | /api/menu              | All menu items           |
| GET    | /api/menu?category=X   | Filter by category       |
| GET    | /api/menu/featured     | Featured dishes          |
| GET    | /api/menu/categories   | All categories           |
| POST   | /api/reservations      | Create a reservation     |
| GET    | /api/reservations      | List all reservations    |
