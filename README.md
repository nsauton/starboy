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

### **Frontend**

In frontend directory run  
    npm install  
    npm run dev  

runs at http://localhost:3000

---

## 🗺 Roadmap

- add tailwind css
- create client pages that use react in frontend
- use dockerfile for the backend
- expand database to include galaxies and moons
- add more backend routes to make data retrieval more efficient
- deploy frontend and backend, methods not decided yet

---

## ⭐⭐
created by me natone  
inspired by astronomy, the stars, and building interesting backend systems  
name was inpired by the weeknd album starboy  
created to learn more a sql db (postgres) in a fullstack env 
