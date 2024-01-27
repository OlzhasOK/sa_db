from database import engine
from models import metadata 


def create_tables():
    metadata.create_all(engine)