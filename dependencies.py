from redislite import Redis
from crud import SessionLocal
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
AlGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

sessions = Redis("sessions.db")

userids = Redis("userids.db")

