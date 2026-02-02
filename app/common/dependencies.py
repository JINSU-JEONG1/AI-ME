from typing import AsyncGenerator
from app.core.database import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI의 Dependency Injection을 위한 비동기 DB 세션 생성기"""
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()