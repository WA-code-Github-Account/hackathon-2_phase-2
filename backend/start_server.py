from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=False,  # Disable reload to avoid potential issues
        log_level="info"
    )