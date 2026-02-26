# 3.1 Text summarization and expansion- ✂️ **Text Summarization**- ➕ **Text Expansion**These are two very common tasks used in **finance, marketing, customer support, emails, and reports**.

## Text Summarization### ✅ What is Text Summarization?**Text summarization** means:> Taking a long text and converting it into a **short, clear version** without losing the main meaning.> In simple words:👉 *Big text → small text, same meaning*

## How to Improve a Summarization PromptWe can improve prompts by adding:1. **Output limits**2. **Output structure**3. **Summarization focus**Let’s see each with examples 👇

## Effective Prompt – Output Limits

### 🎯 What are Output Limits?We tell the model **how long** the summary should be:- Number of sentences- Number of words- Number of characters### ✅ Example Prompt:```Summarize the following review in one sentence.```📌 Result:- The output will be **exactly one sentence**- Clear and controlled

## Effective Prompt – Output Structure

### 🎯 What is Output Structure?We tell the model **how the output should look**:- Bullet points- Numbered list- Paragraph### ✅ Example Prompt:```Summarize the review in at most three bullet points.```📌 Output:- 3 bullet point- Each point highlights a key quality (design, comfort, battery)

## Effective Prompt – Summarization Focus

### 🎯 What is Summarization Focus?We tell the model **what to focus on** while summarizing.### ✅ Example Prompt:```Summarize the review in three sentences, focusing on key features and user experience.```📌 Why this is powerful:- The model ignores unnecessary details- Highlights **strengths and weaknesses**- Very useful for product analysis

## Result ExplanationThe response:- Has **exactly three sentences**- Mentions:    - Positive feedback    - Key features    - User experience👉 This shows how **clear instructions = better output**

## Text Expansion### ✅ What is Text Expansion?**Text expansion** is the **opposite of summarization**.It means:> Taking short ideas and expanding them into **detailed, meaningful text**.> In simple words:👉 *Small text → big text*---### 🏢 Where is Text Expansion Used?- Writing **emails**- Creating **service descriptions**- Expanding **reports**- Generating **marketing content**

## Text Expansion Prompts – Key ElementsA good expansion prompt should mention:- What text to expand (usually **delimited**)- Focus areas- Output rules:    - Tone (professional, friendly)    - Length (sentences or paragraphs)    - Audience (customers, managers)

## Example: Expanding a Service Description

### 📝 Given Bullet Points:- Content creation- Community management- Audience engagement### Output Explanation:- The model:    - Writes **two sentences**    - Uses a **professional tone**    - Explains **what the service does and why it is useful**
    
## Key Takeaways✔ Text summarization shortens content✔ Text expansion grows content✔ Good prompts include:- Length rules- Structure- Focus- Tone👉 **Better prompts = better AI output**


# Exercise
import os
from dotenv import load_dotenv
from openai import OpenAI

#Load dotenv environment variable
load_dotenv()

#Get & initialize the environment variable
api_key = os.getenv('OPENAI_API_KEY')

#Catch error if api key not loaded
if not api_key:
    raise ValueError('API key not loaded: Check environment file (.env)')

#Create client variable
client = OpenAI(api_key=api_key)

report = '''

The market has seen rapid growthin the adoption of artificial intelligence across industries suchas finance, healthcare, and retail. Businesses are increasingly using AI to personalize customer experiences, automate customer support, and analyze large datasetsfor better decision-making. However,this rapid adoption has raised concerns among customers regardingdata privacy and security.

Many consumers are becoming more cautious about how their personaldatais collected, stored, and usedby AI-driven systems. Regulatory frameworks anddata protection laws are influencing how companies design their AI solutions. As a result, companies that prioritize transparency and ethicaldata practices are gaining higher customer trust and loyalty.

'''

