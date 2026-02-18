# **Multi-turn conversation** means:- The user and AI talk **back and forth**- Each new message **remembers previous messages**This is how chatbots like **ChatGPT** work.

## Assistant Messages in Conversations:A conversation is built using a **series of messages**:- system → rules- user → question- assistant → replyThe model always generates a response to the **latest user message**, using:- the system message- all previous user & assistant messages

### Important IdeaIf we **store the assistant’s reply** and send it again with the next user message,we can continue the conversation. This is exactly how real AI chatbots work behind the scenes.

## How a Conversation Is Built (Concept)To build a conversation, we follow these steps:1. User sends a message2. Assistant generates a response3. That response is **saved**4. Both are sent again with the **next user message**Repeat

## Why Conversation History MattersBecause the model sees the **full conversation history**, it understands context.

# Coding a Multi-Turn Conversation in Python


### Step 1: Define the System Message - This sets the behavior of the assistant.
# messages = ['role': 'system', 'content': 'You are a helpful Python tutor.']

### Step 2: Create User Questions - We will ask **multiple related questions**.
# user_qs = ['Why is Python popular?', 'Summarize the above answer in one sentence.']

### Step 3: Loop Through Questions - We want a response for **each question**, so we use a loop.
# for question in user_qs:

### Step 4: Add User Message to Conversation - Convert the question into a message and store it.
# user_message = {'role': 'user', 'content':question}
# messages.append(user_message)

### Step 5: Send Messages to the Model - The model now sees the **full conversation**.
    # response = client.chat.completions.create(
    #     model="gpt-4.1-mini",
    #     messages=messages
    # )

### Step 6: Extract Assistant Response - Get the assistant’s reply and store it.
    # assistant_message = {"role":"assistant","content": response.choices[0].message.content
    # }
    # messages.append(assistant_message)
    
### Step 7: Print the Conversation - So we can clearly see what’s happening.    
# print("User:", question)print("Assistant:", assistant_message["content"])print()



## Result: A Real Conversation - The second question:> “Summarize the above answer in one sentence”works **without repeating the explanation**, because:- the assistant’s previous reply is stored- the model has full context This proves that **multi-turn conversations are working correctly**.

## Key Takeaways (Very Important) Multi-turn chat requires:- storing user messages- storing assistant replies- sending the full message list every time The model **does not remember anything by itself** **We must send conversation history manually**

# Summary Table
# Concept-	Meaning
# Single-turn-	One question, one answer
# Multi-turn-	Back-and-forth conversation
# Messages list-	Stores full conversation
# Context-	Previous messages sent again



## Practice Time ## Practice Task for Students
# Build a chatbot that:- introduces itself- answers a Python question- summarizes its own previous answer
#  Hint:- use a `messages` list- append both user and assistant messages

### Final Thought> Multi-turn conversations are the **foundation of all AI chatbots**.> Once you understand this, you can build **real chat applications**.


import os
from dotenv import load_dotenv
from openai import OpenAI

#Load environment variable
load_dotenv()

#Get & initialize environment variable
api_key = os.getenv('OPENAI_API_KEY')

#Catch error if not loaded/found
if not api_key:
    raise ValueError('API key not loaded/found. Please check environment file (.env)')

#Create OpenAI API client
client = OpenAI(api_key=api_key)

messages = [
    {'role': 'system', 'content': 'You are a helpful math tutor that speaks concisely'},
    {'role': 'user', 'content': 'Explain what pi is.'}
]

#Send the chat messages to the model
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages,
    max_completion_tokens=100
)

#Extract the assistant message from the response
assistant_dict = {'role': 'assistance', 'content': response.choices[0].message.content}

#Add assistant_dict to the messages dictionary
messages.append(assistant_dict)

print(messages)