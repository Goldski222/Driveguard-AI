from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import config, history, ai

app = FastAPI(title="Pharma Safety HMI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(config.router, prefix="/config", tags=["config"])
app.include_router(history.router, prefix="/history", tags=["history"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])
