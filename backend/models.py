from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class ConversationSession(Base):
    __tablename__ = "conversation_sessions"

    session_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    started_at = Column(DateTime(timezone=True), server_default=func.now())

    messages = relationship("Message", back_populates="session")

class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("conversation_sessions.session_id"))
    sender = Column(Enum("user", "ai"))
    message = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("ConversationSession", back_populates="messages")
