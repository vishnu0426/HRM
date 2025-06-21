"""Performance feature endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_performance():
    """List performance records placeholder."""
    return {"performance": []}
