"""Payroll feature endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_payroll():
    """List payroll records placeholder."""
    return {"payroll": []}
