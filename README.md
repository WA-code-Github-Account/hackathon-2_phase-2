---
title: Todo Backend API
emoji: 📝
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Todo Backend API

A modern FastAPI backend for Todo application with JWT authentication and PostgreSQL support.

## 🚀 Features

- ✅ User Authentication (Sign Up, Sign In, Logout)
- ✅ RESTful API for Todo CRUD operations
- ✅ Secure JWT-based authentication
- ✅ PostgreSQL database support (Supabase/Neon)
- ✅ Async/await for better performance
- ✅ Interactive API documentation (Swagger UI)

## 🛠️ Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLModel** - SQL databases with type safety
- **PostgreSQL** - Database (via Supabase or Neon)
- **JWT** - Secure token-based authentication
- **Uvicorn** - ASGI server

## 📝 API Documentation

Once deployed, visit `/docs` for interactive Swagger UI documentation.

## 🔐 Authentication

All protected endpoints require JWT token in Authorization header:
```
Authorization: Bearer <your-token>
```

## 🌐 Deployment

This Space is deployed on Hugging Face using Docker SDK.

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- Hugging Face for hosting
