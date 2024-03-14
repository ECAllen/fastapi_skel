from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column 
from crud import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique= True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    hashed_password: Mapped[str]
    dob: Mapped[datetime] = mapped_column(insert_default=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, dob={self.dob})>"


