# import streamlit as st
# import random
# import string

# def generate_password(length, use_digits, use_special):
#     characters = string.ascii_letters
#     if use_digits:
#         characters += string.digits # adding numbeer from (0-9)
    
#     if use_special:
#         characters += string.punctuation # for adding special charactors
    
#     return ''.join(random.choice(characters)for _ in range(length)) #* '_' is used when you don,t know the actual lenght of a list




# st.title('Password Generator')
# length = st.slider('Passworrd Length', min_value=6, max_value=50, value=12 )

# use_digits = st.checkbox('Include Digits')
# use_special = st.checkbox('Include Special Charactor')

# if st.button('Generate Password'):
#     pasword = generate_password(length, use_digits, use_special)
#     st.write(f'Generated Password: `{pasword}` ')
    
# st.write('-------------------------------------')
# st.write('Made with ❤️ by [Mohsin]("https://github.com/Mohsin897")')
import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits  # Adding numbers (0-9)
    if use_special:
        characters += string.punctuation  # Adding special characters
    
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI enhancements
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            width: 100%;
        }
        .stSlider, .stCheckbox {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# UI elements
st.title("🔐 Secure Password Generator")
st.subheader("Generate strong passwords instantly!")

length = st.slider("🔢 Password Length", min_value=6, max_value=50, value=12)
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("🔣 Include Special Characters")

# Generate button
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("✅ Password Generated!")
    st.code(password, language="python")

    # Copy to Clipboard Button
    st.button("📋 Copy to Clipboard", key="copy_button")

# Footer
st.write("---")
st.write("Made with ❤️ by [Mohsin](https://github.com/Mohsin-ali897)")

