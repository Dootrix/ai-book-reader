# AI Book Reader

An AI-assisted book reader application with note-taking and bookmarking capabilities.

## Project Structure

```
ai-book-reader/
├── frontend/          # Next.js 15 React application
├── backend/           # FastAPI Python application
└── README.md
```

## Setup Instructions

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- pip

### Frontend Setup (Next.js 15)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

### Backend Setup (FastAPI + SQLite)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   python run.py
   ```

The backend API will be available at `http://localhost:8000`
- API documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

## API Endpoints

### Notes
- `GET /api/notes/` - Get all notes
- `GET /api/notes/{note_id}` - Get specific note
- `POST /api/notes/` - Create new note
- `PUT /api/notes/{note_id}` - Update note
- `DELETE /api/notes/{note_id}` - Delete note

### Bookmarks
- `GET /api/bookmarks/` - Get all bookmarks
- `GET /api/bookmarks/{bookmark_id}` - Get specific bookmark
- `POST /api/bookmarks/` - Create new bookmark
- `PUT /api/bookmarks/{bookmark_id}` - Update bookmark
- `DELETE /api/bookmarks/{bookmark_id}` - Delete bookmark

## Database

The application uses SQLite for data persistence. The database file (`ai_book_reader.db`) will be created automatically when you first run the backend server.

## Development

- Frontend uses Next.js 15 with TypeScript and Tailwind CSS
- Backend uses FastAPI with SQLAlchemy ORM
- CORS is configured to allow frontend-backend communication
