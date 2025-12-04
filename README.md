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

### **Database**

make sure empty database called starboy exists in postgres, then backend can be ran to make the tables  
to mess with db either use pgadmin4 or run the following command in terminal:  
    psql -U postgres -d starboy

### **Backend**

In backend directory run  
    uvicorn main:app --reload

runs at http://localhost:8000  
use http://localhost:8000/docs#/ to test endpoints  

### **Frontend**

In frontend directory run  
    npm install  
    npm run dev  

runs at http://localhost:3000

### **Usage**

Hello page: http://localhost:3000/hello  
Start exploring: http://localhost:3000/starboy  

---

## 🗺 Roadmap

- add tailwind css
- create client pages that use react in frontend
- change/add backend routes to make data retrieval more efficient
- use dockerfile for the backend
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
the starboy name was inpired by the weeknd album  
