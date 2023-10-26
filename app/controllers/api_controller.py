from app.models.model import Payment, Customer
from app.database import SessionLocal
from fastapi import HTTPException

session = SessionLocal()

def get_payment(id):
    res = session.query(Payment).filter_by(payment_id=id).first()
    return res


def set_customer_status(email, active):
    matched = False
    for row in session.query(Customer).filter_by(email=email).all():
        row.active = active
        matched = True
    if not matched:
        raise HTTPException(status_code=404, detail="Email not found")
    session.commit()
