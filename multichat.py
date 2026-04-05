from pyexpat.errors import messages
from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic


# for user message to api
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


# creating a empty list of messages to start the conversation
messages = []
# adding a user message to the messages list
add_user_message(messages, "define quantum computing in a single line")
# sending the messages list to the chat function and storing the answer in a answer variable
answer = chat(messages)
answer
# now adding the answer from the assistant to the messages list
add_assistant_message(messages, answer)
# now we can continue the conversation by adding more user messages and sending the updated messages list to the chat function again
add_user_message(messages, "write another sentence")
# sending the messages list to the chat function and storing the answer in a answer variable again
answer = chat(messages)
answer
# now adding the answer from the assistant to the messages list
# add_assistant_message(messages, answer)
# this way we can have a multi-turn conversation with the assistant by keeping track of the messages in a list and sending the updated list to the chat function each time we want to get a response from the assistant.
