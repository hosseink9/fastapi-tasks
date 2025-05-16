from pydantic import BaseModel
from datetime import datetime

class CreateTask(BaseModel):
    title: str
    description: str = ""
    is_completed: bool = False


class ResponseTask(CreateTask):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
