# AI Book Reader

AI assisted book reader with smart notes and bookmarks management.

## Features

- 📝 **Smart Notes**: Take AI-powered notes while reading
- 🔖 **Bookmarks**: Save important passages and references  
- 🤖 **AI Insights**: Get AI-generated summaries and insights (coming soon)
- 💾 **SQLite Database**: Local storage for notes and bookmarks

## Tech Stack

### Frontend
- **Next.js 15** with TypeScript
- **React 19**
- **Tailwind CSS** for styling
- **App Router** for navigation

### Backend
- **FastAPI** with Python 3.12
- **SQLAlchemy** for database ORM
- **SQLite** for data storage
- **Pydantic** for data validation
- **CORS** enabled for frontend integration

## Project Structure

```
ai-book-reader/
├── frontend/          # Next.js 15 frontend application
│   ├── app/          # App router pages and components
│   │   ├── notes/    # Notes management page
│   │   ├── bookmarks/# Bookmarks management page
│   │   └── ...
│   └── package.json  # Frontend dependencies
├── backend/          # FastAPI backend application
│   ├── app/         # Main application code
│   │   ├── main.py  # FastAPI app and routes
│   │   ├── models.py# SQLAlchemy database models
│   │   ├── schemas.py# Pydantic schemas
│   │   └── database.py# Database configuration
│   └── requirements.txt# Backend dependencies
├── vercel.json      # Vercel deployment configuration
└── start.sh         # Local development script
```

## Getting Started

### Prerequisites
- Node.js 20+
- Python 3.12+
- npm or yarn

### Installation

1. **Install Frontend Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

### Development

#### Option 1: Start Both Servers with Script
```bash
chmod +x start.sh
./start.sh
```

#### Option 2: Start Servers Individually

**Backend (Terminal 1):**
```bash
cd backend
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend (Terminal 2):**
```bash
cd frontend
npm run dev
```

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## API Endpoints

### Notes
- `GET /notes/` - List all notes
- `POST /notes/` - Create a new note
- `GET /notes/{id}` - Get specific note
- `PUT /notes/{id}` - Update note
- `DELETE /notes/{id}` - Delete note

### Bookmarks
- `GET /bookmarks/` - List all bookmarks
- `POST /bookmarks/` - Create a new bookmark
- `GET /bookmarks/{id}` - Get specific bookmark
- `DELETE /bookmarks/{id}` - Delete bookmark

## Deployment

This project is configured for deployment on **Vercel**:

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the configuration from `vercel.json`
3. Both frontend and backend will be deployed as serverless functions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is open source and available under the MIT License.
