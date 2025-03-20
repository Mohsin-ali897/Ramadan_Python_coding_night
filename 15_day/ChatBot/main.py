import chainlit as cl # type: ignore
import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv # type: ignore
from typing import Dict, Optional
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key= gemini_api_key)
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",

)
# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  # Print provider ID for debugging
    print(f"User data: {raw_user_data}")  # Print user data for debugging

    return default_user  # Return the default user object


# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message


# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")  # Get chat history from session

    history.append(
        {"role": "user", "content": message.content}
    )  # Add user message to history

    # Format chat history for Gemini model
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"  # Determine message role
        formatted_history.append(
            {"role": role, "parts": [{"text": msg["content"]}]}
        )  # Format message

    response = model.generate_content(formatted_history)  # Get response from Gemini

    response_text = (
        response.text if hasattr(response, "text") else ""
    )  # Extract response text safely

    history.append(
        {"role": "assistant", "content": response_text}
    )  # Add assistant response to history
    cl.user_session.set("history", history)  # Update session history

    await cl.Message(content=response_text).send()  # Send response to user


