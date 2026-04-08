from dotenv import load_dotenv

load_dotenv()
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
messages = client.messages.create(
    model=model,
    max_tokens=300,
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(messages.content[0].text)
#qdfbadhbf