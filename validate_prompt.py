#!/usr/bin/env python3

"""Basic script using the OpenAI Python package to say 'hello world'."""

import os
from openai import OpenAI

def main():
    # Load your API key from an environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if openai.api_key is None:
        raise ValueError("Please set the OPENAI_API_KEY environment variable")

    # Send a simple chat completion request


client = OpenAI()
response = client.chat.completions.create(        
        model="gpt-4o",
        messages=[{"role": "user", "content": "hello world"}]
    )
    # Print the assistant's reply
print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
    