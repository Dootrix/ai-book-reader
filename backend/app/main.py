from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import models to ensure they are registered with SQLAlchemy
from app.models import note, bookmark
from app.database.database import create_tables
from app.routers import notes, bookmarks

app = FastAPI(
    title="AI Book Reader API",
    description="Backend API for AI-assisted book reader application",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
async def startup_event():
    create_tables()

# Include routers
app.include_router(notes.router, prefix="/api/notes", tags=["notes"])
app.include_router(bookmarks.router, prefix="/api/bookmarks", tags=["bookmarks"])

@app.get("/")
async def read_root():
    return {"message": "AI Book Reader API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}