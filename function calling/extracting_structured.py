# Unstructured Text Example
# We are hiring a Data Scientist to join our team in New York.
# The candidate should have experience with Python, machine learning, and data analysis.

# Structured Data Format
# {
#   "job": "Data Scientist",
#   "location": "New York"
# }

# Structured data is easier to:
# - Store in databases
# - Process in applications
# - Use for automation

# Using Function Calling to Extract Data
# Instead of simply prompting the model to return JSON, we can define a function** that specifies exactly what data we want.
# This is done using the **`tools` parameter** in the OpenAI API request.
# The model will then return the output following the **function structure

# Implementing Function Calling
# tools = [
#   {
#     "type": "function",
#     "function": {
#       "name": "extract_job_info",
#       "description": "Extract job information from text",
#       "parameters": {
#         "type": "object",
#         "properties": {
#           "job": {
#             "type": "string",
#             "description": "The job title mentioned in the text"
#           },
#           "location": {
#             "type": "string",
#             "description": "The office location mentioned in the text"
#           }
#         }
#       }
#     }
#   }
# ]


# Understanding the Function Structure
#  1. Type
# "type": "function"
# This tells the API that we are defining a **user-created function**.
#  2. Function Name
# "name": "extract_job_info"

# The name identifies the function that the model can call.
#  3. Description
# "description": "Extract job information from text"
# The description tells the model **what the function should do**.


#  Parameters
# The parameters section defines what data we want to extract.
# "parameters": {
#   "type": "object",
#   "properties": {
#     "job": {...},
#     "location": {...}
#   }
# }
# "job": {
#   "type": "string",
#   "description": "The job title mentioned in the text"
# }


# Example Response
# {
#   "tool_calls": [
#     {
#       "function": {
#         "name": "extract_job_info",
#         "arguments": {
#           "job": "Data Scientist",
#           "location": "New York"
#         }
#       }
#     }
#   ]
# }


# Class Exercise Idea:
# Our company is hiring a Machine Learning Engineer in London.
# The role requires experience with Python and TensorFlow.
# {
#  "job": "Machine Learning Engineer",
#  "location": "London"
# }


import os
from dotenv import load_dotenv
from openai import OpenAI

# Function, calling dotenv variable from .env 
load_dotenv()

#Assign api_key variable
api_key = os.getenv("OPEN_API_KEY")


#Check api_key has loaded successfully
if not api_key:
    raise ValueError("api_key variable not loaded successfully, check .env file")


#Initialiaze the OpenAI client object, to act as a gateway for python script to communicate with OpenAI server's
client = OpenAI(api_key=api_key)

message_listing = """
    Beautiful 3-bedroom apartment for sale in New York.
    This modern apartment is listed at $750,000
"""

# Preloaded function definition/python schema
function_definition = [
    {
        'type': 'function',
        'function': {
            'name': 'extract_property_info',
            'description': 'Extract real estate property details',
            'parameters': {
                'type': 'object',
                'properties': {
                    'house_type': {
                        'type': 'string',
                        'description': 'Type of property (e.g, apartment, house)'
                    },
                    'location': {
                        'type': 'string',
                        'description': 'Location of the property'
                    },
                    'price': {
                        'type': 'string',
                        'description': 'Number of bedrooms'
                    },
                    'bedrooms': {
                        'type': 'string',
                        'description': 'Number of bedrooms'
                    }
                },
                'required': ['house_type', 'location', 'price', 'bedrooms']
            }
        }
    }
]

# get_response function calling
def get_response(messages, function):
    response = client.chat.completions.create(
        model='gpt-4.1-mini',
        messages=messages,
        tools=function,
        tool_choice = 'auto'
    )
    
    
# Complete working code 
import os
# import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Assign api_key variable
api_key = os.getenv("OPENAI_API_KEY")

# Check api_key has loaded successfully
if not api_key:
    raise ValueError("api_key variable not loaded successfully, check .env file")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Sample real estate listing
message_listing = """
Beautiful 3-bedroom apartment for sale in New York.
This modern apartment is listed at $750,000
"""

# Function (tool) definition
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_property_info",
            "description": "Extract real estate property details",
            "parameters": {
                "type": "object",
                "properties": {
                    "house_type": {
                        "type": "string",
                        "description": "Type of property (e.g, apartment, house)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Location of the property"
                    },
                    "price": {
                        "type": "string",
                        "description": "Property price"
                    },
                    "bedrooms": {
                        "type": "string",
                        "description": "Number of bedrooms"
                    }
                },
                "required": ["house_type", "location", "price", "bedrooms"]
            }
        }
    }
]

