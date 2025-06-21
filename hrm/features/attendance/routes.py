"""Attendance feature endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_attendance():
    """List attendance records placeholder."""
    return {"attendance": []}
