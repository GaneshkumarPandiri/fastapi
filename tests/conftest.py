
from fastapi.testclient import TestClient
from app.main import app
from app.routers import oauth2
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db,Base
import pytest
from alembic import command

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL) #Respomsible for databse connection if using SQLite need ti send connection args

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) #To talk to database

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine) # I want to check the db for test actually working orn not
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    except:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        except:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    

@pytest.fixture
def test_user(client):
    user_data = {
        "email":"ganesh@gmail.com",
        "password":"password123"
    }
    res = client.post("/users/",json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def token(test_user):
    return oauth2.create_access_token({"user_id":test_user})


@pytest.fixture
def authorized_client(client,token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    print(client,token,"fixtures resp===")
    return client