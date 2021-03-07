from typing import List, Optional
from pydantic import BaseModel


class Notification(BaseModel):
    notification_type: str
    message: str
    message_type: str
    ids: List[str]
    time_of_return: Optional[str] = None
