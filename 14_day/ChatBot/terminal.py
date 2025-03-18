import google.generativeai as genai # type: ignore
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name='gemini-2.0-flash')
# query = input("Enter your query OR TYPE exit for exit: ")
# response = model.generate_content(query)
# # response = model.generate_content('how llm works')
# print(response.text)


#! for continous runnig the programme
while True:
    query = input("Enter your query OR TYPE exit for exit: ")
    if query == 'exit':
        break
    response = model.generate_content(query)
    print(response.text) 
