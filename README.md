# QualiControl

# QualiControl

Food quality control and traceability system. Backend API built with Django, Django REST Framework and PostgreSQL.

## Features

- Supplier management (list and create) through a REST API
- PostgreSQL database
- Planned: raw materials, lots, batches, samples, measurements, CCP monitoring, corrective actions, audit log

## Tech stack

- Python 
- Django + Django REST Framework
- PostgreSQL

## Project structure

```
config/          Django settings and main routing
traceability/    Suppliers app (models, serializers, views, urls)
postman/         Postman collection
requirements.txt Python dependencies
.env.example     Template for environment variables
```
