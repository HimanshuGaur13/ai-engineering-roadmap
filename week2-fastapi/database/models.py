from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from database.connection import Base


class EmployeeDB(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    salary = Column(Float, nullable=False)

    designation = Column(String, nullable=False)


class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )