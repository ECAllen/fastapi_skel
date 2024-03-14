from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int
    email: str | None = None
    username: str


class UserCreate(UserBase):
    hashed_password: str = Field(alias="password")


class User(UserBase):
    is_active: bool
    projects: list[Project] = []
    full_name: str | None = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
