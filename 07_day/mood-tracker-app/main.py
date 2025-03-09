# import streamlit as st # for creating web app
# import pandas as pd # for data manipulation
# import datetime # for date and time 
# import csv # for reading & writing csv files
# import os  # for file handling

# MOOD_FILE = 'mood_log.csv'
# def load_mood_data():
#     if not os.path.exists(MOOD_FILE):
#         return pd.DataFrame(columns=['date', 'mood'])
#     return pd.read_csv(MOOD_FILE)
# def save_mood_data(data, mood):
#     with open(MOOD_FILE,'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data, mood])
        
# st.title('Mood Tracker App')
# today = datetime.date.today().strftime('%Y-%m-%d')
# st.subheader('How are you feeling today?')
# mood = st.selectbox('Select mood', ['Happy', 'Neutral', 'Sad', 'Angry'])
# if st.button('Save Mood'):
#     save_mood_data(today, mood)
#     st.success('Mood saved successfully')
# data = load_mood_data()
# if not data.empty:
#     st.subheader('Moods Trends Over Time')
#     data['Date']= pd.to_datetime(data['Date'])
#     mood_count = data.groupby('Mood').count()['Date']
#     st.bar_chart(mood_count)
import streamlit as st  
import pandas as pd  
import datetime  
import csv  
import os  
import plotly.express as px   # type: ignore

# File to store moods
MOOD_FILE = "mood_log.csv"

# Load mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["date", "mood"])
    return pd.read_csv(MOOD_FILE)

# Save mood data
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Custom styles
st.markdown(
    """
    <style>
    .main {background-color: #f5f7fa;}
    .stButton>button {border-radius: 8px; background-color: #4CAF50; color: white; padding: 10px 24px; font-size: 16px;}
    .stSelectbox>div>div {border-radius: 8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title & Subtitle
st.title("🌿 Mood Tracker App")
st.subheader("How are you feeling today?")

# Mood selection with emojis
moods = {
    "😊 Happy": "Happy",
    "😐 Neutral": "Neutral",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
}
mood_choice = st.selectbox("Select your mood:", list(moods.keys()))

# for Saving mood
today = datetime.date.today().strftime("%Y-%m-%d")
if st.button("Save Mood"):
    save_mood_data(today, moods[mood_choice])
    st.success("✅ Mood saved successfully!")

# for Load and visualize data
data = load_mood_data()
if not data.empty:
    st.subheader("📊 Mood Trends Over Time")
    data.columns = ["date", "mood"]  # Ensure correct column names
    data["date"] = pd.to_datetime(data["date"])

    mood_count = data["mood"].value_counts().reset_index()
    mood_count.columns = ["Mood", "Count"]

    fig = px.bar(
        mood_count,
        x="Mood",
        y="Count",
        color="Mood",
        title="Mood Distribution",
        labels={"Mood": "Mood Type", "Count": "Number of Times Logged"},
    )
    st.plotly_chart(fig)
