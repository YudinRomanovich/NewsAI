from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import DATABASE_CONNECTION

class Base(DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_CONNECTION)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Возвращает асинхронную сессию с БД
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

# Инициализация БД
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
