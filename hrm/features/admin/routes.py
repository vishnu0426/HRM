"""Admin feature endpoints."""

from fastapi import APIRouter, Depends

from ...security import admin_required, User

router = APIRouter()


@router.get("/dashboard")
async def admin_dashboard(current_user: User = Depends(admin_required)):
    """Simple admin dashboard placeholder."""
    return {"message": f"Admin dashboard for {current_user.role}"}
