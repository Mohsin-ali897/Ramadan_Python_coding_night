# Day 14: Simple Chatbot using Streamlit & Google Gemini API

## Project Overview
On **Day 14** of the Ramadan Coding Night Challenge, I built a simple chatbot using **Streamlit** and the **Google Gemini API**. Additionally, I explored some Chainlit methods like `@cl.on_message` and `@cl.on_chat_start` to enhance the chatbot experience.

## Features
- Uses **Google Gemini API** (LLM) to generate responses.
- Implements **Chainlit** for an interactive chatbot UI.
- Supports **continuous conversation**.
- Listens to user queries and provides AI-generated responses.

## Installation & Setup

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Required Python libraries: `chainlit`, `google-generativeai`, `python-dotenv`

### Install Dependencies
```bash
pip install chainlit google-generativeai python-dotenv
```

### Setup Environment Variables
Create a `.env` file in your project directory and add your **Google Gemini API Key**:
```env
GEMINI_API_KEY=your_api_key_here
```

## Code Implementation
```python
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

# Chainlit Event Handlers
@cl.on_chat_start
async def handle_chat():
    await cl.Message(content="Hello, I am a chatbot. How can I help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, 'text') else str(response)
    await cl.Message(content=response_text).send()

if __name__ == '__main__':
    cl.handle_chat()
    cl.handle_message()
```

## Running the Chatbot
To start the chatbot, run the following command:
```bash
chainlit run main.py
```

## Learning Outcomes
- Learned how to integrate **Google Gemini API** with a chatbot.
- Explored **Chainlit hooks** (`@cl.on_chat_start`, `@cl.on_message`).
- Understood **handling AI-generated responses** effectively.

## Next Steps
- Improve chatbot UI using **Streamlit**.
- Add **context-based memory** for better responses.
- Deploy on **Cloud or Web App** for public use.

---
🎯 *Ramadan Coding Night Challenge - Day 14 Completed!* 🚀
