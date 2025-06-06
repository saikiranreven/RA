from google.cloud import firestore
from datetime import datetime, timezone

def create_order(user_id, product_id, quantity):
    db = firestore.Client()
    db.collection('orders').add({
        'user_id': user_id,
        'product_id': product_id,
        'quantity': quantity,
        'status': 'pending',
        'timestamp': datetime.now(timezone.utc)
    })