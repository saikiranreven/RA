from google.cloud import firestore
from datetime import datetime, timezone

db = firestore.Client()

def create_order(user_id, product_id, quantity):
    quantity = int(quantity)

    # Step 1: Check inventory
    inv_ref = db.collection("inventory").document(product_id)
    inv_doc = inv_ref.get()

    if not inv_doc.exists:
        raise ValueError("Product not found in inventory.")

    inv_data = inv_doc.to_dict()
    current_qty = int(inv_data.get("quantity", 0))

    if quantity > current_qty:
        raise ValueError("Insufficient stock available.")

    # Step 2: Deduct inventory
    new_qty = current_qty - quantity
    inv_ref.update({"quantity": new_qty})

    # Step 3: Create order
    order_ref = db.collection("orders").document()
    order_ref.set({
        "order_id": order_ref.id,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "pending",
        "timestamp": datetime.now(timezone.utc)
    })

    return order_ref.id

def get_user_orders(user_id):
    return [
        d.to_dict()
        for d in db.collection("orders")
                  .where("user_id", "==", user_id)
                  .order_by("timestamp", direction=firestore.Query.DESCENDING)
                  .stream()
    ]
