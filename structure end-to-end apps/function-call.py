# 1.2 Extracting structured data from text
# To use this information in applications, we often need to convert it into **structured data**.
# **Function calling** helps us extract this information reliably.

# 3. Using Function Calling to Extract Data
# Instead of simply prompting the model to return JSON, we can **define a function** that specifies exactly what data we want.
# This is done using the **`tools` parameter** in the OpenAI API request.
# The model will then return the output following the **function structure**.

# Key Takeaways
# - Function calling can extract **structured data from unstructured text**.
# - Functions are defined using the **`tools` parameter**.
# - The response is returned inside **`tool_calls`**.
# - This approach improves **reliability and automation** in AI applications.


# Exercise
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variable from the dotenv (environment)
load_dotenv()

# initialize & create an openai api key variable
api_key = os.getenv('OPENAI_API_KEY')

#catch error for openai api key
if not api_key:
    raise ValueError('OpenAI API key not loaded properly, please check the environment file (.env)')

#create client variable
client = OpenAI(api_key=api_key)


#Real estate agency list
message_listing = """

1. RE/MAX
House Type: Apartment
Location: Johannesburg, Gauteng
Price: ZAR 850,000
Bedrooms: 2
House Type: Freehold House
Location: Pretoria, Gauteng
Price: ZAR 1,750,000
Bedrooms: 3

2. Century 21
House Type: Townhouse
Location: Sandton, Gauteng
Price: ZAR 1,200,000
Bedrooms: 2
House Type: Villa
Location: Cape Town, Western Cape
Price: ZAR 4,500,000
Bedrooms: 5

3. Pam Golding Properties
House Type: Luxury Apartment
Location: Cape Town CBD, Western Cape
Price: ZAR 3,200,000
Bedrooms: 2
House Type: Beach House
Location: Durban, KwaZulu-Natal
Price: ZAR 6,800,000
Bedrooms: 4

4. Seeff Property Group
House Type: Duplex
Location: Midrand, Gauteng
Price: ZAR 1,350,000
Bedrooms: 3
House Type: Cottage
Location: Stellenbosch, Western Cape
Price: ZAR 2,100,000
Bedrooms: 2

5. Harcourts
House Type: Cluster Home
Location: Randburg, Gauteng
Price: ZAR 1,600,000
Bedrooms: 3
House Type: Farmhouse
Location: Bloemfontein, Free State
Price: ZAR 2,900,000
Bedrooms: 4

"""

# create tool and function 
# function_definition = [
#     {
#         'type': 'function', 
#         'function': {
#             'name': 'function_definition',
#             'description': 'You are developing an AI application for a real estate agency and have been asked to extract some key data from listings: house type, location, price, number of bedrooms. ',
#             'parameters': {
#                 'type': 'object',
#                 'properties': {
#                     'agency': {
#                         'type': 'string',
#                         'description': 'The name of the agency mentioned in the real estate list'
#                     },
#                     'house_type': {
#                         'type': 'string',
#                         'description': 'What type of house mentioned in the real estate list '
#                     },
#                     'location': {
#                         'type': 'string',
#                         'description': 'Where is the real estate located mentioned in the real estate list'
#                     },
#                     'price': {
#                         'type': 'integer',
#                         'description': 'How much does the real estate cost, mentioned in the real estate list'
#                     }, 
#                     'number_of_bedrooms': {
#                         'type': 'integer',
#                         'description': 'How many bedrooms are in the real estate, mentioned in the real estate list'
#                     }
#                 }
#             }
#         }
#     }
# ]


#create response function
response = client.chat.completions.create(
    model='gpt-4.1-mini',
    messages = [
        {'role': 'user', 'content': message_listing}
        ],
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'extract_real_estate_data',
                'description': 'Extract structured real estate data from listings',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'agency': {'type': 'string'},
                        'house_type': {'type': 'string'},
                        'location': {'type': 'string'},
                        'price': {'type': 'integer'},
                        'bedrooms': {'type': 'integer'}
                    },
                    'required': ['agency', 'house_type', 'location', 'price', 'bedrooms']
                }
            }
        }
    ],
    #the model may ignore function unless specified
    tool_choice='auto'
)

print(response.choices[0].message.tool_calls[0].function.arguments)



# Building a function dictionary
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

        Title: Attention Is All You Need
        Authors: Ashish Vaswani, Noam Shazeer
        Published in: NeurIPS, 2017

        Abstract:
        This paper introduces the Transformer architecture, a novel neural network design based solely on attention mechanisms, removing the need for recurrence and convolution.

        Research Paper:

        Title: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
        Authors: Jacob Devlin, Ming-Wei Chang
        Published in: NAACL, 2018

        Abstract:
        This paper presents BERT, a method of pre-training language representations that can be fine-tuned for a wide range of NLP tasks.
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


# Extracting the response
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