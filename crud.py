from sqlalchemy.orm import Session
import models
import schemas


# Users CRUD
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(first_name=user.first_name, last_name=user.last_name, email=user.email,
                          address=user.address, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db_user.phone_number = user.phone_number
    db_user.address = user.address
    db.commit()
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()


# Workers CRUD
def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()


def get_workers(db: Session):
    return db.query(models.Worker).all()


def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(first_name=worker.first_name, last_name=worker.last_name, email=worker.email,
                              address=worker.address, password=worker.password, phone_number=worker.phone_number)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def update_worker(db: Session, worker: schemas.WorkerCreate, worker_id: int):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    db_worker.first_name = worker.first_name
    db_worker.last_name = worker.last_name
    db_worker.phone_number = worker.phone_number
    db_worker.email = worker.email
    db_worker.address = worker.address
    db_worker.password = worker.password
    db.commit()
    return db_worker


def delete_worker(db: Session, worker_id: int):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    db.delete(db_worker)
    db.commit()


# Calls CRUD
def get_call(db: Session, call_id: int):
    return db.query(models.Call).filter(models.Call.id == call_id).first()


def get_calls(db: Session):
    return db.query(models.Call).all()


def create_call(db: Session, call: schemas.CallCreate):
    db_call = models.Call(duration=call.duration, status=call.status, worker_id=call.worker_id, user_id=call.user_id)
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call


def update_call(db: Session, call: schemas.CallCreate, call_id: int):
    db_call = db.query(models.Call).filter(models.Call.id == call_id).first()
    db_call.duration = call.duration
    db_call.worker_id = call.worker_id
    db_call.user_id = call.user_id
    db_call.status = call.status
    db.commit()
    return db_call


def delete_call(db: Session, call_id: int):
    db_call = db.query(models.Call).filter(models.Call.id == call_id).first()
    db.delete(db_call)
    db.commit()
