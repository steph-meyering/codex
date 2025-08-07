from dotenv import load_dotenv
import os
import tiktoken
import openai

def count_tokens(text):
    # Assuming use of GPT-4 encoding
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def main():
    # Request prompt from user
    prompt = input("Enter your prompt: ")
    
    # Count tokens in the prompt
    token_count = count_tokens(prompt)
    
    # Display token count
    print(f"Token count: {token_count}")
    
    # Ask for confirmation
    confirm = input("Do you want to send this to GPT-4o? (y/n): ").strip().lower(
)
    
    if confirm == 'y':
        load_dotenv()  # load environment variables from .env
        
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Send the input to GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True #Enable streaming
        )
        
        # Stream the response
        print("Response:", end=" ")
        for chunk in response:
            content = chunk.choices[0].delta.content or ''
            print(content, end="", flush=True)

if __name__ == "__main__":
    main()
