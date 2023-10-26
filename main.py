from app import create_app
from app.controllers import api_controller
from pydantic import BaseModel

app = create_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/payment/{id}")
def get_payment(id: int):
    return api_controller.get_payment(id)


class CustomerStatus(BaseModel):
    email: str
    active: bool

@app.post("/api/customer")
def set_customer_status(data: CustomerStatus):
    return api_controller.set_customer_status(data.email, data.active)
