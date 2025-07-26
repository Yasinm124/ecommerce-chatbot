import openai
import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import crud, schemas

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or set manually

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "E-commerce Chatbot Backend Running"}

@app.post("/start-session/")
def start_session(session: schemas.ConversationSessionCreate, db: Session = Depends(get_db)):
    return crud.create_session(db, session.user_id)

@app.post("/send-message/")
def send_message(msg: schemas.MessageCreate, db: Session = Depends(get_db)):
    # 1. Save user message
    user_msg = crud.add_message(db, msg.session_id, msg.sender, msg.message)

    # 2. Generate AI response
    ai_response = generate_ai_response(msg.message)

    # 3. Save AI message
    ai_msg = crud.add_message(db, msg.session_id, "ai", ai_response)

    return {"user_message": user_msg.message, "ai_response": ai_msg.message}

def generate_ai_response(user_input: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for an e-commerce chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {e}"
