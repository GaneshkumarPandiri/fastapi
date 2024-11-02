from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import posts,users,auth,votes
from . import models,config
from .database import engine





# models.Base.metadata.create_all(bind=engine) # to create tables from models if not using alembic

app = FastAPI()
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


    

   

    

 