prompt = f"""
Summarize the following market research report in a maximum of five sentences.
Focus specifically on how artificial intelligence and data privacy are shaping the market
and how they are affecting customer behavior.

Report:{report}
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=300,
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content

## Why This Prompt Works (Explain in Class)✔ **Clear task** → “Summarize the report”✔ **Output limit** → “maximum of five sentences”✔ **Clear focus** → AI and data privacy✔ **Customer perspective** → “affecting customer behavior”This ensures:- No unnecessary details- Short, business-ready summary- Relevant insights only
## Key Teaching Point (Highlight This ⭐)👉 **The power is not in the AI, but in the PROMPT**A well-written prompt:- Saves time- Improves accuracy- Delivers business-focused results


response = get_response(prompt)

print("Summarized report: \n", response)



# Use Case: Product Features Summarization (Smartphone)

product_description = '''

The smartphone features a6.7-inch AMOLED displaywith a120Hzrefresh rate, offering smooth visualsand vibrant colors. Itis poweredby a high-performance processor that ensures fast multitaskingand gaming. The device includes a5000mAh battery that supports fast charging, allowing extendedusage throughout the day.

The smartphone comeswith a triple-camerasystem, including a64MP main camera, an ultra-wide lens,and a macro sensor, delivering high-quality photosand videos. Italso offers5G connectivity, enhancedsecurity features suchas anin-display fingerprint sensor,and runson the latestversionof the operatingsystem.

'''

prompt2 = f"""
Summarize the following smartphone product description in no more than five bullet points.
Highlight the key features that would help users quickly compare and evaluate the product.

Product Description:{product_description}
"""

#Create get_response function
def get_response(prompt2):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=300,
        messages=[
            {'role': 'user', 'content': prompt2}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content


response = get_response(prompt2)

print("Summarized report: \n", response)



# Example Output (For Student Understanding)

prompt = f"""
Summarize the product description delimited by triple backticks, in at most five bullet points.
 ```{product_description}```

"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=300,
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)


# Product description expansion

# Craft a prompt to expand the product's description
prompt = f"""
expand the product description from pre-loaded string, and writes  a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
```{product_description}```
"""

#Create get_response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=300,
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)



# 3.2 Text Transformation - > Changing a given text into a new version **without changing its original meaning**.> The information stays the same, but the **form, language, tone, or quality** changes.

### Common Text Transformation Tasks- 🌍 Language translation- 🎯 Tone adjustment- 👥 Audience-based rewriting- ✍️ Grammar correction- 🧹 Writing improvement- 🔁 Multiple transformations togetherAll of these are possible using **LLMs with well-written prompts**.

## Language Translation### 🌍 Basic TranslationWhen asking the model to translate text:✔ Always mention the **input language**✔ Clearly mention the **output language**

## Tone Adjustment### 🎭 What is Tone Adjustment?Tone adjustment means:> Rewriting the same message to match a different **style or mood**> Examples of tone:- Informal- Formal- Professional- Persuasive- Friendly

## Grammar and Writing Improvements### ✍️ Proofreading (No Structural Change)If we want to:✔ Fix spelling✔ Fix grammar✔ Fix punctuation❌ Without changing structure or styleWe ask the model to **proofread**.


# Exercise
# Translation for multilingual communication
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

marketing_message = """
Discover elegance redefined with our 
latest collection of premium leather handbags. Crafted from 
the finest quality leather and designed with timeless sophistication, 
each handbag blends luxury, durability, and modern style. Perfect for work, 
travel, or special occasions, our new collection offers versatile designs that 
elevate every outfit. Experience comfort, craftsmanship, and confidence—because 
you deserve accessories as exceptional as you are.
"""

# Craft a prompt that translates
prompt = f"""Translate the marketing materials from English to French, Spanish and Japanese. make sure to check for any grammer and language correctness. ```{marketing_message}``` """

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

print("English:", marketing_message)
print(response)



# Tone adjustment for email marketing
sample_email = '''
Dear Valued Customer,

We’re pleased to share the latest updates from our store and invite you to explore our newest product arrivals. Each item has been thoughtfully selected to deliver quality, style, and value—designed with your needs and preferences in mind.

As a thank you for being part of our community, we’re also offering exclusive deals available for a limited time. This is our way of ensuring you get more from every shopping experience with us.

We look forward to supporting your journey with products you can trust and enjoy. Should you have any questions or need assistance, our team is always here to help.

Warm regards,
The Customer Care Team
'''

# Craft a prompt to change the email's tone
prompt = f"""
Transforms the sample email by changing its tone to be professional, positive and user-centric

```{sample_email}```
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)



# Writing improvement
text = """i really like this community because people share a lot of 
useful ideas. sometimes the posts are hard to read and 
there are many small mistakes, but overall the content is helpful and interesting.
i think if the writing was clearer and more polished, more users would enjoy reading
 and contributing here."""
 
 # Craft a prompt to transform the text
prompt = f"""
Generate the content from below text that can thrive.
step 1:  first proofreads the text without changing its structure, and then adjusts its tone to be formal and friendly.
step 2: Fix any grammar errors and refining writing tones to create a more polished and engaging environment for all users.
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)


