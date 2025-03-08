# import streamlit as st
# from datetime import datetime
# from zoneinfo import ZoneInfo
# TIME_ZONES = ['UTC', 'America/New_York', 'Asia/Kolkata', 'Australia/Sydney', 'Europe/London', 'Europe/Paris','Asia/Tokyo', 'Asia/Karachi']
# selected_time_zone = st.multiselect('Select Time Zones', TIME_ZONES, default=['UTC', 'Asia/Karachi'])

# st.subheader('Selected Time Zones')
# for tz in selected_time_zone:
#     current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I %H:%M:%S %p')
#     st.write(f'**{tz}**: {current_time}')


# st.subheader('Convert Time Zone')
# time = st.time_input('Enter Time', datetime.now().time())
# from_time = st.selectbox('From Time Zone', TIME_ZONES, index=0)
# to_time = st.selectbox('To Time Zone', TIME_ZONES, index=1)

# if st.button('Convert Time Zone'):
#     dt = datetime.combine(datetime.today(), time, tzinfo=ZoneInfo(from_time))
#     converted_time = dt.astimezone(ZoneInfo(to_time)).strftime('%Y-%m-%d %I:%M:%S %p')
#     st.write(f'Converted Time is {to_time}:  {converted_time}')
    
import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

# --- Set Page Config ---
st.set_page_config(page_title="Time Zone Checker & Converter", layout="centered")

# --- CSS for Styling ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #ffffff, #e3eaf8);
        font-family: Arial, sans-serif;
    }
    .stApp {
        background: linear-gradient(to right, #ffffff, #e3eaf8);
    }
    .title {
        font-size: 28px;
        text-align: center;
        font-weight: bold;
        color: #333;
    }
    .subheader {
        font-size: 20px;
        font-weight: bold;
        color: #444;
    }
    .time-display {
        background-color: #222;
        color: #fff;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .converted-time {
        background-color: #222;
        color: #fff;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .custom-label {
        font-size: 16px;
        font-weight: bold;
        color: #0056b3; /* Blue color */
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Time Zone Options ---
TIME_ZONES = ['UTC', 'America/New_York', 'Asia/Kolkata', 'Australia/Sydney', 
              'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Asia/Karachi']

# --- Header ---
st.markdown('<div class="title">🌎 Time Zone Checker & Converter</div>', unsafe_allow_html=True)
st.write("Check and convert time between different time zones easily!")

# --- Time Zone Checker ---
st.markdown('<div class="subheader">⏳ Selected Time Zones</div>', unsafe_allow_html=True)
selected_time_zones = st.multiselect('Select Time Zones', TIME_ZONES, default=['UTC', 'Asia/Karachi'])

for tz in selected_time_zones:
    current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I:%M:%S %p')
    st.markdown(f'<div class="time-display">**{tz}**: {current_time}</div>', unsafe_allow_html=True)

# --- Time Zone Converter ---
st.markdown('<div class="subheader">🔄 Convert Time Zone</div>', unsafe_allow_html=True)
time = st.time_input('Enter Time', datetime.now().time())

# Styled Dropdown Labels
st.markdown('<div class="custom-label">🌍 From Time Zone</div>', unsafe_allow_html=True)
from_time_zone = st.selectbox('', TIME_ZONES, index=0)

st.markdown('<div class="custom-label">🌏 To Time Zone</div>', unsafe_allow_html=True)
to_time_zone = st.selectbox('', TIME_ZONES, index=1)

if st.button('Convert Time Zone'):
    # Combine selected time with today's date & set timezone correctly
    dt = datetime.combine(date.today(), time).replace(tzinfo=ZoneInfo(from_time_zone))
    converted_time = dt.astimezone(ZoneInfo(to_time_zone)).strftime('%Y-%m-%d %I:%M:%S %p')

    st.markdown(f'<div class="converted-time">Converted Time ({to_time_zone}): {converted_time}</div>', 
                unsafe_allow_html=True)
