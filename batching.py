import os
import time
from dotenv import load_dotenv
from openai import OpenAI

#load the environment variable from the .env file
load_dotenv()

# get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

#raise catch error if not loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# create an instance of the OpenAI client
client = OpenAI(api_key=api_key)

#create message to sent to the API
questions = [
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?"
]






#Methods to avoid Rate Limits
import time

for question in questions:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{'role': 'user', 'content': question}]
    )

    print(response.choices[0].message.content)

    time.sleep(2)  # Sleep for 2 seconds to avoid hitting rate limits
    
    
    
#Automatic Retry Mechanism
from tenacity import retry, wait_random_exponential, stop_after_attempt
from openai import OpenAI

client=OpenAI()

@retry(wait=wait_random_exponential(min=1, max=60),
       stop=stop_after_attempt(5))
def get_response():
    resposne=client.chat.completions.create(
        model='gpt-4.1-mini',
        messages=[{'role':'user', 'content':'Tell me a joke'}]
    )
    return response.choices[0].message.content

print(get_response())


#Example Problem
countries=['France', 'South Africa', 'Brazil']

for country in countries:
    reponse=client.chat.completions.create(
        model='gpt-4-1-mini',
        messages=['role':'user', 'content':f'what is the capital of {country}?']
    )
    


countries= ["France","Japan","Brazil"]

response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {
"role":"system",
"content":"Provide the capital city for each country listed."
        },
        {
"role":"user",
"content":f"Countries:{countries}"
        }
    ]
)

print(response.choices[0].message.content)


#Counting Tokens in Python
import tiktoken

encoding=tiktoken.encoding_for_model('gpt-4.1-min')

text='Artificial intelligence is transforming modern technology'

tokens = encoding.encode(text)

print('Number of tokens: ', len(tokens))



# Best Practices for Avoiding Rate Limits
# Developers should follow these guidelines:
# ✔ Add delays between requests
# ✔ Use automatic retry mechanisms
# ✔ Batch multiple tasks into one request
# ✔ Reduce unnecessary text in prompts
# ✔ Monitor token usage
# These techniques make AI applications **faster, more reliable, and scalable**.

# Key Takeaways
# Rate limits help maintain **fair and stable API usage**.
# To handle them effectively:
# - understand why they occur
# - retry failed requests
# - batch multiple tasks
# - reduce token usage
# These strategies are essential when building **large-scale AI systems**.


#Exercise
# Import the tenacity library
from tenacity import (retry, stop_after_attempt, wait_random_exponential)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=[message]
    )
    return response.choices[0].message.content
print(get_response("gpt-4o-mini", {"role": "user", "content": "List ten holiday destinations."}))



#Batching messsages
client = OpenAI(api_key="OPENAI_API_TOKEN")

messages = []
# Provide a system message and user messages to send the batch
messages.append({
            "role": "system",
            "content": "Convert each measurement, given in kilometers, into miles, and reply with a table of all measurements."
        })
# Append measurements to the message
[messages.append({"role":"user", "content": str(i)

}) for i in measurements]

response = get_response(messages)
print(response)


# Setting token limits
client = OpenAI(api_key="OPENAI_API_TOKEN")
input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}

# Use tiktoken to create the encoding for your model
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
# Check for the number of tokens
num_tokens = len(encoding.encode(input_message["content"]))

# Run the chat completions function and print the response
if num_tokens <= 100:
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[input_message])
    print(response.choices[0].message.content)
else:
    print("Message exceeds token limit")
