# 🌌 Starboy  
A full-stack universe exploration app for creating and browsing galaxies, star systems, and planets.

<p align="left">
  <img src="https://img.shields.io/badge/Next.js-15-black" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-green" />
  <img src="https://img.shields.io/badge/PostgreSQL-16-blue" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-orange" />
</p>

Starboy blends **FastAPI + PostgreSQL** on the backend with a **Next.js App Router** frontend to build a smooth world-building / space-exploration experience.

---

## 🚀 Features

- Create & manage **galaxies**, **star systems**, and **planets**
- FastAPI backend with modular routers, schemas, and models
- PostgreSQL relational database for structured space hierarchy
- Next.js frontend with React Server Components
- Clean API for interaction between frontend and backend
- Strong architecture for future expansion (auth, deployment, Docker, etc.)

---

## 📦 Tech Stack

### **Frontend**
- Next.js 15 (App Router)
- React
- TailwindCSS
- Fetch API

### **Backend**
- FastAPI
- SQLAlchemy ORM
- Pydantic models
- PostgreSQL
- Uvicorn (dev server)
- docker (future)

---

## 🛠 Running Locally

### **Docker**

In root directory there is a docker-compose.yml that runs the database, backend, and frontend all at once  
    docker compose -f docker-compose.yml up  
    docker compose -f docker-compose.yml down
  
database container is known as db 
- can access on pgadmin4 using info in the compose file, host is localhost
- or in terminal "psql -h localhost -p 5432 -U postgres -d starboy" with elephant as the password  

backend or server container is known as api  
- runs at http://0.0.0.0:8000  
- use http://0.0.0.0:8000/docs#/ to test endpoints  

frontend container is known as frontend  
- runs at http://localhost:3000  

### **Usage**
 
Hello page: http://localhost:3000/hello  
Start exploring: http://localhost:3000/starboy  

---

## 🗺 Roadmap

- add preloaded db to git, so site can be used with my db
- add env files
- create client pages that use react in frontend
- expand database to include galaxies and moons
- expand database to include more stats/info about planets/stars(systems)/(moons?)
- deploy frontend and backend, methods not decided yet
- search bar for finding specific planets
- find out what is visible in the night sky based on your location and be able to log it (logging means having accounts)

---

## ⭐⭐
created by me natone  
inspired by astronomy, the stars, and building interesting backend systems  
created to learn and experiment with a sql database (postgres) in a fullstack env  
yes the starboy name was inpired by the weeknd album  
