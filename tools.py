from data import ORDERS_DB, PRODUCTS_DB

def get_order_status(order_id: str) -> str:
    clean_id = order_id.upper().strip()
    order = ORDERS_DB.get(clean_id)
    if order:
        return f"Order ID: {clean_id} | Item: {order['item']} | Status: {order['status']} | Delivery: {order['expected_date']}"
    return f"Order ID '{order_id}' kedaikkala. Please correct ID kudunga."

def search_products(category: str) -> str:
    cat = category.lower().strip()
    items = PRODUCTS_DB.get(cat)
    if not items:
        return f"'{category}' category-la items illa. Available: electronics, fashion."
    
    result = f"Products in {category.capitalize()}:\n\n"
    for item in items:
        stock = "Available" if item['in_stock'] else "Out of Stock"
        result += f"- {item['name']} | Price: {item['price']} | ({stock})\n"
    return result

def initiate_return(order_id: str, reason: str) -> str:
    clean_id = order_id.upper().strip()
    if clean_id in ORDERS_DB:
        return f"Return Request Accepted for Order {clean_id}! Reason: '{reason}'. Pickup within 48 hours."
    return f"Invalid Order ID '{order_id}'. Return process panna mudiyadhu."