import firebase_admin
from firebase_admin import credentials, firestore

# 🔹 Step 1: Initialize Firebase
cred = credentials.Certificate("sneakeet-firebase-adminsdk-qdjza-5a140d3551.json")  # Ensure correct path
firebase_admin.initialize_app(cred)

# 🔹 Step 2: Get Firestore database reference
db = firestore.client()

# 🔹 Step 3: Function to Write Data to Firestore
def write_product():
    product_data = {
        "currency": "rupees",
        "date": firestore.SERVER_TIMESTAMP,
        "desc": "",
        "images": [
            "https://potatoparcel.com/cdn/shop/files/potato-parcel-potato-parcel-30437425053781_800x.png?v=1686049817",
            "https://potatoparcel.com/cdn/shop/files/potato-love-bear-bundle-potato-parcel-30437407391829_800x.png?v=1686049458"
        ],
        "name": "potato love",
        "price": 200,
        "tags": ["love", "gift"],
        "type": "1"
    }

    db.collection("products").document("p1").set(product_data)
    print("✅ Product written successfully!")

# 🔹 Step 4: Function to Read Data from Firestore
def read_product():
    doc_ref = db.collection("products").document("p1")
    doc = doc_ref.get()

    if doc.exists:
        print("✅ Product Data:", doc.to_dict())  # Convert Firestore doc to dictionary
        return doc.to_dict()
    else:
        print("❌ No document found!")

# 🔹 Step 5: Run Functions
if __name__ == "__main__":
    write_product()  # Writes data to Firestore
    read_product()   # Reads data from Firestore
