from fastapi import FastAPI
import uvicorn
from app.routers import notifications, users, groups

app = FastAPI()
app.include_router(users.router)
app.include_router(groups.router)
app.include_router(notifications.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
