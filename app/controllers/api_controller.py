from app.models.model import Payment, Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_payment(db, id):
    res = db.query(Payment).filter_by(payment_id=id).first()
    return res


def set_customer_status(db, email, active):
    for row in db.query(Customer).filter_by(email=email).all():
        row.active = active
    db.commit()
