import firebase_admin
from firebase_admin import credentials, firestore
import uuid  # To generate unique product IDs

# 🔹 Initialize Firebase
cred = credentials.Certificate("sneakeet-firebase-adminsdk-qdjza-5a140d3551.json")  # Ensure correct path
firebase_admin.initialize_app(cred)

# 🔹 Get Firestore database reference
db = firestore.client()

# 🔹 Function to Add a New Product
def add_product(product_data, product_id=None):
    if not product_id:
        product_id = str(uuid.uuid4())  # Generate a unique ID for the product
    
    db.collection("products").document(product_id).set(product_data)
    print(f"✅ New Product Added with ID: {product_id}")

# 🔹 Function to Read All Products from Firestore
def read_all_products():
    products_ref = db.collection("products").stream()
    print("\n📦 All Products in Firestore:")
    for doc in products_ref:
        print(f"🆔 {doc.id} ➝ {doc.to_dict()}")

# 🔹 Example: Adding a New Product
new_product = {
    "currency": "rupees",
    "date": firestore.SERVER_TIMESTAMP,
    "desc": "Special Valentine's edition potato",
    "images": [
        "https://example.com/potato1.png",
        "https://example.com/potato2.png"
    ],
    "name": "Valentine Potato",
    "price": 250,
    "tags": ["valentine", "gift", "love"],
    "type": "2"
}

# 🔹 Run the Functions
if __name__ == "__main__":
    add_product(new_product)  # Adds a new product
    read_all_products()       # Reads all products
