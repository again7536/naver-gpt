from typing import Union

from fastapi import FastAPI

from controller.test_controller import TestController

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

test_controller = TestController()
app.include_router(router=test_controller.router)