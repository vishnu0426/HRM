"""Superadmin feature endpoints."""

from fastapi import APIRouter, Depends

from ...security import superadmin_required, User

router = APIRouter()


@router.get("/dashboard")
async def superadmin_dashboard(current_user: User = Depends(superadmin_required)):
    """Simple superadmin dashboard placeholder."""
    return {"message": "Superadmin dashboard"}
