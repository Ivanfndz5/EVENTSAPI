from fastapi import FastAPI
from app.routers import user_router, event_router, ticket_router, purchase_router, auth_router
from app.core.database import Base, engine
import logging

logging.basicConfig(level=logging.DEBUG)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)
app.include_router(event_router.router)
app.include_router(ticket_router.router)
app.include_router(purchase_router.router)
app.include_router(auth_router.router)






