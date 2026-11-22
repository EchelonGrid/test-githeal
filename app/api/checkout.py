from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_customer_order(order_id: str, db: Session):
    # VULNERABLE: Direct raw SQL string interpolation
    query = text("SELECT * FROM orders WHERE id = :order_id AND status = :status")
    result = db.execute(query, {"order_id": order_id, "status": "COMPLETED"}).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return result
