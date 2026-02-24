## Exercise
# **Controlling output structure**
import os
from dotenv import load_dotenv
from openai import OpenAI

#Load environment file
load_dotenv()

#Get & initialize the environment variable
api_key=os.getenv('OPENAI_API_KEY')

#Raise error if API Key not loaded
if not api_key:
    raise ValueError('API Key not loaded: Check environment file.')

#Create OpenAI API client
client = OpenAI(api_key=api_key)

# Create a one-shot prompt
prompt = """
     Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = {1, 3, 7, 19}
     Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:
"""


#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)




# Sentiment analysis with few-shot prompting

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "system", "content": "Your working on market research. Your goal is to use few-shot prompting to perform sentiment analysis on customer reviews."},
              {"role": "assistant", "content": "You are assigning a number for a given customers conversation: -1 if the sentiment is negative, 1 if positive."},
              {"role": "user", "content": "The product quality exceeded my expectations -> 1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service -> -1"},
              # Provide the text for the model to classify
              {"role": "user", "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)


#Solution
response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user",
  		     "content": "The product quality exceeded my expectations"},
              {"role": "assistant",
  		     "content": "1"},
              {"role": "user",
  		     "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant",
  		     "content": "-1"}, 
              # Provide the text for the model to classify
              {"role": "user",
  		     "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)



# 2.2 Multi-step prompting
# **Exercise**
# **Single-step prompt to plan a trip**

# Create a single-step prompt to get help planning the vacation
prompt = "I have 2 weeks of break from my job i need to plan for a beach vacation."

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)


# Multi-step prompt to plan a trip
# Create a prompt detailing steps to plan the trip
prompt = """
I need to plan for my 2 week beach vacation.
step 1: Four potential locations.
step 2: Each location must have accommodation options, some activities.
steo 3: Evaluate pros and cons for each locations.
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)



# Analyze solution correctness

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""" 
access the function provided in the delimited code string.
step 1: check for correct syntax.
step 2: receiving two inputs, 5 and 9.
step 3: returning one output.

{code}
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)


# 2.3 Chain-of-Thought and Self-Consistency Prompting
# Reasoning with chain-of-thought prompts

# Create the chain-of-thought prompt
prompt = """
Guess the age of my friend father in 10 years based on below conditions.
step 1: My frind is 20.
step 2: My frind father is twice the age of my friend.
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)



# One-shot chain-of-thought prompts
# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: (10,4,2). Adding them:10+4+2=16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}.
             A: Even numbers: """

# Create the final prompt
prompt = f"""

Find the sum {question} and example is {example}


"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content


response = get_response(prompt)
print(response)




# Self-consistency prompts
# Create the self_consistency instruction
self_consistency_instruction = 'Imagine three independent experts solving the problem. Each expert explains their reasoning. Choose the final answer by majority vote.'

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = f'''

The results from the three experts are as follows: {self_consistency_instruction} \n
The final answer that is solve is as follows: {[problem_to_solve]}
Those are the remaining results at the end of the day at the store.

'''

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=400,
        messages=[
            {'role': 'assistant', 'content': self_consistency_instruction},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)



# Solution

# Create the self_consistency instruction
self_consistency_instruction = "Imagine three completely independent experts who reason differently are answering this question. The final answer is obtained by majority vote. The question is: "

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)



# Iterative prompt engineering for standard prompts

# Refine the following prompt
prompt = "Give me the top 10 pre-trained language models, add a table with three columns, list model name, release year and owning company"

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=400,
        messages=[
            {'role': 'assistant', 'content': self_consistency_instruction},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content

response = get_response(prompt)
print(response)


response = get_response(prompt)
print(response)


# Iterative prompt engineering for few-shot prompts
# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
step 1: no explicit emotion

They sat and ate their meal ->
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=400,
        messages=[
            {'role': 'assistant', 'content': self_consistency_instruction},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    return response.choices[0].message.content


response = get_response(prompt)
print(response)


