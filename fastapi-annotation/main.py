from fastapi import FastAPI
from services.apis import demo

app = FastAPI(title= "Annotations")

app.include_router(demo)
