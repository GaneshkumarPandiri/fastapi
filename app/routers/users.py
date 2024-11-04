from fastapi import status,HTTPException,Depends,APIRouter
from sqlalchemy.exc import IntegrityError
from .. import schemas,utils,models
from ..database import get_db
from sqlalchemy.orm import Session


 
router = APIRouter(
    prefix="/users",
    tags = ["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hass_password(user.password)
        user.password = hashed_password
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as err:
        db.rollback()  # Rollback the transaction to avoid a stale state
        print("IntegrityError:", str(err))
        # Raise an HTTPException to ensure FastAPI returns the error as a response
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists.")
    except Exception as err:
        print("General error:", str(err))
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(err))

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id : int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with user id:{id} not found")
    return user