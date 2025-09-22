from backend.database import SessionLocal
from backend.models.task import Task

def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "tags": task.tags,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "updated_at": task.updated_at.isoformat() if task.updated_at else None,
    }

def add_task(title, description="", priority="normal", tags=""):
    db = SessionLocal()
    try:
        task = Task(title=title, description=description, priority=priority, tags=tags)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task_to_dict(task)
    finally:
        db.close()

def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(Task).order_by(Task.id.desc()).all()
        return [task_to_dict(t) for t in tasks]
    finally:
        db.close()

def get_task(task_id):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        return task_to_dict(task) if task else None
    finally:
        db.close()

def update_task(task_id, **kwargs):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        for k, v in kwargs.items():
            if hasattr(task, k):
                setattr(task, k, v)
        db.commit()
        db.refresh(task)
        return task_to_dict(task)
    finally:
        db.close()

def delete_task(task_id):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        db.delete(task)
        db.commit()
        return True
    finally:
        db.close()
def mark_task_complete(task_id):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        task.status = "complete"
        db.commit()
        db.refresh(task)
        return task_to_dict(task)
    finally:
        db.close()


def search_tasks(query):
    db = SessionLocal()
    try:
        tasks = db.query(Task).filter(
            (Task.title.ilike(f"%{query}%")) |
            (Task.description.ilike(f"%{query}%"))
        ).all()
        return [task_to_dict(t) for t in tasks]
    finally:
        db.close()
