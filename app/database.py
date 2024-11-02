import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<useranme>:<password>@<ipaddress/lostname>/databasename'

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Ganesh%40m0477@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL) #Respomsible for databse connection if using SQLite need ti send connection args

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) #To talk to database

Base = declarative_base() # for create db and all

#depedency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host="",database="",user="",password="",cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#     except Exception as err:
#         print(str(err))