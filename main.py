from fastapi import FastAPI 
from routers import user, shop

app = FastAPI(title="api")

app.include_router(user.router)
app.include_router(shop.router)

