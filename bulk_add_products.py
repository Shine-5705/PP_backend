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
        "images": ["https://phelapyar.com/cdn/shop/files/potato-parcel-potato-parcel-28352980353109_5000x_1_40c8a7ec-4a79-4e14-99c0-5e4a81defc71.jpg?v=1737655618&width=823" , "https://phelapyar.com/cdn/shop/files/potato-parcel-potato-parcel-30360035393621_5000x_107bd867-b7af-4176-989d-d386370bd0e1.png?v=1737655618&width=246"],
        "type": "1"
    },  
    {
        "n  ame": "Teddy Potato Duo",
        "price": 600,
        "original_price": 1000,
        "currency": "rupees",
        "desc": "Celebrate love and creativity with the 'Teddy Potato Duo'! Perfect for quirky and heartfelt gifts.",
        "tags": ["love", "valentine", "gift"],
        "images": ["https://i.ibb.co/XrgtcRLL/2.png" , "https://i.ibb.co/wZnwzm7y/1.png"],
        "type": "1"
    },
    {
        "name": "Valentine's Love Potato Gift Box",
        "price": 750,
        "original_price": 900,
        "currency": "rupees",
        "desc": "Make this Valentine's Day special with a personalized potato and Ferrero Rocher chocolates!",
        "tags": ["valentine", "gift", "love"],
        "images": ["https://i.ibb.co/BHWNrM4B/ferraror-potato.webp","https://i.ibb.co/BHWNrM4B/ferraror-potato.webp"],
        "type": "1"
    },
    {
        "name": "Cowboy Potato Uncle",
        "price": 250,
        "original_price": 500,
        "currency": "rupees",
        "desc": "Meet the Potato Buddies! These cowboy-style potatoes bring humor and charm to any room.",
        "tags": ["funny", "decor", "gift"],
        "images": ["https://i.ibb.co/FLPZjGsR/girl-with-cowboy.webp","https://i.ibb.co/dwC1C9px/Screenshot-2025-01-23-233730.png"],
        "type": "1"
    },
    {
        "name": "Potato Love Bundle",
        "price": 350,
        "original_price": 1000,
        "currency": "rupees",
        "desc": "Say 'I love you' in the quirkiest way with our Potato Love Bundle! Cute doodles & heartfelt messages.",
        "tags": ["love", "valentine", "gift"],
        "images": ["https://i.ibb.co/kVjYcLCw/potato-Ilvu.webp","https://i.ibb.co/gZCsrqqX/bundlepotato.png"],
        "type": "1"
    }
]

# Send POST request
response = requests.post(url, json=products)
print(response.json())
