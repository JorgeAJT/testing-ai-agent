from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str
    password: str
    age: int
    languages: List[str]
