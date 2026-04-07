from dotenv import load_dotenv

load_dotenv()
from anthropic import Anthropic

client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-0",
    max_tokens=1000,
    temperature=0,
    messages=[{"role": "user", "content": "palindrome python code"}],
) as x:
    for text in x.text_stream:
        print(text)
# instead of showing the resonse in chunks if we want to store in a variable so that we can use that for later
# and then print the final response we can do like this:
y = x.get_final_message()
print(y.content[0].text)
# By this the output will be a streaming response of the generated text in chunks.
# It means the model reply looks like fast typing and the text is being sent in chunks as it is generated,
# rather than waiting for the entire response to be ready before receiving it.
