# Simple Chatbot with Chainlit and Gemini

## Overview
This is a simple chatbot built using [Chainlit](https://chainlit.io/) and [Google Gemini API](https://ai.google.dev/). The chatbot includes authentication using GitHub OAuth and maintains a session-based message history.

## Features
- Uses **Google Gemini API** for generating responses
- Implements **GitHub OAuth authentication**
- Maintains **chat history** within a session
- **Lightweight** and easy to deploy

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` package manager
- A Google API Key for Gemini
- A GitHub OAuth app (for authentication)

### Clone the Repository
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root and add:
```env
GEMINI_API_KEY=your_google_api_key
```

## Usage
### Run the Chatbot
```sh
chainlit run app.py
```

### How It Works
1. On startup, the chatbot initializes a session and welcomes the user.
2. Messages are stored in session history.
3. The chatbot interacts with the **Gemini API** to generate responses.
4. Authentication is handled via GitHub OAuth.

## Code Overview
### Key Components
- **Authentication:** Uses `@cl.oauth_callback` for GitHub login.
- **Message Handling:** `@cl.on_message` listens to user inputs and generates responses.
- **Session Management:** Stores history in `cl.user_session`.
- **Gemini API Integration:** Uses `generate_content()` to fetch AI responses.



