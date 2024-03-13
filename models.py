from asyncio import tasks
from sqlalchemy import ForeignKey, Integer, Table, Column, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from crud import Base
from typing import List
from typing import Final 
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    # weeks: Mapped[List["Week"]] = relationship(secondary="task_week", back_populates="tasks")
    # projects: Mapped[List["Project"]] = relationship(secondary="project_task", back_populates="tasks")
    
    def __init__(self, name: str):
        self.name = name 

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, description={self.description}, estimate={self.estimate}, time={self.time}, completed={self.completed}, status={self.status}, start={self.start})>"

class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    estimate: Mapped[int] = mapped_column(default=0)
    time: Mapped[int] = mapped_column(default=0)
    completed: Mapped[bool] = mapped_column(default=False)
    status: Mapped[str] = mapped_column(default="TODO")
    start: Mapped[int] = mapped_column(default=0)
    users: Mapped[List["User"]] = relationship(secondary="user_project", back_populates="projects")
    project_task: Mapped[List[Task]] = relationship(secondary=lambda: project_tasks_table)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, description={self.description}, estimate={self.estimate}, time={self.time}, completed={self.completed}, status={self.status}, start={self.start})>"

    tasks: AssociationProxy[List[str]] = association_proxy("project_task", "tasks")


project_tasks_table: Final[Table] = Table(
    "project_task",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("project_id", Integer, ForeignKey("projects.id"), index=True),
    Column("task_id", Integer, ForeignKey("tasks.id"), index=True),
)


class Week(Base):
    __tablename__ = "weeks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    year: Mapped[int]
    week: Mapped[int]
    # tasks: Mapped[List["Task"]] = relationship(secondary="task_week", back_populates="weeks")

    def __repr__(self):
        return f"<Week(id={self.id}, name={self.name}, description={self.description}, completed={self.completed})>"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique= True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    hashed_password: Mapped[str]
    dob: Mapped[datetime] = mapped_column(insert_default=func.now())
    projects: Mapped[List["Project"]] = relationship(secondary="user_project", back_populates="users")
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, dob={self.dob})>"


user_project = Table(
    "user_project",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey("users.id"), index=True),
    Column("project_id", Integer, ForeignKey("projects.id"), index=True),
)

# project_task = Table(
#     "project_task",
#     Base.metadata,
#     Column("id", Integer, primary_key=True, index=True),
#     Column("project_id", Integer, ForeignKey("projects.id"), index=True),
#     Column("task_id", Integer, ForeignKey("tasks.id"), index=True),
#     )

task_week = Table(
    "task_week",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("task_id", Integer, ForeignKey("tasks.id"), index=True),
    Column("week_id", Integer, ForeignKey("weeks.id"), index=True),
    )
