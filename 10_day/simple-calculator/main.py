
import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True
)

def main():
    st.title("🧮 Beautiful Calculator")
    st.write("Enter two numbers and choose an operation.")

    # Input fields in columns
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

    # Operation selection
    operation = st.selectbox("Select operation", ["➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"])

    # Calculate button
    if st.button("Calculate"):
        try:
            if operation == "➕ Add":
                result = num1 + num2
                symbol = "+"
            elif operation == "➖ Subtract":
                result = num1 - num2
                symbol = "-"
            elif operation == "✖ Multiply":
                result = num1 * num2
                symbol = "×"
            elif operation == "➗ Divide":
                if num2 == 0:
                    st.error("❌ Cannot divide by zero!")
                    return
                result = num1 / num2
                symbol = "÷"

            st.success(f"✅ **Result:** {num1} {symbol} {num2} = `{result:.2f}`")
        
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
