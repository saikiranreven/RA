from google.cloud import firestore
db = firestore.Client()

def get_all_products():
    return [doc.to_dict() for doc in db.collection("products").stream()]

def get_product_by_id(pid):
    snap = db.collection("products").document(pid).get()
    return snap.to_dict() if snap.exists else None