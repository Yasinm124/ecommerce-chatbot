from pydantic import BaseModel
from typing import List

class MessageCreate(BaseModel):
    session_id: int
    sender: str
    message: str

class ConversationSessionCreate(BaseModel):
    user_id: int

class MessageResponse(BaseModel):
    message_id: int
    sender: str
    message: str
