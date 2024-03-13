from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    id: int
    name: str
    description: str | None = None
    estimate: int | None = None


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    time: int | None = 0
    start: int | None = 0

    class Config:
        from_attributes = True


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


class UserProject(BaseModel):
    id: int
    user_id: int
    project_id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