# Function that sends the request
def get_response(messages, function):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=function,
        tool_choice="auto"
    )
    return response


messages = [
    {"role": "user", "content": message_listing}
]

response = get_response(messages, function_definition)

# Extract the function call arguments
tool_call = response.choices[0].message.tool_calls[0]
arguments = json.loads(tool_call.function.arguments)

# Print structured output
print("✅ Extracted Property Information:")
print(f"House Type : {arguments['house_type']}")
print(f"Location   : {arguments['location']}")
print(f"Price      : {arguments['price']}")
print(f"Bedrooms   : {arguments['bedrooms']}")


# Exercise - Using the tools parameters
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

message_listing = """
   
    Beautiful 3-bedroom apartment for sale in New York.
    This modern apartment is listed at $750,000 and 
"""

# Preloaded function definition
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_property_info",
            "description": "Extract real estate property details",
            "parameters": {
                "type": "object",
                "properties": {
                    "house_type": {
                        "type": "string",
                        "description": "Type of the property (e.g., apartment, house)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Location of the property"
                    },
                    "price": {
                        "type": "string",
                        "description": "Price of the property"
                    },
                    "bedrooms": {
                        "type": "integer",
                        "description": "Number of bedrooms"
                    }
                },
                "required": ["house_type", "location", "price", "bedrooms"]
            }
        }
    }
]

client = OpenAI(api_key=api_key)

def get_reponse(message, function): 
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts structured data."},
        {"role": "user", "content": message}
    ],
    tools=function,
    tool_choice="auto"
)

# Extract tool call 
    return response.choices[0].message.tool_calls[0].function.arguments


print(get_reponse(message_listing, function_definition))

# ===============================================================

# Exercise - Building a function dictionary
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")





messages = [
    {
        "role": "system",
        "content": "You extract the title and year of publication from research papers."
    },
    {
        "role": "user",
        "content": """
        Research Paper:

        Title: Deep Learning for Natural Language Processing
        Authors: John Smith, Sarah Johnson
        Published in: Journal of AI Research, 2021

        Abstract:
        This paper explores the application of deep learning techniques in natural language processing tasks such as text classification, machine translation, and sentiment analysis.
        """
    }
]




function_definition = [
    {
        "type": "function",  
        "function": {
            "name": "extract_paper_info",
            "description": "Extract title and year from research papers",
            "parameters": {}
        }
    }
]

# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = 'object'

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    'title': {
        'type': 'string',
        'description': 'Title of the research paper'
    },
    'year': {
        'type': 'string',
        'description': 'Year of publication of the research paper'
    }
}

# (Optional but recommended)
function_definition[0]['function']['parameters']['required'] = ['title', 'year']

print(function_definition)



client = OpenAI(api_key=api_key)

def get_reponse(messages, tools): 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice='auto'
    )

# Extract tool call 
    return response.choices[0].message.tool_calls[0].function.arguments


print(get_reponse(messages, function_definition))


# =========================================================

# Exercise - Extracting the response 
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")





messages = [
    {
        "role": "system",
        "content": "You extract sentiment and key product features from customer reviews."
    },
    {
        "role": "user",
        "content": """
        I recently bought this smartphone and I'm really impressed!
        The battery life is amazing and lasts all day.
        The camera quality is excellent, especially in low light.
        However, the phone feels a bit heavy.
        Overall, I love it.
        """
    }
]



# Function definition (tool)
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract sentiment and key features from customer reviews",
            "parameters": {
                "type": "object",
                "properties": {
                    "sentiment": {
                        "type": "string",
                        "description": "Overall sentiment of the review (positive, negative, neutral)"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Key product features mentioned in the review"
                    }
                },
                "required": ["sentiment", "features"]
            }
        }
    }
]


client = OpenAI(api_key=api_key)

def get_reponse(messages, tools): 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice='auto'
    )

# Extract tool call 
    return response


response = get_reponse(messages, function_definition)

# Function to extract dictionary from response
def extract_dictionary(response):
    arguments = response.choices[0].message.tool_calls[0].function.arguments
    return json.loads(arguments)  # Convert JSON string → Python dict

# Print extracted structured data
print(extract_dictionary(response))

