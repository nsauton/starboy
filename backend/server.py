from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

#cors middleware so frontend can access this
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_URL = "postgresql://postgres@localhost:5432/myapp"
engine = create_engine(DB_URL)

@app.get("/")
def root():
    return{"message": "hello from the fastapi server!"}

@app.get("/planets")
def get_all_planets():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM planets;"))
        planets = [dict(row) for row in result.mappings()]
    return planets or {"error": "planets not found"}

@app.get("/planets/{id}")
def get_planet(id: str):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM planets WHERE id = :id;"), 
                              {"id": id}
                              ).mappings().first()
    return result or {"error": "planet not found"}
