from google.cloud import firestore
from datetime import datetime, timezone

db = firestore.Client()

def create_order(user_id: str, product_id: str, quantity: int):
    db.collection("orders").add({
        "user_id":    user_id,
        "product_id": product_id,
        "quantity":   quantity,
        "status":     "pending",
        "timestamp":  datetime.now(timezone.utc)
    })