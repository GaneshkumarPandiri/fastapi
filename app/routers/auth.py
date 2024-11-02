from fastapi import status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import List
from .. import schemas,models,utils
from ..database import get_db
from sqlalchemy.orm import Session
from . import oauth2

router = APIRouter(
    tags=["Auth"]
)

@router.post("/login", response_model=schemas.Token)
def user_login(user_credentials:OAuth2PasswordRequestForm = Depends() , db:Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
        if not user:
            print("No users")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
        if not utils.verify_passwords(user_credentials.password,user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
        access_token = oauth2.create_access_token(data = {"user_id":user.id})
        return {"access_token":access_token,"token_type":"bearer"}
    except Exception as err:
        print(err,"eee")


