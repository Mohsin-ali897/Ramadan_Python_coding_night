# FastAPI - Day 4 of Ramadan Coding Night Challenge

## What is FastAPI?
FastAPI is a modern, high-performance web framework for building APIs with Python. It is based on Starlette for web routing and Pydantic for data validation.

### Key Features:
- **Fast**: Asynchronous support makes it one of the fastest Python frameworks.
- **Automatic Docs**: Provides Swagger UI and ReDoc for API documentation.
- **Type Hints**: Uses Python type hints for automatic validation and better development experience.
- **Asynchronous & Synchronous Support**: Works with both async and sync functions.

## Where is FastAPI Used?
FastAPI is widely used in:
- Building RESTful APIs
- Machine learning model deployment
- Microservices architecture
- Real-time applications

## How to Use FastAPI?

### **Installation**
```sh
uv pip install fastapi uvicorn
```

### **Basic FastAPI Example**
```python
from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelance web development",
    "Affiliate marketing",
    "Dropshipping",
    "YouTube content creation",
    "Graphic design",
    "AI automation services"
]

money_quotes = [
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett"
]

@app.get('/side_hustles')
def get_side_hustles(apikey: str):
    if apikey != '1234567890':
        return {"error": "API key invalid"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get('/money_quotes')
def get_money_quotes():
    return {"money_quote": random.choice(money_quotes)}
```

### **Running the FastAPI Server**
```sh
uvicorn filename:app --reload
```

### **Accessing Swagger UI**
Once the server is running, open this URL in your browser:
```
http://127.0.0.1:8000/docs
```

### **Accessing ReDoc Documentation**
```
http://127.0.0.1:8000/redoc
```

## **What I Learned Today**
✅ What is FastAPI and where it is used  
✅ How to install and set up FastAPI using `uv` as a package manager  
✅ How to create API endpoints in FastAPI  
✅ How to run the FastAPI development server  
✅ How to use Swagger UI for API testing  

---
This was my **Day 4 of Ramadan Coding Night Challenge!** 🚀
