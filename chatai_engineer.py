import os
from dotenv import load_dotenv
from openai import OpenAI

#load the environment variables from .env file
load_dotenv()

#Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

#Check if API key loads
if not api_key:
    raise ValueError('API key not found: Please check for API key at the enivornment file')


#Creating client
client = OpenAI(api_key=api_key)

#Chatbot prompt
prompt = 'Could you explain OpenAI API in simple terms'

response = client.chat.completions.create (
    model='gpt-4o-mini',
    max_completion_tokens=100,
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print(response)
print('=========================================')

print(response.choices[0].message.content)


## What’s Happening in This Code?- `OpenAI()` creates a connection to the OpenAI API- `model` specifies which AI model you want to use- `input` is your prompt (question or instruction)- `response.output_text` contains the AI’s reply
# This is the **same technology behind ChatGPT**, but now *you* control it through code.

## Reponse -“The API response is like a box. -Inside the box is a list. -Inside the list is a message. -Inside the message is the actual text.

## Understanding the API Response. The API returns a **ChatCompletion object** containing:- `id`- `model`- `created`- `choices` (most important). The actual text response is inside: response.choices[0].message.content
## Interpreting the Response (Step-by-Step)1. `choices` → a list 2. `[0]` → first response choice 3. `.message` → message object 4. `.content` → final text output. Result: model response as a **string**
## Key Takeaways - APIs work via **endpoints** - Authentication uses **API keys** - Requests → Responses - API responses are **structured objects** - Access data step-by-step using attributes

