from dotenv import load_dotenv

load_dotenv()
from anthropic import Anthropic


def user_message(messages, text):
    messages.append({"role": "user", "content": text})


def assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, temperature):
    parameters = {
        "model": "claude-sonnet-4-0",
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    client = Anthropic()
    message = client.messages.create(**parameters)
    return message.content[0].text


messages = []
system = """you are a helpful story writer. You will be given a story prompt and you will write a story based on the prompt. """
while True:
    user_input = input(
        "I am your story writer. Enter a story prompt, I will write a story based on the prompt: "
    )
    user_message(messages, user_input)
    answer = chat(messages, temperature=0)
    assistant_message(messages, answer)
    print("-----------")
    print("Assistant:", answer)
    print("------------")
