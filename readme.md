# 🌙 Ramadan Coding Night Challenge 2025 🚀  

Welcome to my **Ramadan Coding Night Challenge** repository! This challenge, initiated by **Sir Asharib Ali**, is all about coding, learning, and building projects every night during Ramadan.  

## 📌 Day 1: CLI Task Manager  
For **Day 1**, I built a **CLI Task Manager** using Python. This is a simple yet efficient command-line tool for managing daily tasks.  

### 🚀 Features:  
- ✅ Add, remove, and list tasks  
- ✅ Mark tasks as completed  
- ✅ Data is stored in a JSON file for persistence  
- ✅ Uses **Click** for easy CLI interaction  
- ✅ Lightweight and fast  

### 🛠️ Installation  
Make sure you have **uv** installed. If not, install it first:  
```bash  
pip install uv  
```

### 🚀 How to Run  
Use the following commands to manage your tasks:  

#### ✅ Add a Task  
To add a new task, run:  
```bash  
uv run python todo.py add 'Python practice'  
```
This will store the task in `todo.json`.  

#### ❌ Remove a Task  
To delete a task, provide its index number:  
```bash  
uv run python todo.py remove 2  
```

#### 📌 Mark Task as Completed  
To mark a task as completed:  
```bash  
uv run python todo.py complete 2  
```

#### 📜 List All Tasks  
To view all tasks:  
```bash  
uv run python todo.py list  
```

---

## 📌 Day 2: Unit Converter App  
For **Day 2**, I built a **Unit Converter App** using **Streamlit**. This app allows users to convert between different units easily, showcasing the power and simplicity of Streamlit for web-based applications.  

### 🚀 Features:  
- Convert between various units (length, weight, temperature, etc.)  
- Simple and interactive UI with Streamlit  
- Fast and lightweight  

## 📌 Day 3: Secure Password Generator App 🔐  
For **Day 3**, I developed a **Secure Password Generator App** using **Streamlit**. It helps users generate strong and secure passwords with customization options.  

### 🚀 Features:  
- ✅ Choose password length (6 to 50 characters)  
- ✅ Include **digits** and **special characters**  
- ✅ Beautiful **dark theme** UI  
- ✅ One-click password generation  
- ✅ **Copy to Clipboard** feature  

### 🎮 Live Demo  
🔗 [Try the Password Generator](https://python-password-generator89.streamlit.app/)  

## 📌 Day 4: FastAPI - Side Hustle & Money Quotes API  
For **Day 4**, I explored **FastAPI**, a modern and high-performance web framework for building APIs with Python. I created a simple API that provides **side hustle ideas** and **money quotes**.  

### 🚀 Features:  
- ✅ Returns a random **side hustle idea**  
- ✅ Returns a random **money quote**  
- ✅ API authentication using a basic API key  
- ✅ Implemented with **FastAPI** and **uvicorn**  
- ✅ Interactive API documentation with **Swagger UI**  

### 🛠 How to Run the API:  
1. Install dependencies:  
```sh  
uv pip install fastapi uvicorn  
```
2. Run the server:  
```sh  
   fastapi dev main.py  
```
3. Access **Swagger UI** for testing:  
```
http://127.0.0.1:8000/docs  
```

## 📌 Day 5: Money Making Machine App 💰  
For **Day 5**, I focused on integrating APIs into a **Money Making Machine App** using **Streamlit**. Today, I learned:  
- How to fetch API data using the `requests` module  
- How to use the `random` module for generating values  
- How to use the `time` module for implementing delays  
- Running my previous class code that included simple APIs  
- Hosting APIs on a local server and fetching data in my project  

### 🚀 Features:  
- ✅ Generates a **random money amount** 💵  
- ✅ Fetches **money quotes** from a local API  
- ✅ Fetches **side hustle ideas** from a local API  
- ✅ Implements **loading indicators** for better user experience  
- ✅ Styled UI using **Streamlit Markdown and CSS**  

### 🛠 How to Run the Project:  
1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/ramadan-coding-challenge.git
   cd ramadan-coding-challenge/day5
   ```
2. Install dependencies:  
   ```sh
   pip install streamlit requests
   ```
3. Run the local API server (from Day 4):  
   ```sh
   fastapi dev main.py
   ```
4. Start the Streamlit app:  
   ```sh
   streamlit run app.py
   ```

## 📌 Day 6: ⏳ Time Zone Checker & Converter  

For **Day 6**, I built a **Time Zone Checker & Converter** using **Python & Streamlit**. This app allows users to check the current time in multiple time zones and convert time from one zone to another.  

### 🚀 Features:  
- ✅ **Check real-time updates** for multiple time zones  
- ✅ **Convert time** between different time zones  
- ✅ **Modern UI** with a gradient background & dark-styled time display  
- ✅ **Interactive dropdowns** for selecting time zones  
- ✅ **Instant conversion** with a simple button click  

---

## 🛠️ Technologies Used  

- **Python** 🐍  
- **Streamlit** 🎨  
- **ZoneInfo** (for time zone handling)  
- **HTML & CSS** (for styling)  

## 📌 Day 7: Mood Tracker App 😃  
A **Mood Tracker App** built using **Streamlit, Pandas, and Plotly** to track and visualize mood trends.  

### 🚀 Features:  
- **Emoji-Based Mood Selection** – Makes tracking fun 😃😐😞😡  
- **Modern UI** – Clean, sleek design 🎨  
- **Interactive Mood Trends** – **Plotly charts** to visualize emotional patterns 📊  
- **Seamless Data Logging** – Stores mood entries in CSV format 📂  

### 🛠️ What I Learned  
- Improving UI in **Streamlit** with custom CSS  
- Using **Plotly** for interactive graphs  
- Data handling & visualization using **Pandas**  

### 🎮 Live App  
🔗 [Your Deployment Link]  


---

## 🛠️ Technologies Used  
- **Python** 🐍  
- **Streamlit** 🎨  
- **Plotly** 📊  
- **Pandas** 📖  
- **CSV for data storage**  

---


## 🎮 Ramadan Coding Night Challenge Playlist  
Watch the full **Ramadan Coding Night Challenge** series here:  
🔗 **[YouTube Playlist](https://www.youtube.com/live/EeFUfDNNoNg?si=owG-2tdSuGIYqSJD)**  

## 🎯 Stay Connected!  
Follow my journey and updates:  
- 🌟 [LinkedIn](YOUR_LINKEDIN_PROFILE)   
- 📚 [GitHub](YOUR_GITHUB_PROFILE)  

A big thanks to **Sir Asharib Ali** for guiding and inspiring us throughout this challenge! 🙌  

#RamadanCodingNight #Streamlit #FastAPI #Python #CodingChallenge #Learning


