# Calling APIs in Python (requests Library)
import requests

url="https://api.artic.edu/api/v1/artworks/search"

params= {
"q":"seaside"
}

response=requests.request("GET",url,params=params)

data=response.json()

print(data)




# An **API (Application Programming Interface)** allows **different software systems to communicate with each other**.
# Example:
# - Weather API → returns weather data
# - Maps API → returns location data

# Element >	Purpose
# URL >	API endpoint
# params >	input values for API
# GET >	type of request
# response.json() >	converts response to Python dictionary


# Packaging the API Call as a Function
import requests

def get_artwork(keyword):
    url="https://api.artic.edu/api/v1/artworks/search"

    params= {
    "q":keyword
        }

    response=requests.get(url,params=params)

    return response.json()


# Providing Context to the Model
# The model needs **clear instructions** on what to do.

# We provide **system messages** to guide it.

# Example instruction:

# > Interpret the user message and extract **one keyword** that describes the artwork preference.
# >


# Adding the Function to Tools
tools = [
    {
        'type': 'function',
        'funtion': {
            'name': 'get_artwork',
            'description': 'Get artwork recommendation based on museum collection',
            'parameeters': {
                'type': 'object',
                'properties': {
                    'keyword': {
                        'type': 'string',
                        'description': 'Keyword describing artwork preference'
                    }
                },
                'required': ['keyword']
            }
        }
    }
]

# The model will:
# 1. Extract keyword from user input
# 2. Pass it to **get_artwork()**
# 3. Retrieve artwork results


# Handling the Model Response
import json

response=client.chat.completions.create(...)

if response.choices[0].finish_reason=="tool_calls":

message=response.choices[0].message

function_call=message.tool_calls[0].function

function_name=function_call.name

arguments=json.loads(function_call.arguments)


# Proper corrected code, complete with function call handling:
import json
import os
from openai import OpenAI

# Initialize the OpenAI client
# Set your API key as environment variable: set OPENAI_API_KEY=api_key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define tools for the model
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_artwork',
            'description': 'Get artwork recommendation based on museum collection',
            'parameters': {
                'type': 'object',
                'properties': {
                    'keyword': {
                        'type': 'string',
                        'description': 'Keyword describing artwork preference'
                    }
                },
                'required': ['keyword']
            }
        }
    }
]

# Call the API with proper parameters
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            "role": "system",
            "content": "You are an art expert. Extract the keyword from the user's message."
        },
        {
            "role": "user",
            "content": "I'm looking for a seaside artwork"
        }
    ],
    tools=tools,
    tool_choice="auto"
)

# Handle the model response
if response.choices[0].finish_reason == "tool_calls":
    message = response.choices[0].message
    function_call = message.tool_calls[0].function
    function_name = function_call.name
    arguments = json.loads(function_call.arguments)
    
    print(f"Function called: {function_name}")
    print(f"Arguments: {arguments}")
    
    
    
# Processing API Response
# Different APIs return data in different formats.
# We often need to **extract useful fields**.


# Post-Processing the Response
# Sometimes the API response contains:
# - unnecessary fields
# - nested data
# - large datasets


# Summary
# Concept	> Meaning
# API	> Communication between systems
# requests library >	Used to call APIs in Python
# function calling >	Model triggers external functions
# tools >	List of available functions
# finish_reason="tool_calls" >	Indicates function was called
# JSON parsing >	Extract function arguments


# Exercise
# Defining a function with external APIs

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function to pass to tools
function_definition = [{"type": "function",
                        "function" : {"name": "get_airport_info",
                                      "description": "This function calls the Aviation API to return the airport code corresponding to the airport in the request",
                                      "parameters": {"type": "object",
                                                     "properties": {"airport_code": {"type": "string","description": "The code to be passed to the get_airport_info function."}} }, 
                                      "result": {"type": "string"} } } ]

def get_response(function_definition):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system', 'content': 'You are an assistant that extracts the airport code from the user message and calls the get_airport_info function.'
            },
            {
                'role': 'user', 'content': 'What is the airport code for John F. Kennedy International Airport?'
            }
        ]
    )

response = get_response(function_definition)
print(response)




# Calling an external API

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Call the Chat Completions endpoint 
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are an assistant that extracts the airport code from the user message and calls the get_airport_info function."},
    {"role": "user", "content": "I'm planning to land a plane in JFK airport in New York and would like to have the corresponding information."}],
  tools=function_definition)

print(response)



# Handling the response with external API calls
import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load API Keys
# -----------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
aviation_api_key = os.getenv("AVIATION_API_KEY")

client = OpenAI(api_key=api_key)

# -----------------------------
# 🔥 External API Function
# -----------------------------
def get_airport_info(airport_code: str):
    url ="https://api.aviationstack.com/v1/airports"

    params = {
        "access_key": aviation_api_key,   
        "iata_code": airport_code         
    }


    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API failed with status {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# 🧠 get_response FUNCTION
# -----------------------------
def get_response(messages, tools):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # ✅ Check if tool was called
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        function_call = tool_call.function

        print("🔧 Function Called:", function_call.name)

        # Parse arguments safely
        arguments = json.loads(function_call.arguments)
        airport_code = arguments.get("airport_code")

        print("✈️ Extracted Airport Code:", airport_code)

        # Call external API
        api_result = get_airport_info(airport_code)

        return api_result

    else:
        return message.content


# -----------------------------
# Tool Definition
# -----------------------------
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "get_airport_info",
            "description": "Extract airport code and fetch airport details",
            "parameters": {
                "type": "object",
                "properties": {
                    "airport_code": {
                        "type": "string",
                        "description": "Airport code like JFK, KTM, LHR"
                    }
                },
                "required": ["airport_code"]
            }
        }
    }
]

# -----------------------------
# Messages
# -----------------------------
messages = [
    {
        "role": "system",
        "content": "You are an aviation assistant. Extract airport codes from user queries."
    },
    {
        "role": "user",
        "content": "Give me info on QATAR AIR PORT."
    }
]

# -----------------------------
# Run
# -----------------------------
result = get_response(messages, function_definition)

print("\n✅ Final Result:")
print(result)