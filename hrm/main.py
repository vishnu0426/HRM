"""Main FastAPI application."""

from fastapi import FastAPI

from .features.employees.routes import router as employees_router
from .features.payroll.routes import router as payroll_router
from .features.attendance.routes import router as attendance_router
from .features.performance.routes import router as performance_router
from .features.admin.routes import router as admin_router
from .features.superadmin.routes import router as superadmin_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI app."""
    app = FastAPI(title="HRM")
    app.include_router(employees_router, prefix="/employees")
    app.include_router(payroll_router, prefix="/payroll")
    app.include_router(attendance_router, prefix="/attendance")
    app.include_router(performance_router, prefix="/performance")
    app.include_router(admin_router, prefix="/admin")
    app.include_router(superadmin_router, prefix="/superadmin")
    return app


app = create_app()
