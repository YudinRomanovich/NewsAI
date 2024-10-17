from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update
from auth.base_config import current_user
from user.models import user
from database import get_async_session


router = APIRouter(
    prefix="",
    tags=["User"]
)