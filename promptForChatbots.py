# 4.1 Prompt Engineering for Chatbot DevelopmentPrompt engineering is the process of **designing instructions (prompts)** that guide a chatbot to behave and respond in the way we want.👉 In chatbot development, prompts decide:- **Who the chatbot is**- **What it knows**- **How it responds to users**

## Why Do Chatbots Need Prompt Engineering?Chatbots interact with **many unpredictable users**.Even if we have past data (search queries, FAQs), **we cannot predict every question** a user will ask.### Why prompt engineering is important:- Helps guide chatbot behavior- Improves accuracy and reliability- Ensures consistent responses- Keeps chatbot focused on its domain📌 **Without good prompts:**The chatbot may give vague, incorrect, or irrelevant answers.📌 **With good prompts:**The chatbot answers confidently and correctly, even for new questions.

## Chatbot Prompt Engineering Using the OpenAI APIWhen building chatbots using the **OpenAI API**, we don’t send just one prompt.Instead, we send a **list of messages**, and **each message has a role**.### Common roles:- **System** → Defines chatbot behavior- **User** → User’s question- **Assistant** → Chatbot’s responseUntil now, we mostly focused on **user prompts**,but for chatbot development, **system messages are the most important**.

## Why System Messages Are CrucialSystem messages:- Control how the chatbot behaves- Define its role, tone, and limitations- Apply to **every user interaction**👉 Think of the system message as the **brain or rulebook** of the chatbot.

## Chat Completions Endpoint for ChatbotsThe **chat completions endpoint** is ideal for chatbot development.### How it works:- Messages are sent as a **list**- Each message has a **role**- The chatbot responds based on **all previous messages**

## System Message: Response GuidelinesSystem messages should also define **how the chatbot should respond**.You can specify:- Target audience- Tone (formal, friendly, neutral)- Answer length- Output structure### Example:For a financial chatbot:> “Respond in a formal, precise, and objective manner.”> If a user asks:> “What do you think about cryptocurrencies?”> 📌 The chatbot will:- Start with a definition- Explain advantages- Explain disadvantages- End with a neutral summaryThis keeps the response **balanced and professional**.

## Key Takeaways- Prompt engineering is essential for chatbot reliability- System messages guide chatbot behavior- Define:    - Purpose    - Response style    - Behavior limits- Chat completion endpoint is ideal for chatbot development- Well-written system prompts = smarter chatbots 🚀


# **Exercise**
# **Creating a dual-prompt get_response() function**
import os
from dotenv import load_dotenv
from openai import OpenAI

#Load the environment variable
load_dotenv()

#get & create the environment variable
api_key = os.getenv('OPENAI_API_KEY')

#catch error if OpenAI API key not loaded
if not api_key:
    raise ValueError('API key not loaded: Check environment file (.env)')

#create OpenAI API client
client = OpenAI(api_key=api_key)

#create get response function
def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("You are an expert data scientist that explains complex concepts in understandable terms", "Define AI")
print(response)



# Behavioral control of a customer support chatbot
# Define the technical issue condition
technical_issue_condition = "I'm sorry to hear about your issue with ... if the user is reporting a technical issue."

# Create the refined system prompt
refined_system_prompt =f"""

```{base_system_prompt}```

```{order_number_condition}```
```{technical_issue_condition }```

"""

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)