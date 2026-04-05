from dotenv import load_dotenv

load_dotenv()
from pyexpat.errors import messages
from anthropic import Anthropic


def chat(messages):
    client = Anthropic()
    model = "claude-sonnet-4-0"
    messages = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return messages.content[0].text


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


messages = []
while True:
    user_input = input("You: ")
    add_user_message(messages, user_input)
    answer = chat(messages)
    add_assistant_message(messages, answer)
    print("-----------")
    print("Assistant:", answer)
    print("------------")
