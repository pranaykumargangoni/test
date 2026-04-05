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
system = """You are a patient math tutor.
You will be given a math problem and you will explain the solution step by step in a way that a 10 year old can understand.
You will also provide the final answer to the problem at the end of your explanation."""
while True:
    user_input = input("Enter a math problem: ")
    user_message(messages, user_input)
    answer = chat(messages)
    assistant_message(messages, answer)
    print("-----------")
    print("Assistant:", answer)
    print("------------")
