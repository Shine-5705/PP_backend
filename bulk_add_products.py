import requests

# API Endpoint
url = "http://127.0.0.1:5000/products/bulk"

# Product List
products = [
    {
        "name": "Potato Message",
        "price": 200,
        "original_price": 400,
        "currency": "rupees",
        "desc": "Send a custom potato message to anyone in India! Write up to 100 characters.",
        "tags": ["gift", "funny", "message"],
        "images": ["https://example.com/potato-message.png"],
        "type": "1"
    },
    {
        "name": "Teddy Potato Duo",
        "price": 600,
        "original_price": 1000,
        "currency": "rupees",
        "desc": "Celebrate love and creativity with the 'Teddy Potato Duo'! Perfect for quirky and heartfelt gifts.",
        "tags": ["love", "valentine", "gift"],
        "images": ["https://example.com/teddy-potato.png"],
        "type": "1"
    },
    {
        "name": "Valentine's Love Potato Gift Box",
        "price": 750,
        "original_price": 900,
        "currency": "rupees",
        "desc": "Make this Valentine's Day special with a personalized potato and Ferrero Rocher chocolates!",
        "tags": ["valentine", "gift", "love"],
        "images": ["https://example.com/love-potato-box.png"],
        "type": "1"
    },
    {
        "name": "Cowboy Potato Uncle",
        "price": 250,
        "original_price": 500,
        "currency": "rupees",
        "desc": "Meet the Potato Buddies! These cowboy-style potatoes bring humor and charm to any room.",
        "tags": ["funny", "decor", "gift"],
        "images": ["https://example.com/cowboy-potato.png"],
        "type": "1"
    },
    {
        "name": "Potato Love Bundle",
        "price": 350,
        "original_price": 1000,
        "currency": "rupees",
        "desc": "Say 'I love you' in the quirkiest way with our Potato Love Bundle! Cute doodles & heartfelt messages.",
        "tags": ["love", "valentine", "gift"],
        "images": ["https://example.com/love-bundle.png"],
        "type": "1"
    }
]

# Send POST request
response = requests.post(url, json=products)
print(response.json())
