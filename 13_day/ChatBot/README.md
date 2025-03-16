# 🚀 Day 13 - Ramadan Coding Night Challenge  

## 🔥 Exploring Chainlit: Hooks, Events & Decorators  

### 📝 Overview  
On **Day 13** of my **Ramadan Coding Night Challenge**, I explored **Chainlit**, a powerful framework for building conversational AI applications. I focused on:  
- **Hooks & Events** in Chainlit  
- Using the **@cl.on_message** decorator  
- Handling user messages dynamically  

### 📜 Code Implementation  
Here’s the **Chainlit bot** that responds to user messages:  

```python
import chainlit as cl  # type: ignore

@cl.on_message
async def message_handler(message: cl.Message):
    response = f'You said: {message.content}'
    await cl.Message(content=response).send()
```