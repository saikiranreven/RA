from google.cloud import firestore
from datetime import datetime, timezone
db = firestore.Client()

def create_order(user_id, product_id, quantity):
    doc_ref = db.collection("orders").document()
    doc_ref.set({
        "order_id":  doc_ref.id,
        "user_id":   user_id,
        "product_id":product_id,
        "quantity":  int(quantity),
        "status":    "pending",
        "timestamp": datetime.now(timezone.utc)
    })
    return doc_ref.id  

def get_user_orders(user_id):
    return [
        d.to_dict()
        for d in db.collection("orders")
                  .where("user_id", "==", user_id)
                  .order_by("timestamp", direction=firestore.Query.DESCENDING)
                  .stream()
    ]