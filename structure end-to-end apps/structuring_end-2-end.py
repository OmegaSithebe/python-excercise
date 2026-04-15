# 1. Structuring End-to-End Applications - 1.1 Structuring an API call

import os
from dotenv import load_dotenv
from openai import OpenAI

#load the environment variable
load_dotenv()

#get & initialize the environment variable
api_key = os.getenv('OPENAI_API_KEY')


#get & catch api_key load error
if not api_key:
    raise ValueError('API key not found/loaded: Please check environment file (.env)')


#create OpenAI client
client = OpenAI(api_key=api_key)


# Create the request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format={"type":"json_object"}
)

# Print the response
print(response.choices[0].message.content)


# Handling errors
# from openai import OpenAI

client=OpenAI()

response=client.chat.completions.create(
model="old-model-name",
messages=[{"role":"user","content":"Hello"}]
)


# try:
# response=client.chat.completions.create(
# model="gpt-4.1-mini",
# messages=[{"role":"user","content":"Hello"}]
#     )

# exceptExceptionase:
# print("Connection issue. Please try again later.")


# import time

# for i in range(5):
#  try:
# response=client.chat.completions.create(
# model="gpt-4.1-mini",
# messages=[{"role":"user","content":"Tell me a joke"}]
#         )
# print(response.choices[0].message.content)

# except Exception:
# print("Rate limit reached. Waiting...")
# time.sleep(5)


# Handling Exceptions in Python
# client = OpenAI(api_key=api_key)

# try:
#     response=client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[{"role":"user","content":"List five data science profession"}],
   
#     )
#     print(response.choices[0].message.content)

# except openai.AuthenticationError as e:
#        print(f"Invalid API key. {e}")
# except Exception as e:
#     print(f"Unexpected error occurred.{e}")


# Handling Specific Errors
# client = OpenAI(api_key=api_key)

# try:
#     response=client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[{"role":"user","content":"List five data science profession"}],
   
#     )
#     print(response.choices[0].message.content)

# except openai.AuthenticationError as e:
#        print(f"Invalid API key. {e}")

# # except openai.RateLimitError as e:
# #         print(f"Too many requests. Please wait.{e}")
# except Exception as e:
#     print(f"Unexpected error occurred.{e}")


# Exercise - Handling exceptions
# client = OpenAI(api_key="OPENAI_API_TOKEN")

# # Use the try statement
# try: 
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[message]
#     )
#     # Print the response
#     print(response.choices[0].message.content)
# # Use the except statement
# except openai.AuthenticationError as e:
#     print("Please double check your authentication key and try again, the one provided is not valid.")


#Batching
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

# Exercise - Avoiding rate limits with retry
import os
from dotenv import load_dotenv
from openai import OpenAI

#Load environemtn variable from the dotenv file
load_dotenv()

#get the openai api key from the env file
api_key = os.getenv('OPENAI_API_KEY')

#catch error if api key not loaded
if not api_key:
  raise ValueError('openai api key not found, please check .env file (.env)')

#create openai client
client = OpenAI(api_key=api_key)

