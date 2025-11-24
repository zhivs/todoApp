from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

from . import models, database, schema

app = FastAPI(title='ToDO API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Можно создать таблицу (если она не была создана до этого)

#models.Base.metadata.create_all(bind=database.engine)

@app.get("/todos", response_model=List[schema.Todo])
def read_todos(db: Session = Depends(database.get_db)):
    return db.query(models.Todo).all()

@app.post("/todos")
def create_todo(todo: schema.TodoCreate, db: Session = Depends(database.get_db)):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo