# Todo Full Stack Application

A modern, full-stack Todo application built with FastAPI (Backend) and Next.js (Frontend).

## 🚀 Features

- ✅ User Authentication (Sign Up, Sign In, Logout)
- ✅ Create, Read, Update, Delete Todos
- ✅ Mark todos as complete/incomplete
- ✅ Secure JWT-based authentication
- ✅ PostgreSQL database support (Supabase/Neon)
- ✅ Modern, responsive UI

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLModel** - SQL databases in Python with type safety
- **PostgreSQL** - Database (via Supabase or Neon)
- **JWT** - Secure authentication
- **Uvicorn** - ASGI server

### Frontend
- **Next.js 16** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Lucide Icons** - Modern icons

## 📦 Project Structure
```
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core configurations
│   │   ├── models/       # Database models
│   │   └── main.py       # FastAPI application
│   ├── .env              # Environment variables
│   └── requirements.txt  # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── app/          # Next.js pages
│   │   ├── components/   # React components
│   │   └── lib/          # Utilities and API client
│   ├── .env.local        # Frontend environment variables
│   └── package.json      # Node dependencies
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL database (Supabase or Neon account)

### Backend Setup

1. **Navigate to backend directory:**
```bash
   cd backend
```

2. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

3. **Create `.env` file:**
```dotenv
   PROJECT_NAME=Todo API
   BETTER_AUTH_SECRET=your-super-secret-jwt-token
   BETTER_AUTH_URL=http://localhost:3000
   DATABASE_URL=postgresql+asyncpg://user:password@host:port/database
```

4. **Run the backend:**
```bash
   uvicorn app.main:app --reload
```

   Backend will run on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
   cd frontend
```

2. **Install dependencies:**
```bash
   npm install
```

3. **Create `.env.local` file:**
```dotenv
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
   BETTER_AUTH_SECRET=your-super-secret-jwt-token
```

4. **Run the frontend:**
```bash
   npm run dev
```

   Frontend will run on `http://localhost:3000`

## 🗄️ Database Setup

### Using Supabase

1. Create account at [supabase.com](https://supabase.com)
2. Create new project
3. Get connection string:
   - Dashboard → Connect → Session Pooler
   - Copy the URI connection string
4. Add to backend `.env` as `DATABASE_URL`

### Using Neon

1. Create account at [neon.tech](https://neon.tech)
2. Create new project
3. Copy pooled connection string
4. Add to backend `.env` as `DATABASE_URL`

## 🌐 Deployment

### Backend Deployment (Railway/Render)

1. **Railway.app:**
   - Connect GitHub repository
   - Select backend folder
   - Add environment variables
   - Deploy

2. **Environment Variables:**
```
   DATABASE_URL=your-production-database-url
   BETTER_AUTH_SECRET=your-secret-key
   BETTER_AUTH_URL=https://your-frontend-url.vercel.app
```

### Frontend Deployment (Vercel)

1. **Vercel:**
   - Connect GitHub repository
   - Select frontend folder
   - Add environment variables
   - Deploy

2. **Environment Variables:**
```
   NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app/api
   NEXT_PUBLIC_BETTER_AUTH_URL=https://your-frontend-url.vercel.app
   BETTER_AUTH_SECRET=your-secret-key
```

## 📝 API Documentation

Once the backend is running, visit:
```
http://localhost:8000/docs
```

Interactive API documentation (Swagger UI) will be available.

## 🔐 Authentication Flow

1. User signs up with email, name, and password
2. Backend creates user and returns JWT token
3. Frontend stores token in localStorage
4. All subsequent requests include the token in Authorization header
5. Backend validates token for protected routes

## 📱 Usage

1. **Sign Up:** Create a new account
2. **Sign In:** Login with your credentials
3. **Create Todo:** Add new tasks to your list
4. **Complete Todo:** Mark tasks as done
5. **Delete Todo:** Remove completed tasks
6. **Logout:** Securely end your session

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- FastAPI for the amazing backend framework
- Next.js team for the powerful React framework
- Supabase/Neon for database hosting

---

**Made with ❤️ for productive task management**
