from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import schemas, crud
from app.database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[schemas.ResponseTask])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    return await crud.get_tasks(db)


@router.get("/{task_id}", response_model=schemas.ResponseTask)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/", response_model=schemas.ResponseTask)
async def create_task(task: schemas.CreateTask, db: AsyncSession = Depends(get_db)):
    return await crud.create_task(db, task)


@router.put("/{task_id}", response_model=schemas.ResponseTask)
async def update_task(task_id: int, task: schemas.CreateTask, db: AsyncSession = Depends(get_db)):
    updated_task = await crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
