# 2. Advanced Prompt Engineering Strategies
# 2.1 Few-shot promptingFew-shot prompting means **giving examples inside the prompt** before asking the real question.👉 We usually include:- Example question- Example answer- Then our actual question📌 **Idea:**“AI learns from examples just like students do.”

## **3. How Few-Shot Prompting Works**1. We write a prompt with examples2. We send it to the model3. The model **copies the pattern** from the examples4. It answers our final question in the same way🧠 The model doesn’t *remember*—it simply **follows the pattern**.


## **Types of Prompting**The name depends on **how many examples** we give:
# Examples given-	Name
# 0 examples-	Zero-shot prompting
# 1 example-	One-shot prompting
# 2 or more examples-	Few-shot prompting

## **Zero-Shot Prompting****Zero-shot prompting** means:- No examples- Just a direct question
### ✅ Example**Prompt:**```Define prompt engineering.```📌 The model answers using its **existing knowledge only**.🟢 Best for:- Simple questions- Definitions- Quick answers

## **One-Shot Prompting****One-shot prompting** means:- One example is provided- The model learns the **format or style**
### ✅ Example (Math in words)**Prompt:**```
# Example:Three plus five plus six equals 14.Question:Four plus two plus eight equals?```**Model Output:**```Four plus two plus eight equals 14.```📌 The model copied the **sentence style** from the example.

## **One-Shot Prompting (Structured Output)**We can also control **how the answer looks**.### ✅ Example**Prompt:**```
# Example:The sum of 3,5, and 6 is 14.Question:What is the sum of 4,2, and 8?```**Model Output:**```The sum of 4,2,and 8 is 14.```🟢 One example = same structure every time

## **Few-Shot Prompting****Few-shot prompting** means:- We give **multiple examples**- Useful for **complex tasks**
### ✅ Example: Sentiment Analysis**Prompt:**```Text: I love this movie.Sentiment: PositiveText: This productis terrible.Sentiment: NegativeText: The service was okay.Sentiment:```**Model Output:**```Neutral```📌 The model learns how to **classify text** from multiple examples.

## **Few-Shot Prompting in Chat Models**In chat models, examples look like **previous conversations**.
### ✅ Example (Conceptual)- **User:** I love this phone- **Assistant:** Positive- **User:** This app crashes a lot- **Assistant:** Negative- **User:** The delivery was fast➡️ The model replies:```Positive```📌 Each example is a **user message + assistant reply**.

## **Important Things to Remember**✔ For **simple tasks**→ Zero-shot or one-shot is enough✔ For **format control**→ One-shot works well✔ For **complex tasks** (classification, reasoning)→ Use few-shot prompting✔ Always:- Give **clear examples**- Cover **all categories**- Use **diverse examples**

## **Simple Summary**🧠 **Think of prompting like teaching:**- No example → student guesses- One example → student copies format- Many examples → student understands patternThat’s exactly how **few-shot prompting** works 🚀

# import os
# from dotenv import load_dotenv
# from openai import OpenAI

#load the dotenv environment variable
# load_dotenv()

#Get & initialize the environment variable
# api_key = os.getenv('GEMINI_API_KEY')

#catch API Key if not loaded
# if not api_key:
#     raise ValueError('API key not loaded: Please check environment file (.env)')

#Create OpenAI API client
# client = OpenAI(api_key=api_key)


# Create a one-shot prompt
# prompt = """
#      Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = {1, 3, 7, 19}
#      Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:
# """

#Get response function
# def get_response(prompt):
#     response = client.chat.completions.create(
#         model='gpt-4o-mini',
#         max_completion_tokens=150,
#         messages=[
#             {'role': 'user', 'content': prompt}
#         ],
#         temperature=0
#     )
    
#     return response.choices[0].message.content

# response = get_response(prompt)
# print(response)


import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError('API key not loaded: Check your .env file')

# Configure the Gemini SDK
genai.configure(api_key=api_key)

# Initialize the model (Gemini 1.5 Flash is great for small tasks)
model = genai.GenerativeModel('gemini-1.5-flash')

# Your one-shot prompt
prompt = """
     Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = {1, 3, 7, 19}
     Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:
"""

def get_response(prompt_text):
    # Temperature 0 for consistent, logical results
    response = model.generate_content(
        prompt_text,
        generation_config=genai.types.GenerationConfig(
            temperature=0
        )
    )
    return response.text

response = get_response(prompt)
print(response)




# Sentiment analysis with few-shot prompting
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




# 2.2 Multi-step prompting - This technique helps us guide the AI step by step so it gives better and more accurate answers.

## **What is Multi-Step Prompting?**Multi-step prompting means:👉 **Breaking one big task into smaller steps**👉 Telling the model **what to do in each step**This works very well for:- **Sequential tasks** (tasks with an order)- **Thinking tasks** (analysis, checking, decision-making)
### ✅ Examples of where it helps:- Writing an article from an outline- Solving a problem step by step- Checking whether code is correct📌 Just like humans, AI performs better when instructions are **clear and ordered**.

## **Multi-Step Prompts = Treasure Maps**Think of multi-step prompting like a **treasure map** 🗺️- Each step = one direction- Follow all steps → reach the treasure- Skip steps → you may get lost📌 The model doesn’t guess—it **follows your directions**.

## **Single-Step Prompt Example (Writing a Blog)**### ❌ Single-step prompt:```Write a travel blog.```### What happens?- The model chooses a **random place**- It decides the structure itself- Output may not match what we want📌 Example result:- A random trip to Iceland- Day-by-day journey- No control over structure

## **Multi-Step Prompt Example (Writing a Blog)**### ✅ Multi-step prompt:```Step1: Introduce the destination.Step2: Describe a personal adventure.Step3: Summarize the journey.```📌 Notice:- We did **not** specify the destination- We focused on **structure**, not content

## **Output from Multi-Step Prompt**### Result:- Step 1 → Introduction to Barcelona- Step 2 → Personal travel experience- Step 3 → Clear conclusion🟢 The blog is:- Well-organized- Easy to read- More professional

## **Single-Step Code Evaluation (Problem)**Imagine we have Python code for:- Addition- Subtraction- Multiplication- Division### ❌ Single-step prompt:```Is this code correct?```### Problem:- Model may say **“Yes”**- No explanation- No deep checking📌 Example issue:- Syntax is correct- But division by zero is **not handled**

## **Multi-Step Prompt for Code Analysis**### ✅ Multi-step prompt:```Step1: Check if the code syntax is correct.Step2: Check if division by zero is handled.```### Output:- Step 1 → Syntax is correct ✅- Step 2 → Division by zero is NOT handled ❌🟢 Now we get:- Clear feedback- Logical reasoning- Better evaluation

## **Multi-Step Prompt vs Few-Shot Prompt**Let’s compare them simply 👇### 🧭 Multi-Step Prompting- Uses **instructions**- Tells the model **what to do**- Like a roadmap### 📘 Few-Shot Prompting- Uses **examples**- Shows the model **how to respond**- Like learning by example

# Final Comparison (Easy Way)
# Technique-	What it uses-	Purpose
# Multi-step-	Steps / instructions-	Guide thinking & process
# Few-shot-	Examples (Q&A)-	Teach pattern or format

## **Simple Summary**🧠 **Remember this:**- Few-shot → *“Here are examples, follow them”*- Multi-step → *“Follow these steps, one by one”*💡 Best results often come when **both are combined**.

# Single-step prompt to plan a trip
# Create a single-step prompt to get help planning the vacation
prompt = "I have 2 weeks of break from my job i need to plan for a beach vacation."

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

response = get_response(prompt)
print(response)