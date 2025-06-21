# HRM

A minimal Human Resource Management (HRM) skeleton using **FastAPI** and **PostgreSQL**.

## Structure

- `hrm/` – main package
  - `main.py` – FastAPI application entry point
  - `database.py` – SQLAlchemy session and engine
  - `config.py` – application settings
  - `features/` – individual feature modules
    - `employees/`
    - `payroll/`
    - `attendance/`
    - `performance/`
    - `admin/` – admin dashboard
    - `superadmin/` – superadmin dashboard
  - `ai/` – placeholder for AI utilities

## Running

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn hrm.main:app --reload
```

The application currently exposes placeholder endpoints for each feature.

### Role Simulation

Use the `X-Role` HTTP header to simulate different user roles when calling the
API. Supported roles are `user`, `admin`, and `superadmin`.
