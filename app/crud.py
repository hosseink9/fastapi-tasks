from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Task
from app.schemas import CreateTask


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()


async def create_task(db: AsyncSession, task: CreateTask):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def update_task(db: AsyncSession, task_id: int, task: CreateTask):
    db_task = await get_task(db, task_id)
    if not db_task:
        return None
    for key, value in task.model_dump().items():
        setattr(db_task, key, value)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def delete_task(db: AsyncSession, task_id: int):
    db_task = await get_task(db, task_id)
    if not db_task:
        return None
    await db.delete(db_task)
    await db.commit()
    return db_task
