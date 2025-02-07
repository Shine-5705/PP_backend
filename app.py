from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import uuid

# 🔹 Initialize Firebase
cred = credentials.Certificate("PP_backend\sneakeet-firebase-adminsdk-qdjza-5a140d3551.json")  # Ensure correct path
firebase_admin.initialize_app(cred)

# 🔹 Get Firestore database reference
db = firestore.client()

# 🔹 Initialize Flask
app = Flask(__name__)

# ✅ **1. Fetch Products (User - With Limit)**
@app.route("/products", methods=["GET"])
def get_products():
    limit = request.args.get("limit", default=10, type=int)  # Default limit: 10
    products_ref = db.collection("products").limit(limit).stream()
    products = [{**doc.to_dict(), "id": doc.id} for doc in products_ref]
    return jsonify({"products": products})

# ✅ **2. Fetch All Products (Admin)**
@app.route("/admin/products", methods=["GET"])
def admin_get_products():
    products_ref = db.collection("products").stream()
    products = [{**doc.to_dict(), "id": doc.id} for doc in products_ref]
    return jsonify({"products": products})

# ✅ **3. Fetch a Single Product**
@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    doc_ref = db.collection("products").document(product_id)
    doc = doc_ref.get()
    if doc.exists:
        return jsonify({"product": doc.to_dict()})
    return jsonify({"error": "Product not found"}), 404

# ✅ **4. Add a New Product**
@app.route("/products", methods=["POST"])
def add_product():
    product_data = request.json
    product_id = str(uuid.uuid4())  # Generate a unique product ID
    product_data["date"] = firestore.SERVER_TIMESTAMP  # Set timestamp
    db.collection("products").document(product_id).set(product_data)
    return jsonify({"message": "Product added successfully", "product_id": product_id})

# ✅ **5. Create an Order (Includes User Details)**
@app.route("/orders", methods=["POST"])
def create_order():
    order_data = request.json
    order_id = str(uuid.uuid4())  # Unique order ID
    order_data["date"] = firestore.SERVER_TIMESTAMP  # Timestamp for order
    db.collection("orders").document(order_id).set(order_data)
    return jsonify({"message": "Order created successfully", "order_id": order_id})

# ✅ **6. Fetch All Orders (Admin)**
@app.route("/admin/orders", methods=["GET"])
def get_orders():
    orders_ref = db.collection("orders").stream()
    orders = [{**doc.to_dict(), "id": doc.id} for doc in orders_ref]
    return jsonify({"orders": orders})

@app.route("/products/bulk", methods=["POST"])
def add_multiple_products():
    products_data = request.json  # Expecting a list of products
    if not isinstance(products_data, list):
        return jsonify({"error": "Invalid data format. Expecting a list of products."}), 400

    batch = db.batch()  # Use batch write for efficiency

    product_ids = []
    for product in products_data:
        product_id = str(uuid.uuid4())  # Generate unique ID
        product["date"] = firestore.SERVER_TIMESTAMP  # Add timestamp
        doc_ref = db.collection("products").document(product_id)
        batch.set(doc_ref, product)  # Add to batch
        product_ids.append(product_id)

    batch.commit()  # Execute batch write

    return jsonify({"message": "Products added successfully", "product_ids": product_ids})


# 🔹 Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
