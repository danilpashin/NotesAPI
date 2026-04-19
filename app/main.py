from fastapi import FastAPI
from app.database.database import engine, Base
from app.routes import notes_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

app.include_router(notes_routes.router, prefix="/notes", tags=["notes"])

@app.get("/")
def root():
    return {"message": "Notes API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}