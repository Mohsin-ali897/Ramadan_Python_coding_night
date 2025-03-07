import streamlit as st
import random
import time
import requests

#? Setting Page Config
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="centered")

#? Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f7fa;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #ff2020;
        }
        .stSuccess {
            background-color: #28a745;
            color: white;
            font-size: 18px;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
        }
        .stInfo {
            background-color: #17a2b8;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#? Application Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>💸 Money Making Machine 💸</h1>", unsafe_allow_html=True)

#? Money Generator Function
def generate_money():
    return random.randint(1, 1000)

#? Layout with Columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h3 style='text-align: center;'>💰 Instant Cash Generator 💰</h3>", unsafe_allow_html=True)

    if st.button("Generate Money 💵"):
        with st.spinner("Counting Your Money... 💰"):
            time.sleep(3)
            amount = generate_money()
        st.success(f"💵 You made ${amount} at {time.strftime('%Y-%m-%d %H:%M:%S')}! 🎉")

#? Fetch Money Quotes
def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            return response.json()["money_quotes"]
        else:
            return "💡 'Too many people spend money they haven’t earned, to buy things they don’t want, to impress people they don’t like.' – Will Rogers"
    except:
        return "⚠️ Something went wrong! Try again later."

st.markdown("---")  # Adds a horizontal line

st.markdown("<h3 style='text-align: center;'>📜 Money Quotes</h3>", unsafe_allow_html=True)
if st.button("Generate Money Quotes 💬"):
    quote = fetch_money_quotes()
    st.success(f"💡 {quote}")

#? Fetch Side Hustle Ideas
def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apikey=1234567890")
        if response.status_code == 200:
            return response.json()["side_hustles"]
        else:
            return "🔎 No side hustle ideas found. Try again!"
    except:
        return "⚠️ Something went wrong! Try again later."

st.markdown("---")  # Adds a horizontal line

st.markdown("<h3 style='text-align: center;'>🚀 Side Hustle Ideas</h3>", unsafe_allow_html=True)
if st.button("Generate Side Hustle Idea 💡"):
    idea = fetch_side_hustles()
    st.info(f"🚀 {idea}")
