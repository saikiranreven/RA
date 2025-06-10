import datetime
from google.cloud import firestore

db = firestore.Client()

def create_order(user_id, product_id, quantity):
    doc_ref = db.collection("orders").document()
    doc_ref.set({
        "order_id": doc_ref.id,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "pending",
        "timestamp": datetime.datetime.now().isoformat()
    })

def get_user_orders(user_id):
    docs = db.collection("orders").where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]