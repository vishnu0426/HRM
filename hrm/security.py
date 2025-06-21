"""Simple role-based security utilities."""

from fastapi import Header, HTTPException, status, Depends
from pydantic import BaseModel


class User(BaseModel):
    """Authenticated user representation."""

    username: str = "placeholder"
    role: str = "user"


def get_current_user(x_role: str = Header(default="user")) -> User:
    """Retrieve the current user from the X-Role header."""
    return User(role=x_role)


def admin_required(user: User = Depends(get_current_user)) -> User:
    """Ensure the user has admin or superadmin role."""
    if user.role not in ("admin", "superadmin"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return user


def superadmin_required(user: User = Depends(get_current_user)) -> User:
    """Ensure the user has superadmin role."""
    if user.role != "superadmin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Superadmin privileges required")
    return user
