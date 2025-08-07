from dotenv import load_dotenv
import os
import openai

# Initialize the OpenAI client
load_dotenv()
client = openai.OpenAI()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_chat_completion(prompt):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )
    for chunk in response:
        if 'choices' in chunk and len(chunk['choices']) > 0:
            print(chunk.choices[0].get('delta', {}).get('content', ''), end='')

# Example usage
if __name__ == '__main__':
    prompt_text = "What's the weather like today?"
    print("Querying chat completion with prompt:", prompt_text)
    get_chat_completion(prompt_text)
