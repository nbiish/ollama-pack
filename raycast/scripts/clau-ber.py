#!/usr/bin/env python3

import anthropic
import os
from dotenv import load_dotenv
import sys

# Load the .env file
load_dotenv()

client = anthropic.Anthropic(
    # Get the API key from the .env file
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0.0,
    system="You're having a conversation with a conmputer scientist, programmer, and cybersecurity student. Be Concise.",
    messages=[
        {"role": "user", "content": sys.argv[1] if len(sys.argv) > 1 else "Tell me a story about Nanaboozhoo."}
    ]
)

# Calculate the costs
input_cost = message.usage.input_tokens * 0.25 / 1000000
output_cost = message.usage.output_tokens * 1.25 / 1000000
total_cost = input_cost + output_cost

# Print the formatted output
print('\n' * 3)
print('-' * 81)
print('INPUT:')
print(sys.argv[1] if len(sys.argv) > 1 else "Tell me a story about Nanaboozhoo.")
print('-' * 81)
print('MODEL:')
print(message.model)
print('-' * 81)
print('Response:')
print('🍓' * 36)
print('-' * 81)
for item in message.content:
    print(item.text)
print('-' * 81)
print('🫐' * 36)
print('\n' * 3)
print('👍🧿👄🧿💻:')
print('Stats for nerds:')
print('-' * 81)
print(f'Token {message.usage}')
print()
print("claude-3-haiku costs as of 4-12-24:")
print(f'Input Tokens Cost: ${input_cost:.9f} USD')
print(f'Output Tokens Cost: ${output_cost:.9f} USD')
print(f'Total Cost: ${total_cost:.7f} USD')