import chainlit as cl # type: ignore 
@cl.on_message
async def message_handler(message:cl.message):
    response = f'You said: {message.content}'
    await cl.Message(content=response).send()
