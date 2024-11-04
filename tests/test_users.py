from app import schemas
import pytest
import jwt
from app.config import settings




def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json().get("message") == "Hello World!!!"

def test_create_user(client):
    #json is for body need to send through body data
    resp = client.post("/users/",json={"email":"ganesh.m0477@gmail.com","password":"Ganesh@m0477"})
    new_user = schemas.UserResponse(**resp.json())
    assert resp.status_code == 201
    assert new_user.email == "ganesh.m0477@gmail.com"

def test_login_user(test_user,client):
    #data is for body need to send through form data
    resp = client.post("/login",data={"username":test_user["email"],"password":test_user["password"]})
    login_details = schemas.Token(**resp.json())
    payload = jwt.decode(login_details.access_token,settings.secret_key,algorithms=settings.algorithm)
    id : str = payload.get("user_id")
    assert id == test_user["id"]
    assert resp.status_code == 200


# @pytest.mark.parametrize("email, password, status_code")
def test_login_wrong_user(test_user,client):
    #data is for body need to send through form data
    resp = client.post("/login",data={"username":test_user["email"],"password":"wrongpassword"})
    assert resp.status_code == 403
    assert resp.json().get('detail') == "Invalid Credentials"
    



