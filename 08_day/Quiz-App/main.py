# import streamlit as st
# import random
# import time
# st.title('Quiz App') 
# questions = [
#     {
#         "question": "What is the capital of pakistan?",
#         'options': ['Karachi', 'Islamabad', 'Lahore', 'Quetta'],
#         'answer': 'Islamabad'
#     },
#     {
#         "question": 'Who is the founder of Pakistan?',
#         'options': ['Quaid-e-Azam', 'Allama Iqbal', 'Liaquat Ali Khan', 'Zulfiqar Ali Bhutto'],
#         'answer': 'Quaid-e-Azam'
#     },
#     {
#         "question": "Which city is known as the city of lights?",
#         'options': ['Karachi', 'Islamabad', 'Lahore', 'Quetta'],
#         'answer': 'Karachi'
#     },
#     {
#         "question": "What is the capital of India?",
#         'options': ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata'],
#         'answer': 'Delhi'
#     },
#     {
#         "question": "What is the capital of USA?",
#         'options': ['Washington DC', 'New York', 'Los Angeles', 'Chicago'],
#         'answer': 'Washington DC'
#     },
#     {
#         "question": "What is the capital of UK?",
#         'options': ['Manchester', 'Liverpool', 'London', 'Birmingham'],
#         'answer': 'London'
#     }
# ]
# if 'current_question' not in st.session_state:
#     st.session_state.current_question = random.choice(questions)
# question = st.session_state.current_question
# st.subheader(f'Q. {question["question"]}')
# selected_option = st.selectbox('Select an option', question['options'], key='answer')
# if st.button('Submit'):
#     if selected_option == question['answer']:
#         st.success('Correct Answer')
#     else:
#         st.error(f'Incorrect  Correct Answer is:  + {question['answer']}')
#     time.sleep(2)
    
#     st.session_state.current_question = random.choice(questions)
#     st.rerun()

import streamlit as st
import random
import time

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .title {
            text-align: center;
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with styling
st.markdown("<h1 class='title'>🌟 Quiz App 🌟</h1>", unsafe_allow_html=True)

# Quiz Questions
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Karachi", "Islamabad", "Lahore", "Quetta"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Quaid-e-Azam", "Allama Iqbal", "Liaquat Ali Khan", "Zulfiqar Ali Bhutto"], "answer": "Quaid-e-Azam"},
    {"question": "Which city is known as the city of lights?", "options": ["Karachi", "Islamabad", "Lahore", "Quetta"], "answer": "Karachi"},
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Bangalore", "Kolkata"], "answer": "Delhi"},
    {"question": "What is the capital of USA?", "options": ["Washington DC", "New York", "Los Angeles", "Chicago"], "answer": "Washington DC"},
    {"question": "What is the capital of UK?", "options": ["Manchester", "Liverpool", "London", "Birmingham"], "answer": "London"},
]

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question
question = st.session_state.current_question

# Display Question
st.subheader(f'📝 {question["question"]}')

# Option Selection with Radio Button
selected_option = st.radio("Choose an answer:", question["options"], key="answer")

# Submit Button
if st.button("Submit ✅"):
    if selected_option == question["answer"]:
        st.success("🎉 Correct Answer!")
    else:
        st.error(f"❌ Incorrect! The correct answer is: **{question['answer']}**")
        #? for stoping the code at this point 
        breakpoint()

    time.sleep(3)  # Delay before loading the next question

    # Load a new question
    st.session_state.current_question = random.choice(questions)

    st.rerun()  # Refresh the page to show the next question
