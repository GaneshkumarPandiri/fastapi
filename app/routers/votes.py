from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import database,models,schemas
from .. import schemas
from .oauth2 import get_current_user



router = APIRouter(
    prefix="/vote",
    tags=["Votes"]
    )

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_votes(vote : schemas.CreateVote ,db : Session = Depends(database.get_db), current_user : int = Depends(get_current_user) ):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.post_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Already voted")
        new_vote = models.Vote(post_id = vote.post_id,user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Voted Successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"Successfully Deleted"}


        
    
  