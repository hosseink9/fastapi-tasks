from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas import ResponseTask, CreateTask
from app.crud import get_tasks, get_task, create_task, update_task, delete_task
from app.database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[ResponseTask])
async def _read(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)


@router.get("/{task_id}", response_model=ResponseTask)
async def _read(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/", response_model=ResponseTask)
async def _create(task: CreateTask, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)


@router.put("/{task_id}", response_model=ResponseTask)
async def _update(task_id: int, task: CreateTask, db: AsyncSession = Depends(get_db)):
    updated_task = await update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}")
async def _delete(task_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
