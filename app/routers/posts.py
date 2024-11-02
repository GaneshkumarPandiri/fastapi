from fastapi import status,HTTPException,Depends,APIRouter,Response
from typing import List
from .. import schemas,models
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import oauth2
from typing import Optional


router = APIRouter(
    prefix="/posts",
     tags = ["Posts"]
)

@router.get("/",response_model=List[schemas.PostsRespopnse])
def get_posts(db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), limit : int = 10, skip : int = 0, search : Optional[str] = ""):
    # skip also can use
    my_posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # reslt_joins = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Post.id == models.Vote.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    if not my_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No data found")
    return my_posts

@router.get("/{id}",response_model=schemas.PostsRespopnse)
def get_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    try:
        my_post = db.query(models.Post).filter(models.Post.id == id).first()
        if not my_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found!")
        return my_post
    except Exception as err:
        print(err)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching the post.")



@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.PostsRespopnse)
def create_post(post: schemas.CreatePosts, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    new_post_resp = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post_resp)
    db.commit()
    db.refresh(new_post_resp)
    return new_post_resp


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    my_post = post_query.first()
    if not my_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found!")
    if my_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    post_query.delete(my_post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.PostsRespopnse)
def update_post(id: int, updated_post: schemas.UpdatePosts, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    try:
        post_query = db.query(models.Post).filter(models.Post.id == id)
        post = post_query.first()
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} Not Found")
        if post.owner_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
        post_query.update(updated_post.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        updated_post = post_query.first() 
        return updated_post 
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An internal server error occurred.")
