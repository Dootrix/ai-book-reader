from app.main import app

# This is the Vercel serverless function handler
def handler(request, response):
    return app(request, response)