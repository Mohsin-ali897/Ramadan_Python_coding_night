# import google.generativeai as genai # type: ignore
# from dotenv import load_dotenv # type: ignore
# import os
# load_dotenv()
# genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# model = genai.GenerativeModel(model_name='gemini-2.0-flash')
# # query = input("Enter your query OR TYPE exit for exit: ")
# # response = model.generate_content(query)
# # # response = model.generate_content('how llm works')
# # print(response.text)


# #! for continous runnig the programme
# while True:
#     query = input("Enter your query OR TYPE exit for exit: ")
#     if query == 'exit':
#         break
#     response = model.generate_content(query)
#     print(response.text) 
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    
    )
@cl.on_chat_start
async def handle_chat():
    await cl.Message(content="Hello, I am a chatbot. How can I help you?").send()
@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    resonse_text = response.text if hasattr(response, 'text') else response
    await cl.Message(content=resonse_text).send()
 
if __name__ == '__main__':
    cl.handle_chat()
    cl.handle_message()
# GEMINI_API_KEY=AIzaSyAsD882ZxOCoV-Q34REtACxjv3uGEBC23E