from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import user, product, task


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(product.router)
app.include_router(task.router)


@app.get("/")
def read_root():
    return {"Welcome": "jobs-data-assignment-samson-samuel"}


app.mount('/api/v1', app)