# 3.3 Text analysis - Text analysis means understanding and studying text using effective prompts. In this lesson, we learn how AI models can analyze text to extract useful information.

# 2. What is Text Analysis?### **What is Text Analysis?**Text analysis is the process of examining written text to find meaningful information.In this session, we focus on two main techniques:- **Text classification**- **Entity extraction**⚠️ Note: All examples used are fictional. In real projects, companies must follow privacy laws and seek legal advice when working with customer data.

### **Text Classification**Text classification means assigning a category to a given text.**Example:**Sentiment analysis- Positive- Negative- NeutralIf a customer writes a review, the model decides which sentiment category it belongs to.

### **Classification with Specified Categories**For better results, we should **clearly mention the categories in the prompt**.**Example:**If we want to analyze the sentiment of a smartwatch review, we tell the model:- Categories: *positive, negative, neutral*- Output format: *one word only*The model then follows these instructions exactly.

### **Classification with Unspecified Categories**If we **do not specify categories**, the model uses its own knowledge.This usually works for simple tasks like sentiment analysis.However, for **complex or custom classifications**, always define categories to get predictable results.

### **Multiple Class Classification**Sometimes, a text can belong to **more than one category**.**Example:** smartwatch review may show:- Happiness- Comfort- SatisfactionBest practice:- Tell the model the **maximum number of classes** it can return- Example: *“List up to 3 emotions”*The model may respond with emotions like *impressed, positive, comfortable*.

### **Entity Extraction**Entity extraction is another form of text analysis.Here, the goal is to **extract specific information** such as:- Names- Places- Organizations- Dates- Product details

### **Entity Extraction with Specified Entities**To get accurate results, we should:- Clearly mention **which entities to extract**- Specify the **output format****Example:**From a mobile phone description, ask the model to extract:- Product name- Display size- Camera resolutionAnd format the result as an **unordered list**.

### **Applying Few-Shot Prompts to New Data**Now, suppose we receive a new ticket from a customer named **David**.We include:- Previous tickets- Their extracted entities- The new ticketThe model follows the same structure and:- Extracts relevant entities- Identifies new sub-entities (like customer ID)This ensures **consistent and structured outputs**.



## Exercise
# **Customer support ticket routing**

ticket = """Hello Support Team,

I was charged twice for my subscription this month, but I can only see one active plan in my account dashboard. I’ve already checked my payment history and bank statement, and the duplicate charge is still showing. Could you please look into this and help resolve the issue as soon as possible?

Thank you.
"""
# Craft a prompt to classify the ticket
prompt = f"""
classifies the ticket based on technical issue, billing inquiry, or product feedback, without providing anything else in the response.



```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)



# Customer support ticket analysis

# Sample tickets
ticket_1 = (
    "Hi Support Team, I’m unable to log into my account since yesterday. "
    "I keep getting an error message saying “authentication failed” even though my password "
    "is correct. My username is john.doe@email.com. Please help me fix this issue as soon as "
    "possible."
)

ticket_2 = (
    "Hello, I noticed that my credit card was charged twice for my monthly "
    "subscription on August 10, 2025. The amount charged was $49.99 each time. "
    "My order ID is ORD-45821. I’d appreciate it if you could check this and process a "
    "refund for the extra charge."
)

ticket_3 = (
    "Hey team, I just wanted to share some feedback about your new mobile app update. "
    "The interface looks much cleaner and the app feels faster, but the notification "
    "settings are a bit confusing to use. Overall, great work!"
)

ticket_4 = (
    "Good afternoon, my name is David Miller and I’m contacting you regarding a "
    "booking I made through your travel app. My reservation ID is TRV-90217 for a flight "
    "from New York to London scheduled on September 15, 2025. I need to update the passenger "
    "phone number linked to this booking. Please let me know how to proceed."
)

# Sample extracted entities
entities_1 = {
    "issue_type": "technical_issue",
    "problem": "authentication failed",
    "username": "john.doe@email.com"
}

entities_2 = {
    "issue_type": "billing_inquiry",
    "charge_amount": "$49.99",
    "charge_date": "August 10, 2025",
    "order_id": "ORD-45821",
    "request": "refund"
}

entities_3 = {
    "issue_type": "product_feedback",
    "product": "mobile app",
    "positive_feedback": ["cleaner interface", "faster performance"],
    "negative_feedback": ["confusing notification settings"]
}

# Craft a few-shot prompt
prompt = f"""
Extract entities from the new ticket using the same structure as the examples below.

