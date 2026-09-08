# Dummy Orders Database
ORDERS_DB = {
    "ORD101": {
        "item": "Wireless Headphones",
        "status": "Out for Delivery",
        "expected_date": "Today, 5:00 PM"
    },
    "ORD102": {
        "item": "Mechanical Keyboard",
        "status": "Shipped",
        "expected_date": "Tomorrow"
    },
    "ORD103": {
        "item": "Fitness Smartwatch",
        "status": "Delivered",
        "expected_date": "Yesterday"
    }
}

# Dummy Products Catalog
PRODUCTS_DB = {
    "electronics": [
        {"name": "Wireless Mouse", "price": "Rs. 699", "in_stock": True},
        {"name": "Fast Charger 65W", "price": "Rs. 999", "in_stock": True},
        {"name": "Gaming Keyboard", "price": "Rs. 1,899", "in_stock": False}
    ],
    "fashion": [
        {"name": "Cotton T-Shirt", "price": "Rs. 499", "in_stock": True},
        {"name": "Running Shoes", "price": "Rs. 1,499", "in_stock": True}
    ]
}