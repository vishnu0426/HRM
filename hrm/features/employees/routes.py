"""Employee feature endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_employees():
    """List employees placeholder."""
    return {"employees": []}
