from backend.database import engine, Base
from backend.models import *

Base.metadata.create_all(bind=engine)
