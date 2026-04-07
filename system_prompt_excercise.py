from dotenv import load_dotenv

load_dotenv()
from pyexpat.errors import messages
from anthropic import Anthropic


def user_message(messages, text):
    messages.append({"role": "user", "content": text})


def assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages):
    parameters = {
        "model": "claude-sonnet-4-0",
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        parameters["system"] = system
    client = Anthropic()
    message = client.messages.create(**parameters)
    return message.content[0].text


messages = []
system = """You are a helpful python coding assistant.
If the user asks for any code then do not explain everything, just give the code. If the user asks for an explanation then explain the code in a way that a 10 year old can understand."""
while True:
    user_input = input(
        "I am your python coding assistant. Enter a python code snippet or ask for an explanation: "
    )
    user_message(messages, user_input)
    answer = chat(messages)
    assistant_message(messages, answer)
    print("-----------")
    print("Assistant:", answer)
    print("------------")
