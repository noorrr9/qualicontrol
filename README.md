# QualiControl

REST API for food quality control and batch traceability, built with Django REST Framework and PostgreSQL.

## Stack

Python 3.13 · Django · Django REST Framework · PostgreSQL

## Quick start

```powershell
git clone https://github.com/noorrr9/qualicontrol.git
cd qualicontrol
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

Create the `qualicontrol` database in PostgreSQL first, and set your password in `.env`.

API: `http://127.0.0.1:8000/api/` · Admin: `http://127.0.0.1:8000/admin/`

## Endpoints

Every resource supports full CRUD (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

| Module | Resources |
|--------|-----------|
| Traceability | `/suppliers/` `/raw-materials/` `/lots/` `/batches/` |
| Quality | `/control-limits/` `/samples/` `/measurements/` `/ccps/` `/ccp-monitorings/` `/corrective-actions/` | | Audit | `/audit-logs/`

Reports:

- `GET /batches/<id>/trace/`: lots, suppliers, samples, measurements and CCP checks for a batch, with a conformity summary
- `GET /lots/<id>/trace/`: recall lookup, all batches that used a lot

Measurements and CCP readings are checked against their control limits automatically.

## API testing

Import the Postman collection from [`postman/`](postman/).
