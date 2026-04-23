#WHat is OpenAI? - is a company that: researches & develop artificial intelligence systems - builds powerful AI models (is a data structure to handle certain work(e.g AI Models to predict the text - these models are fed with lot of data called training the AI Model(machine learning) the company OpenAI does the training)- Makes them available to developers - one of their famous development is chatGPT
#AI models which is trained on hospital data, reason for RAG (Retrieval-Augmented Generation - is a rapidly growing AI framework designed to enhance the accuracy, relevance, & reliablity of Large Language Models (LLMs) by connecting them to external, trusted knowledge base) systems is because not all data we do not know if the model has complete knowledge/idea of our information/data. That is where the RAG come in the middle, the rag uses the rag systems called rag workflow. We store our data in a database, then we search data ourselves from our storage. With that information we send to the model. Here is my data, can you look at this data & give an answer back based on my information & not yours. You (AI) predict answer based on my information given. That is why when it said built knowledge bot it is based on your data, your knowledge. 
#What OpenAI actually provides - Language models (LLMs) to predict -> (text, chat, reasoning) - Image models - Speech models - Embedding models (have lot of data, you need a model that will take the data & embedd, break it down & put it somewhere. Break it down to a certain size of data, that's called embedding (take that data & later can be stored in a database.) we use models for embedding, managing our data, break down our data. )
#What is ChatGPT? - A **ready-made application - Runs in a web browser - Designed for humans to chat with AI 
#OpenAI is a company, which develops artificial intelligence systems & chatGPT is one of their product. 
#Simple comparison: ChatGPT - OpenAI API | Web app - Developer tool | Used by humans - Used by code | Manual input - Automated | Fixed UI - Fully customizable | For personal use - For apps, startups, companies


# uv add openai 

# from chatai_engineer import OpenAI # Create a client (make sure your OPENAI_API_KEY is set in your environment)

# key = "sk-proj-HayZxDGrniwhoT8k33cSqjtwCTZ1L-X riDLJAMfygvJGHRiLtLFsMhQ624ZRX5dhitmxQE yRLjT3BLbkFJbgNsr_Jp2ewjGatNUvx0d5LmLIV NmqWav9@LIJ11HxtFxxuJhCy_3k6NFohQjLsTAX 700IixsA"

# client = OpenAI(key)# Replace the prompt below with your own question or instruction

# prompt = "Could you explain about OpenAI"

# response = client.chat.reponse.create(
#     model="gpt-4o-mini",
#     input=prompt,
# )

# print(response)



# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# # Optional: check if key is loaded
# if not api_key:
#     raise ValueError("OPENAI_API_KEY not found in .env file")





# messages = [
#     {
#         "role": "system",
#         "content": "You extract the title and year of publication from research papers."
#     },
#     {
#         "role": "user",
#         "content": """
#         Research Paper:

#         Title: Deep Learning for Natural Language Processing
#         Authors: John Smith, Sarah Johnson
#         Published in: Journal of AI Research, 2021

#         Abstract:
#         This paper explores the application of deep learning techniques in natural language processing tasks such as text classification, machine translation, and sentiment analysis.
#         """
#     }
# ]




# function_definition = [
#     {
#         "type": "function",  
#         "function": {
#             "name": "extract_paper_info",
#             "description": "Extract title and year from research papers",
#             "parameters": {}
#         }
#     }
# ]

# # Define the function parameter type
# function_definition[0]['function']['parameters']['type'] = 'object'

# # Define the function properties
# function_definition[0]['function']['parameters']['properties'] = {
#     'title': {
#         'type': 'string',
#         'description': 'Title of the research paper'
#     },
#     'year': {
#         'type': 'string',
#         'description': 'Year of publication of the research paper'
#     }
# }

# # (Optional but recommended)
# function_definition[0]['function']['parameters']['required'] = ['title', 'year']

# print(function_definition)



# client = OpenAI(api_key=api_key)

# def get_reponse(messages, tools): 
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=messages,
#         tools=tools,
#         tool_choice='auto'
#     )

# # Extract tool call 
#     return response.choices[0].message.tool_calls[0].function.arguments


# print(get_reponse(messages, function_definition))


import os
from dotenv import load_dotenv #the library (dotenv - the module you import)
from openai import OpenAI

# is a function call, not a variable. It is a method from the python-dotenv library used to load environment variable from a .env file into your system's environment(accessible via os.environ).
# The function: load_dotenv() - the action of loading the file. The return value: it returns a Boolean (true or false - if it found it or not)
load_dotenv()

# this line is an assignment statement that retreives a specific piece of information from your computer's environment & saves it for use in your script. api_key: This is a variable. In python, it is a string (str) type, because environment variables are always stored and retreived as text. os.getenv('...'): This is a method call from python's built-in os module. It searches your system's environment for a key named 'OPEN_API_KEY'
api_key = os.getenv('OPENAI_API_KEY')

# check api_key variable string has loaded successfully or not
if not api_key:
    raise ValueError("api_key not found, please check naming or the .env file")

message_listing = """
    Beautiful 3-bedroom apartment for sale in New York.
    This modern apartment is listed at $750,000
"""


# Preloaded function definition
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
                        'description': 'Type of the property (e.g, apartment, house)'
                    }, 
                    'location': {
                        'type': 'string',
                        'description': 'Location of the property'
                    },
                    'price': {
                        'type': 'string',
                        'description': 'Price of the property'
                    }, 
                    'bedrooms': {
                        'type': 'integer',
                        'description': 'Number of bedrooms'
                    }
                },
                'required': ['house_type', 'location', 'price', 'bedrooms']
            }
        }
    }
]

# This line is an object instsatiation. It creates a 'tool' (an object) that your code uses to talk to OpenAI's servers.
# - client: this is a variable. Its type is an instance (or object) of the OpenAI class. Think of it as a remote control programmed specifically to handle your requests.
# - OpenAI(...): This is the constructor. It's like a factory function that builds the client.
# - api_key=api_key: This is a keyword argument. You are talking the string stored in your api_key variable and handling it to the constructor so the client knows how to authenticate your account.
# 1. load_dotenv(): Finds your secret file.
# 2. os.getenv(): Grabs the specific key from that file.
# 3. OpenAI(): Plugs that key into the "remote control" (client) so you can finally ask the AI to do things.
client = OpenAI(api_key=api_key)

# This is a function definition that sends a prompt to the AI & specifically tells it how to use tools (like functions written) to give you structured data.
# def get_response(...): defining a custom function. It takes two inputs: the user's message and the function (the tool definition)
# client.chat.completions.create: This is a method call that sends a request to the OpenAI's API.
# model='gpt-40-mini': This specifies which 'brain' you want to use
# messages=[...]: This is a list of dictionaries.
## System Role: Sets the 'personality' or rules for the AI.
## Use Role: This is the actual text/question you passed into your function
# tools=function: This passes in a list of tolls (usually JSON schemas) that the AI is  allowed to 'call'
# tool_choice='auto': This tells the AI to decide for itself whether it should just talk back normally or use one of the tools you provided.
# The Result: The variable response will be an object containing the AI's answer of the specific data it extracted to fill your function's arguments. 


def get_response(message, function):
    response = client.chat.completions.create(
        model='gpt-4.1-mini',
        messages=[
            {'role': 'system', 'content': 'You are an assistant that extracts structured data'},
            {'role': 'user', 'content': message}
        ],
        tools=function,
        tool_choice='auto'
    )

    #Extract tool call
    return response.choices[0].message.tool_calls[0].function.arguments

print(get_response(message_listing, function_definition))
