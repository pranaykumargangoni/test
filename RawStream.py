# this is for raw streaming of the response, which means that the response is being sent
#  in chunks as it is generated, rather than waiting for the entire response to be ready
# before receiving it.
from dotenv import load_dotenv

load_dotenv()
from anthropic import Anthropic

client = Anthropic()
x = client.messages.create(
    model="claude-sonnet-4-0",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Write a 1 sentence description of a fake database.",
        }
    ],
    stream=True,
)

for event in x:
    print(event)


# here from output we can see that the response is being streamed in chunks as it is generated,
# rather than waiting for the entire response to be ready before receiving it.
# This allows for a more responsive and interactive experience when working with large language models.
# the main output is in the rawcontentblockdeltaevent, which contains the generated text as it is being produced.
