from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        min_length=3,
        max_length=50
    )
    salary: float = Field(
        gt=0
    )
    designation: str = Field(
        min_length=3,
        max_length=50
    )

class Config:
    from_attributes = True