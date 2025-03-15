# import streamlit as st
# import requests

# def get_joke():
#     '''Function to get a random joke from the API'''
#     try:
#         response = requests.get("https://official-joke-api.appspot.com/jokes/random")
#         if response.status_code == 200:    
#             joke = response.json()
#             return f"{joke['setup']} \n\n {joke['punchline']}"
#         else:
#             return 'Failed to get joke'
#     except Exception as e:
#         return f"An error occurred: {e}"
# def main():
#     st.title("Random Joke Generator")
#     st.write('Click the button below to get a random joke')
#     if st.button("Get Joke"):
#         joke = get_joke()
#         st.success(joke)
#     st.markdown('<div class=" height:200px; width:200px; background-color:lightblue; text-align:center; padding:10px; margin:10px; border-radius:10px;"><h1>Random Joke Generator</h1></div>', unsafe_allow_html=True)
# if __name__ == "__main__":
#     main()
import streamlit as st
import requests

def get_joke():
    '''Function to get a random joke from the API'''
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        if response.status_code == 200:    
            joke = response.json()
            return f"**{joke['setup']}** <br><br> <b style='color:#2E86C1;'>{joke['punchline']}</b>"
        else:
            return 'Failed to get joke'
    except Exception as e:
        return f"An error occurred: {e}"

# UI Enhancements
def main():
    st.markdown(
        """
        <style>
            .title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #2E86C1;
            }
            .container {
                background-color: #F4F6F7;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                width: 80%;
                margin: auto;
                font-size: 20px;
                font-weight: bold;
                color: black;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">😂 Random Joke Generator</h1>', unsafe_allow_html=True)

    st.write('Click the button below to get a random joke')

    if st.button("Get Joke", use_container_width=True):
        joke = get_joke()
        st.markdown(f'<div class="container">{joke}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

