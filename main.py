from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from starlette.responses import Response

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# User endpoints
@app.get('/api/users/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get('/api/users', response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@app.post('/api/users', response_model=schemas.User, status_code=HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.put('/api/users/{user_id}', response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)


@app.delete('/api/users/{user_id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)


# Workers endpoints
@app.get('/api/workers/{worker_id}', response_model=schemas.Worker)
def get_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker


@app.get('/api/workers', response_model=List[schemas.Worker], response_model_exclude={'password'})
def get_workers(db: Session = Depends(get_db)):
    return crud.get_workers(db=db)


@app.post('/api/workers', response_model=schemas.Worker, response_model_exclude={'password'},
          status_code=HTTP_201_CREATED)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db=db, worker=worker)


@app.put('/api/workers/{worker_id}', response_model=schemas.Worker)
def update_user(worker_id: int, worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.update_worker(db=db, worker_id=worker_id, worker=worker)


@app.delete('/api/workers/{worker_id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(worker_id: int, db: Session = Depends(get_db)):
    crud.delete_worker(db=db, worker_id=worker_id)


# Calls endpoints
@app.get('/api/calls/{call_id}', response_model=schemas.Call)
def get_call(call_id: int, db: Session = Depends(get_db)):
    db_call = crud.get_call(db, call_id=call_id)
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call


@app.get('/api/calls', response_model=List[schemas.Call])
def get_calls(db: Session = Depends(get_db)):
    return crud.get_calls(db=db)


@app.post('/api/calls', response_model=schemas.Call, status_code=HTTP_201_CREATED)
def create_call(call: schemas.CallCreate, db: Session = Depends(get_db)):
    return crud.create_call(db=db, call=call)


@app.put('/api/calls/{call_id}', response_model=schemas.Call)
def update_user(call_id: int, call: schemas.CallCreate, db: Session = Depends(get_db)):
    return crud.update_call(db=db, call_id=call_id, call=call)


@app.delete('/api/calls/{call_id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(call_id: int, db: Session = Depends(get_db)):
    crud.delete_call(db=db, call_id=call_id)
