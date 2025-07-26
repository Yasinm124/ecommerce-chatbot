from sqlalchemy.orm import Session
from . import models, schemas

def create_session(db: Session, user_id: int):
    session = models.ConversationSession(user_id=user_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def add_message(db: Session, session_id: int, sender: str, message: str):
    msg = models.Message(session_id=session_id, sender=sender, message=message)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
