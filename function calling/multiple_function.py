# Working With Multiple Functions (Parallel Function Calling)
## 1. Introduction
# Previously, we learned how to use **function calling to extract structured data** from text using an API.
# Now we will extend this concept by learning how to:
# - Use **multiple functions in a single API call**
# - Allow the model to **choose or call multiple functions**
# - Control which function the model should call
# This capability is called **Parallel Function Calling**.

# 2. What is Parallel Function Calling?
# **Parallel Function Calling** means that the AI model can:
# - Access **multiple functions**
# - Decide **which function(s) to call**
# - Return **multiple function responses**

### Why is this useful?
# It improves communication between the **application and the model** by allowing the model to:
# - Process more complex tasks
# - Use multiple tools
# - Generate richer responses



# Two Function Example - Function 1 - Extract Job information
def extract_job_data(description):
    return {
        'job_title': 'Data Scientist',
        'location': 'New York',
        'skills': ['Python', 'Machine Learning']
    }
    

# Function 2 - Get Timezone from Location
def get_timezone(location):
    return {
        'location': location,
        'timezone': 'EST'
    }
    
    

# 11. Summary
# Key takeaways:
### Parallel Function Calling
# Allows the model to:
# - Use multiple functions
# - Process complex tasks
# - Return multiple structured outputs


import os
from dotenv import load_dotenv
from openai import OpenAI

#create call function for the variable
load_dotenv()

#initialize the api_key variable
api_key = os.getenv('OPENAI_API_KEY')

#raise error if dotenv file not loaded
if not api_key:
    raise ValueError('dotenv api_key not loaded: check dotenv file')

# content message
message_listing = """
    I recently bought this smartphone and I really like it. The battery life is great and the camera is amazing. However, the phone feels a bit heavy.
"""

#Preloaded function definition
function_definition = [
    {
        'type': 'function',
        'function': {
            'name': 'extract_review_info',
            'description': 'Extract sentiment and key features',
            'parameters': {
                'type': 'object',
                'properties': {
                    'sentiment': {
                        'type': 'string',
                        'description': 'overall sentiment of the review'
                    },
                    'features': {
                        'type': 'array',
                        'items': {'types': 'string'}
                    }
                },
                'required': ['sentiment', 'features']
            }
        }
    }
]

function_definition.append({'type': 'function', 'function': {'name': 'reply_to_review', 'description': 'Reply politely to the customer who wrote the review', 'parameters': {'type': 'object', 'properties': {'reply': {'type': 'string', 'description': 'Reply to post in reponse to the review'}}},
        'required': ['reply']}})


#Initialize the OpenAI object for python script gateway communication with OpenAI server's
client = OpenAI(api_key=api_key)

#create schema for get_resonse call
def get_response(message, function):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': 'You are an assistant that extracts structured data, and reply to the review'},
            {'role': 'user', 'content': message}
            ],
        tools=function,
        tool_choice='auto'
        
    )
    
    # Extract tool call
    return response.choices[0].message.tool_calls

response = get_response(message_listing, function_definition)

print(response[0].function.arguments)
print(response[1].function.arguments)



# clear explanation
# In this script, you are using Parallel Function Calling. This is a feature where the model identifies that multiple tools are relevant to the user's request and decides to call them all at once rather than one by one.
# Here is the breakdown of how the process works and how those specific list indexes function:
## 1. The Model’s Decision
# When you send the message_listing and the function_definition list to OpenAI, the system prompt tells the model to "extract structured data and reply to the review."
# * The model looks at your tools list and sees two distinct functions: extract_review_info and reply_to_review.
# * Because the prompt asks for both actions, the model generates a response containing a list of tool_calls.

## 2. The response.choices[0].message.tool_calls List
# Instead of returning a standard text string, the model returns an array (a list) of objects.
# * response[0]: This is the first "tool call" object in that list. Usually, the model processes the functions in the order it deems most logical or the order they appear in your tool definition. In this case, it's likely the extraction tool.
# * response[1]: This is the second "tool call" object. It contains the data for the second function (the reply).

## 3. How the Arguments are Printed
# When you call response[0].function.arguments, you are accessing the specific JSON data the model "made up" to fill that function's parameters.
# * response[0] logic: The model generates a JSON string like {"sentiment": "positive", "features": ["battery life", "camera", "weight"]}.
# * response[1] logic: The model generates a second, separate JSON string for the second function, like {"reply": "Thank you for your feedback! We are glad you love the camera..."}.

