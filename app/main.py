from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base
from app.routers.tasks import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(task_router)
