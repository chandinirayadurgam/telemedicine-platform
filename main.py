from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import User, Appointment, SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "User registered"}

@app.get("/appointments")
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()
