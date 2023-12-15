from fastapi import Depends, FastAPI, HTTPException, status
from database import engine
from tickets import models as tickets_models
from tickets import main as tickets_main
from messages import models as messages_models
from messages import main as messages_main
from users import main as users_main
from users import models as users_models 

tickets_models.Base.metadata.create_all(bind=engine)
messages_models.Base.metadata.create_all(bind=engine)
users_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tickets system", description="A tickets system made with FastAPI")

app.include_router(tickets_main.router)
app.include_router(messages_main.router)
app.include_router(users_main.router)

@app.get("/")
async def root():
    return {"message": "backend server is running", "connected_modules": ["tickets", "messages"]}
