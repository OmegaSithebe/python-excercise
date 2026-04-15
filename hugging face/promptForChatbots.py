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

# system_prompt = 'You are a Software Engineer/Developer, your job is to instruct a huge banking corporate company how & ways to go from physical paper work to using electronic systems & secure cloud websites for easy & anywhere access transmissions.'

# user_prompt = 'I have a client paper work from UK England and my banking corporate company is here in South Africa. I want to get here in South Africa, verify it and then send it back to England ASAP but I fear the process is going to take forever the back & forth. Any other solutions you can recommend for me & including our company?'

#create get response function
def get_response(system_prompt, user_prompt):
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}]
    response = client.chat.completions.create(
        model='gpt-4o-mini', messages=messages, max_completion_tokens=450, temperature=0
    )
    return response.choices[0].message.content


# Try the function with a system and user prompts of your choice 
response = get_response("You are an expert data scientist that explains complex concepts in understandable terms", "Define AI")
print(response)



# Behavioral control of a customer support chatbot
# Define the technical issue condition
technical_issue_condition = '''
If the user is reporting a technical issue, 
start your response with:
'I'm sorry to hear about your issue with ...'
and then continue with helpful troubleshooting steps.
'''

base_system_prompt = '''
You are a professional and polite customer support chatbot.
You help customers with orders, deliveries, refunds and technical issues.
Your responses should be clear, concise and helpful.
'''

order_number_condition = '''
If a user asks about an order but does not provide an order number, 
politely ask them to share their order number before proceeding.
'''
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


# 4.2 Role-playing prompts for chatbots
## What Are Role-Playing Prompts?Role-playing prompts instruct a chatbot to **act as a specific role**, just like an actor playing a character in a movie or play 🎭.Instead of giving **generic answers**, the chatbot:- Adopts a specific **tone**- Uses suitable **vocabulary**- Follows the **behavior of the assigned role**📌 This makes chatbot responses **more realistic, professional, and useful**.

## Why Role-Playing Prompts Matter in Chatbot DevelopmentRole-playing prompts are especially useful for:- Domain-specific chatbots (finance, healthcare, tech, education)- Customer support systems- Professional advisory chatbots
### Benefits:- More accurate responses- Better user experience- Consistent personality and expertise- Clear separation of responsibilities📌 The chatbot learns how roles behave from its **training data**, but we must **explicitly instruct it** using prompts.

## Understanding Role-Playing with an Example### Scenario:We are building a chatbot for a **high-tech product company**.A user asks:> “Can you explain the technical specifications of this product?”> We define **three possible roles** for the chatbot.---
### 🧑‍💼 Role 1: Customer Support Agent**How this role responds:**- Gives general guidance- Avoids deep technical details- Redirects users to official resources- Offers help politely**Example response:**> “You can find the complete specifications on our official website. If you need help choosing the right product, I’d be happy to assist.”>

## Implementing Role-Playing PromptsTo implement role-playing, we **explicitly tell the model what role to play**.This is commonly done using **system messages** when working with the **OpenAI API**.
### Example Prompt:**System message:**> “You are an expert financial analyst.”> **User message:**> “Give retirement planning advice for people nearing retirement.”> 📌 The chatbot now responds like a **real financial expert**, not a general assistant.

## Role-Playing with Additional RequirementsRole-playing **does not replace** other prompt rules.We still need to specify:- Behavior limits- Topic boundaries- Response guidelines
### Example:**System message:**> “You are a technology journalist. Answer only technology-related questions. For other topics, say that you specialize in technology.”> **User asks:**> “Tell me about American literature.”> **Chatbot replies:**> “I specialize in technology and the tech industry, so I’m unable to help with literature-related topics.”> 📌 This keeps the chatbot:- Focused- Accurate- Domain-specific

## Key Takeaways- Role-playing prompts make chatbots act like real professionals- Same question can have different answers based on role- Roles affect tone, depth, and vocabulary- Adding traits makes role-playing more realistic- Role-playing should be combined with behavior rules

# Exercise
# Learning advisor chatbot

# Craft the system_prompt using the role-playing approach
system_prompt = " act as a learning advisor who can interpret learner queries as described and provide the relevant textbook recommendations. specify the role of a learning advisor and the instruction to recommend beginner and advanced textbooks based on their background?"

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)



# **Adding guidelines for the learning advisor chatbot**

#Create a base prompt 
base_system_prompt = 'Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options.'

#Define behaviour guidelines
behavior_guidelines = 'ask a user about their background, experience, and goals, whenever any of these were not provided in a prompt.'

#Define reponse guidelines
response_guidelines = 'recommend no more than three textbooks.'

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = """
Hey, I'm looking for courses on python and data visualization. What do you recommend? 
"""

