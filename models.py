from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "postgresql://postgres:password@localhost/telemedicine"

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    password = Column(String)  # Hashed password
    is_doctor = Column(Boolean, default=False)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    patient_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="scheduled")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
