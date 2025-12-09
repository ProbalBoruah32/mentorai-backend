from fastapi import FastAPI

from app.api.routes_upload import router as upload_router
from app.api.routes_live import router as live_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MentorAI Backend Running"}

# Register API routes
app.include_router(upload_router, prefix="/api")
app.include_router(live_router, prefix="/api")
