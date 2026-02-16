import os
from dotenv import load_dotenv
from openai import OpenAI

#load environment variables from .env file
load_dotenv()

#Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')


#Optional: Check if API key is loaded
if not api_key:
    raise ValueError('API key not found. Please set OPENAI_API_KEY in your environment variables (.env file).')

# Create a client (make sure your OPENAI_API_KEY is set in your environment)
# WARNING: Your API key is exposed in this code! Never share or commit API keys.
client = OpenAI(api_key=api_key)

prompt = 'Explain OpenAI API in simple terms.'

response = client.chat.completions.create(
    model='gpt-4o-mini',
    max_completion_tokens=100,
    messages=[
        {'role': 'user', 'content': 'Why is learning OpenAI API important for developers?'}
    ]
)

print(response)

print(response.choices[0].message.content)
