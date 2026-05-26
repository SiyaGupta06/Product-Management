from app.database.connection import engine
from app.database.base import Base
from app.database.models import *

Base.metadata.drop_all(bind=engine)
print("All tables dropped successfully.")