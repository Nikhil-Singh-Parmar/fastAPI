from fastapi import FastAPI
from routes.index import user
app = fastAPI()

app.include_router(user)