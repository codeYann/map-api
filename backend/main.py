from fastapi import FastAPI
from api.routes import router as routes

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(routes)
