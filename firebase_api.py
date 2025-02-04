from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import uuid

# 🔹 Initialize Firebase
cred = credentials.Certificate("sneakeet-firebase-adminsdk-qdjza-5a140d3551.json")  # Ensure correct path
firebase_admin.initialize_app(cred)

# 🔹 Get Firestore database reference
db = firestore.client()

# 🔹 Initialize Flask
app = Flask(__name__)

# ✅ **1. Fetch All Products**
@app.route("/products", methods=["GET"])
def get_products():
    products_ref = db.collection("products").stream()
    products = [{**doc.to_dict(), "id": doc.id} for doc in products_ref]
    return jsonify({"products": products})

# ✅ **2. Fetch a Single Product**
@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    doc_ref = db.collection("products").document(product_id)
    doc = doc_ref.get()
    if doc.exists:
        return jsonify({"product": doc.to_dict()})
    return jsonify({"error": "Product not found"}), 404

# ✅ **3. Add a New Product**
@app.route("/products", methods=["POST"])
def add_product():
    product_data = request.json
    product_id = str(uuid.uuid4())  # Generate a unique product ID
    product_data["date"] = firestore.SERVER_TIMESTAMP  # Set timestamp
    db.collection("products").document(product_id).set(product_data)
    return jsonify({"message": "Product added successfully", "product_id": product_id})

# ✅ **4. Create an Order**
@app.route("/orders", methods=["POST"])
def create_order():
    order_data = request.json
    order_id = str(uuid.uuid4())  # Unique order ID
    order_data["date"] = firestore.SERVER_TIMESTAMP  # Timestamp for order
    db.collection("orders").document(order_id).set(order_data)
    return jsonify({"message": "Order created successfully", "order_id": order_id})

# ✅ **5. Fetch All Orders**
@app.route("/orders", methods=["GET"])
def get_orders():
    orders_ref = db.collection("orders").stream()
    orders = [{**doc.to_dict(), "id": doc.id} for doc in orders_ref]
    return jsonify({"orders": orders})

# 🔹 Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
