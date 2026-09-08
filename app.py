import streamlit as st
import re
from tools import get_order_status, search_products, initiate_return

st.set_page_config(page_title="AI E-Commerce Assistant", page_icon="🛍️")
st.title("🛍️ E-Commerce Support Agent")

# Memory State Setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory_order_id" not in st.session_state:
    st.session_state.memory_order_id = None

# Custom Agent Logic
def run_agent(user_text: str) -> str:
    text = user_text.strip()
    lower_text = text.lower()

    # 1. Flexible Order ID Extraction (ORD followed by numbers)
    match = re.search(r"ord\s*[-_]?\s*(\d+)", lower_text)
    if match:
        st.session_state.memory_order_id = f"ORD{match.group(1)}"

    active_order_id = st.session_state.memory_order_id

    # 2. Return / Refund Action
    if any(k in lower_text for k in ["return", "refund", "replace", "damage"]):
        if not active_order_id:
            return "Kandippa return process panren. Ungaloda Order ID (e.g., ORD101) solla mudiyuma?"
        return initiate_return(active_order_id, user_text)

    # 3. Order Tracking Action
    if any(k in lower_text for k in ["order", "status", "track", "delivery", "where", "check"]) or active_order_id:
        if active_order_id and any(k in lower_text for k in ["status", "track", "delivery", "check", "order", "ord"]):
            return get_order_status(active_order_id)
        elif not active_order_id:
            return "Unga order status track panna, please Order ID provide pannunga (e.g., ORD101)."

    # 4. Product Search Action
    if any(k in lower_text for k in ["product", "buy", "item", "catalog", "price", "show"]):
        if "fashion" in lower_text or any(w in lower_text for w in ["shirt", "shoe", "dress"]):
            return search_products("fashion")
        else:
            return search_products("electronics")

    # 5. Greeting
    if any(k in lower_text for k in ["hi", "hello", "vanakkam", "hey"]):
        return "Vanakkam! Naan unga support assistant. Order status, returns, alladhu product search-ku udhava mudiyum."

    return "Puriyavillai. Ungalukku order track pannanuma, product search pannanuma, alladhu return pannanuma?"

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = run_agent(user_input)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})