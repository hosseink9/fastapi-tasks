# 📝 FastAPI Tasks API

A full-featured **task management API** built with [FastAPI](https://fastapi.tiangolo.com/), [PostgreSQL](https://www.postgresql.org/), and [SQLAlchemy](https://www.sqlalchemy.org/), supporting both synchronous and asynchronous operations. It comes Docker-ready for easy deployment and also supports manual running using Uvicorn.

---

## 📌 Features

- 🚀 FastAPI-powered high-performance web framework
- 🗃️ PostgreSQL for robust data persistence
- 🔄 Async support with `asyncpg` and `SQLAlchemy`
- 🔒 Environment-based configuration
- 📄 Swagger and ReDoc auto-generated API docs
- 🐳 Docker support for containerized deployment
- ♻️ Modular code structure (CRUD, schemas, DB, routes)

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI app entry
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic models
│   ├── crud.py              # CRUD operations
│   ├── database.py          # DB connection and session
│   ├── config.py
│   └── routers/
│       └── tasks.py           # Environment config loader
├── .env                     # Environment variables
├── Dockerfile               # Image build instructions
├── docker-compose.yml       # Multi-container setup
├── requirements.txt         # Pip dependencies (if not using poetry)
├── README.md                # Project documentation
```

---

## 🧰 Requirements (If Running Without Docker)

- Python 3.10+
- PostgreSQL 13+
- `pip` or [Poetry](https://python-poetry.org/)
- (optional) [virtualenv](https://virtualenv.pypa.io/en/latest/)

---

## ⚙️ Environment Variables

All configuration is handled through the `.env` file. Example:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi-tasks
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/fastapi-tasks
```

> 🔐 Make sure not to expose your `.env` file publicly.

---

## 🐳 Running with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-tasks.git
cd fastapi-tasks
```

### 2. Configure `.env`

```env
DATABASE_HOST=db
DATABASE_PORT=5432
DATABASE_NAME=fastapi-tasks
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@db:5432/fastapi-tasks
```

### 3. Start Docker Containers

```bash
docker-compose up --build
```

### 4. Access the Application

- API Docs: [http://localhost/docs](http://localhost/docs)
- Redoc: [http://localhost/redoc](http://localhost/redoc)
- App (via Nginx): [http://localhost](http://localhost)

### 5. Stop Containers

```bash
docker-compose down
```

---

## ⚡ Running Locally (Without Docker)

### 1. Setup Python Environment

```bash
python -m venv venv
source venv/bin/activate
```

Or with Poetry:

```bash
poetry install
poetry shell
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup `.env`

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi-tasks
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/fastapi-tasks
```

### 4. Ensure PostgreSQL is Running

Check status:

```bash
sudo systemctl status postgresql
```

Or start it manually:

```bash
sudo systemctl start postgresql
```

### 5. Create the Database

```bash
createdb -U postgres fastapi-tasks
```

### 6. Run the App with Uvicorn

```bash
uvicorn app.main:app --reload
```

Visit:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔧 Useful Commands

### Docker

```bash
docker-compose build
docker-compose up
docker-compose down
```

### Local DB (PostgreSQL)

```bash
sudo systemctl start postgresql
sudo -u postgres psql
```

### Uvicorn (local dev)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🧪 Example API Endpoints

- `GET /tasks/` – List all tasks
- `POST /tasks/` – Create a new task
- `GET /tasks/{id}` – Retrieve task by ID
- `PUT /tasks/{id}` – Update task
- `DELETE /tasks/{id}` – Delete task

---

## 🧾 License

MIT License

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Feel free to fork this project and improve it.