sample 1:
{ticket_1}
entities:
{entities_1}

sample 2:
{ticket_2}
entities:
{entities_2}

sample 3:
{ticket_3}
entities:
{entities_3}

new ticket:
```{ticket_4}```
"""

response = get_response(prompt)

print("Ticket:\n", ticket_4)
print("Entities:\n", response)






# 3.4 Code generation and explanation
### **ntroduction**In this session, we will learn about **code generation** and **code explanation** using effective prompts. These are powerful business applications of Large Language Models (LLMs) that help developers write and understand code faster.

### **Code Generation**Code generation means creating code that solves a specific problem.This is useful in almost every software-related domain.⚠️ Important note for students:LLMs can generate code quickly, but **you must understand the code** before using it in real projects.

### **Writing Effective Code Generation Prompts**A good code-generation prompt should clearly include:- The **problem description**- The **programming language** (e.g., Python, JavaScript)- The **desired format** (function, script, class, etc.)### **Example Prompt**“Write a Python function to calculate the average sales per quarter.”### **Model Output (Example)**The model generates a function called `calculate_average_sales` that:- Takes a list called `quarterly_sales`- Adds all values- Divides by the number of elements- Returns the average

### **Code Generation Using Input–Output Examples**Sometimes, instead of describing the problem in words, we provide **input–output examples**.### **Example**- Input: `[100, 200, 300, 400]`- Output: `250`From this, the model figures out that the task is to calculate the **average**.---### **5. How the Model Understands Input–Output Examples**The model:1. Observes patterns in inputs and outputs2. Identifies the underlying logic (average calculation)3. Generates the appropriate function4. Demonstrates how it works using the given examples

### **How the Model Understands Input–Output Examples**The model:1. Observes patterns in inputs and outputs2. Identifies the underlying logic (average calculation)3. Generates the appropriate function4. Demonstrates how it works using the given examples

### **Code Modification**We don’t always need new code.We can ask the model to **modify existing code**.### **Example**Given a Python script that:- Calculates total sales- Prints the resultWe can ask the model to:- Convert it into a **function**- Return the total sales instead of printing it

### **Code Modification**We don’t always need new code.We can ask the model to **modify existing code**.### **Example**Given a Python script that:- Calculates total sales- Prints the resultWe can ask the model to:- Convert it into a **function**- Return the total sales instead of printing it

### **Multiple Code Modifications in One Prompt**We can request **multiple changes at once**.### **Example**Ask the model to:- Take user input interactively- Ensure all inputs are positive numbers- Show an error message if a value is negative- Compute total sales only if inputs are valid

### **Final Modified Code Behavior**After modification, the code:- Accepts four sales values from the user- Validates the inputs- Displays an error for negative values- Calculates and displays total sales

### **Code Explanation**Sometimes, code can be:- Long- Complex- Hard to understandLLMs can explain code clearly and quickly.

### **Code Explanation Requirements**When asking for an explanation, we should specify:- **Length** of explanation (one sentence, paragraph, detailed)- **Depth** (high-level or step-by-step)### **Example**“One-sentence explanation”→ *This code calculates the average sales per quarter.*

### **Detailed Code Explanation**For deep understanding, we ask the model to:- Explain the code **step by step**- Use a **chain-of-thought style** explanation

### **How Detailed Explanation Works**The model:1. Explains the function definition2. Describes how inputs are processed3. Explains calculations step by step4. Describes the return value5. Summarizes the overall purpose of the code

### **Key Takeaways**- LLMs can **generate**, **modify**, and **explain** code- Clear prompts lead to better results- Always review and understand generated code- Use detailed explanations when learning or debugging


# **Exercise**
# **Code generation with problem description**

# Craft a prompt that asks the model for the function
prompt = f"""write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."""

response = get_response(prompt)
print(response)




# Input-output examples for code generation
examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""
 infer the Python function that maps the inputs to the outputs in the provided examples.

 ```{examples}```

"""

response = get_response(prompt)
print(response)



# Modifying code with multi-step prompts
function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
modify the function according to the specified requirements: test if the inputs to the functions are positive, and if not, display appropriate error messages, otherwise return the area and perimeter of the rectangle.

```{function}```
"""

response = get_response(prompt)
print(response)



# Explaining code step by step
# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f""" Explain your chan-of-thought, describe the function step by step ```{function}``` """
 
response = get_response(prompt)
print(response)



