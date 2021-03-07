from typing import List
from pydantic import BaseModel


class Group(BaseModel):
    name: str
    users_ids: List[str]