response = get_response(system_prompt, user_prompt)
print(response)



# 4.3 Incorporating external context
## What Is External Context?External context means **extra information that we provide to a chatbot**, which the model does not already know from its training.👉 This information helps the chatbot give **accurate, relevant, and useful answers** to users.

## Why Do Chatbots Need External Context?When we build a chatbot using the **OpenAI API**, we are using a **pre-trained language model (LLM)**.### Important limitation:LLMs only know:- Information from their training data- Up to a specific **knowledge cut-off date**📌 But in real applications, chatbots often need:- Company-specific data- Recent updates- Private or internal informationThat’s why we must **inject external context**.

# Why Is Some Information Missing in LLMs?There are **two main reasons** why a chatbot may not know something.---
### 🔹 Reason 1: Knowledge Cut-OffLanguage models are trained **up to a certain date**.If you ask about events **after that date**, the model:- May say it doesn’t know- Or may guess (hallucinate) if not guided properly### Example:A model trained up to 2021 is asked:> “What are the financial trends in 2023?”> **Possible response:**> “I’m sorry, but as of my last update in 2021, I don’t have information about financial trends in 2023.”> 📌 This happens because the information did not exist during training.

### Reason 2: Private or Non-Public InformationSome information is **never available online**, so the model cannot learn it.### Example:You ask a chatbot acting as a study buddy:> “Who is my favorite instructor?”> 📌 The model cannot know this because:- It’s personal information- It was never part of public training data

## How Do We Provide Extra Information to a Chatbot?To solve this problem, we **explicitly give context** to the chatbot.There are **two common ways**:1. Sample conversations2. System prompt with embedded context

## Method 1: Using Sample Conversations We can guide the chatbot by showing **example conversations**.### Example:**System message:**> “You are a customer service chatbot.”> **User message:**> “What services do you offer?”> **Assistant message:**> “We offer web development, mobile app development, and software consulting.”> Now, when a user asks:> “How many services do you offer?”> 📌 The chatbot can infer the answer from the sample conversation.### ⚠️ Limitation:- Requires many example Q&A pairs- Not scalable for large or complex information

## Method 2: Providing Context in the System Prompt (Best Approach)A **more effective and cleaner method** is to include external context directly in the **system prompt**.### Example Scenario:A company called **ABC Tech Solutions** wants the chatbot to know about its services.### System Prompt:> “You are a customer support chatbot for ABC Tech Solutions.> > > The company offers the following services:> > 1. Web application development> 2. Mobile app development> 3. Custom software solutions>     >     Respond clearly and professionally.”>     ### User asks:> “What services does your company provide?”> 📌 The chatbot answers correctly using the context:- Web application development- Mobile app development- Custom software solutions

## Why System Prompt Context Works Better- Centralized information- Easy to update- No need for many example conversations- Works well with purpose and behavior rules📌 This method is ideal for:- Company chatbots- Product chatbots- Educational assistants- Internal tools

## Important Limitation: Context SizeLLMs can only handle a **limited amount of context**.### What this means:- Small to medium context → works well- Very large documents or databases → not ideal📌 For large-scale context (e.g., thousands of documents), more advanced techniques are required (covered in advanced courses).

## Key Takeaways- LLMs do not know everything- Missing information is due to:    - Knowledge cut-off    - Private or non-public data- External context improves chatbot accuracy- System prompts are the best way to inject context- Context size is limited and must be managed carefully


# Exercise
# Providing context through sample conversations

#Define the system prompt
system_prompt = 'You are a customer service chatbot for MyPersonalDelivery, a delivery service that offers a wide range of delivery options for various items. You should respond to user queries in a gentle way.'

context_question = 'What types of items can be delivered using MyPersonalDelivery?'
context_answer = 'We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special hand'

# Add the context to the model
def get_response(system_prompt, context_question, context_answer):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': context_question},
                {'role': 'assistant', 'content': context_answer} ,
                {'role': 'user', 'content': 'Do you deliver for hazardous materials or extremely fragile items?'}],
        max_completion_tokens=450,
        temperature=0
    )
    return response.choices[0].message.content

response = get_response(system_prompt, context_question, context_answer)
print(response)


# Providing context through system prompt
service_description = """MyPersonalDelivery is a fast and reliable delivery service that helps customers
send and receive everyday items with ease. The service delivers groceries,
medicines, electronics, clothing, documents, and small household items.

MyPersonalDelivery offers same-day delivery for groceries and medicines in most
cities, affordable pricing, real-time order tracking, and friendly customer
support. The goal of the service is to make daily deliveries simple, safe, and
stress-free for customers."""

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

def get_response(system_prompt, user_prompt):
    client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=450,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0
    )

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)
print(response)