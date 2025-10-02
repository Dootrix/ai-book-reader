from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Book Reader API",
    description="API for managing notes and bookmarks in the AI Book Reader",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Book Reader API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Export the app for Vercel
handler = app