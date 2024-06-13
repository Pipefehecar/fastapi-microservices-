# FastAPI Car CRUD Project

Welcome to the **FastAPI Car CRUD** project, a modern and efficient application for managing cars, developed with [FastAPI](https://fastapi.tiangolo.com/) and a [PostgreSQL](https://www.postgresql.org/) database. The database can be easily set up using Docker.

## 🚀 Getting Started

### 📋 Requirements

- **Python 3.11.0+**
- **Docker**
- **pipenv** or **virtualenv** (optional but recommended for virtual environment management)

### 🔧 Installation

#### 1. Clone the repository

```rm
git clone https://github.com/Pipefehecar/fastapi-microservices-.git
cd your_repository
```
#### 2. Set up the virtual environment (optional but recommended):
```python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt

```
#### 3. Set up the PostgreSQL database:
Ensure Docker is installed and running, then run the following command to start the PostgreSQL container:
```
docker run -d --name fastapi-car-crud-db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -e POSTGRES_DB=fastapi_car_db -p 5432:5432 postgres:latest

```
#### 4. Install and run the FastAPI application
```
uvicorn app.main:app --reload
```

Now you can now access the FastAPI Car CRUD application at http://localhost:8000.