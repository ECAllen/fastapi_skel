from redislite import Redis
from crud import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

sessions = Redis("sessions.db")

userids = Redis("userids.db")

# TODO move this to .env

##################################
# to get a string like this run:
# openssl rand -hex 32
##################################
SECRET_KEY = ""
ALGORITHM = ""
ACCESS_TOKEN_EXPIRE_MINUTES = 30
