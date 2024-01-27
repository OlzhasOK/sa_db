from sqlalchemy import create_engine, text
from config import settings 

engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo=True
)

with engine.connect() as connect:
    result = connect.execute(text('SELECT VERSION()'))
    print(result.first())