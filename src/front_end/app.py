import streamlit as st
import requests
from typing import Dict, Any
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fastAPI.main import app

def create_coffee_order_app():
    st.set_page_config(
        page_title="Coffee Order System",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Main UI Elements
    st.title("☕ Coffee Order System")
    
    # Display available coffees
    if st.button("Show Available Coffees"):
        try:
            response = requests.get("http://localhost:8000/coffees")
            if response.status_code == 200:
                st.json(response.json())
        except Exception as e:
            st.error(f"Failed to fetch coffee menu: {str(e)}")
    
    # Order input section
    with st.container():
        st.subheader("Place Your Order")
        order_input = st.text_input(
            "What would you like to order?",
            placeholder="e.g., large flat white with 2 sugars"
        )

        col1, col2 = st.columns([1, 2])
        with col1:
            submit_button = st.button("Place Order", type="primary")

    # Order processing
    if submit_button and order_input:
        with st.spinner("Processing your order..."):
            try:
                response = process_order(order_input)
                display_order_result(response)
            except Exception as e:
                st.error(f"Failed to process order: {str(e)}")

def process_order(order: str) -> Dict[str, Any]:
    """Process the coffee order through the backend API"""
    response = requests.post(
        "http://localhost:8000/order",
        json={"order_text": order}
    )
    if response.status_code != 200:
        raise Exception(f"API returned status code {response.status_code}")
    return response.json()

def display_order_result(result: Dict[str, Any]):
    """Display the processed order details"""
    st.success("Order processed successfully!")
    
    with st.container():
        st.subheader("Order Details")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Size", result.get("size", "N/A"))
            st.metric("Menu Item", result.get("menu_item", "N/A"))
        
        with col2:
            st.metric("Menu Number", f"#{result.get('menu_number', 'N/A')}")
            if result.get("modifications"):
                st.write("Modifications:", ", ".join(result["modifications"]))

if __name__ == "__main__":
    create_coffee_order_app()
