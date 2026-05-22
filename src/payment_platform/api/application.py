from fastapi import FastAPI
from payment_platform.api.routers import routers

def create_app():
  app = FastAPI()

  for router in routers:
    app.include_router(router)
  
  return app