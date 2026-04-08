import json
from dotenv import load_dotenv

load_dotenv()
from anthropic import Anthropic


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages):
    client = Anthropic()
    model = "claude-sonnet-4-0"
    messages = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return messages.content[0].text


messages = []
add_user_message(
    messages, "Generate 3 different sample aws cli commands. Each should be very short"
)
add_assistant_message(
    messages, "```bash"
)  # this is prefilled message to make sure the model outputs the commands in a code block
y = chat(
    messages, stop_sequence=["```"]
)  # the stop sequence is used to make sure the model stops generating after the code block is closed
y.strip()
