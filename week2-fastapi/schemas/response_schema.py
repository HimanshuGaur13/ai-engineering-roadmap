from pydantic import BaseModel


class EmployeeResponse(BaseModel):

    message: str
    data: dict