## Why are they different?
# They are different because the model treats each index in the tool_calls array as a separate instruction to your code.
#    1. Index 0 is the "payload" for the first function it wants to trigger.
#    2. Index 1 is the "payload" for the second function it wants to trigger.



# Exercise - Setting a specific function
import os
from dotenv import load_dotenv
from openai import OpenAI

#function for loading the dotenv file
load_dotenv()

#create and initialize the openai variable
api_key = os.getenv('OPENAI_API_KEY')

#catch error if api_key variable not loaded
if not api_key:
    raise ValueError('api_key not loaded, check dotenv (.env) file')

#initialize the OpenAI client for communication
client = OpenAI(api_key=api_key)

#message content
message_listing2 = """
    Extract product name, variant and sentiment from the following reviews:
    
    1. I just received my AuraPro Wireless Headphones in Midnight Black, and I am blown away. The sound quality is crisp, and they are so comfortable for long flights. Definitely worth the price!
    
    2. Bought the EcoSpring Water Bottle (2L, Forest Green). It looks great and the insulation keeps water cold all day, but it’s much heavier than I expected when full. It’s okay, but maybe not for hiking.
    
    3. Extremely disappointed with the Lunar Tab 10 (128GB, Silver Edition). The screen started flickering after just two days of use, and the battery drains in less than three hours. I'll be returning this immediately.
"""

#function definition
function_definition2 = [
    {
        'type': 'function',
        'function': {
            'name': 'extract_review_key_features',
            'description': 'Analyze and extract key main product name, variant, and sentiment from customer reviews.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'reviews': {
                        'type': 'object',
                        'description': 'List of extracted review data',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'product_name': {
                                    'type': 'string',
                                    'description': 'Extract product name of the product.'
                                },
                                'variant': {
                                    'type': 'string',
                                    'description': 'Extract the product variant from the customer review, like storage, model, etc'
                                },
                                'sentiment': {
                                    'type': 'string',
                                    'enum': ['positive', 'negative', 'neutral'],
                                    'description': 'Extract customer sentiment.'
                                }
                            },
                            'required': ['product_name', 'variant', 'sentimemnt']  
                        }
                    }
                },
                'required': ['review'] 
            }
        }
    }
]

#get_response function
def get_response(message, function):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': 'You are an assistant that extract structured data from customer reviews.'},
            {'role': 'user', 'content': message}
        ]
        tools=function,
        tool_choice={
            "type": "function",
            "function": {"name": "extract_review_key_features"}
        }
    )

#print output
print(response.choices[0].message.tool_calls[0].function.arguments)



#Avoiding inconsistent responses

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


# -----------------------------
# Messages (review input)
# -----------------------------
messages = [
    {
        "role": "system",
        "content": "You are an assistant that processes customer reviews."
    },
    {
        "role": "user",
        "content": "The delivery was fast and packaging was great, but nothing else to say."
    }
]

# 🔥 IMPORTANT: Avoid assumptions
messages.append({
    "role": "system",
    "content": (
        "Do not make assumptions about missing information. "
        "If the review does not contain a product name, variant, or clear sentiment, "
        "do not generate or guess those values. "
        "Only extract or respond when sufficient information is present."
    )
})

# -----------------------------
# Function Definitions
# -----------------------------
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract product name, variant, and sentiment from a review",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "variant": {"type": "string"},
                    "sentiment": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"]
                    }
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "reply_to_review",
            "description": "Generate a polite reply to a customer review",
            "parameters": {
                "type": "object",
                "properties": {
                    "reply": {
                        "type": "string",
                        "description": "Professional reply to the customer"
                    }
                },
                "required": ["reply"]
            }
        }
    }
]

# -----------------------------
# Helper function
# -----------------------------
def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition,
        tool_choice="auto"  # Let model decide whether to call a function
    )

    message = response.choices[0].message

    # If function is called
    if message.tool_calls:
        return message.tool_calls[0].function.arguments
    else:
        return message.content


# -----------------------------
# Call and print response
# -----------------------------
response = get_response(messages, function_definition)

print(response)