import os
from dotenv import load_dotenv
from openai import OpenAI

#Load the environment variables
load_dotenv()

#Get & intialize the environment variable
api_key = os.getenv('OPENAI_API_KEY')

#Catch API key error if not loaded
if not api_key:
    raise ValueError('API key not loaded: Please check environment file (.env)')


#create OpenAPI client
client = OpenAI(api_key=api_key)

# prompt = """Give the eye catching slogan for a restaurant with Italian, Chinese food and fine-dining, fast-food etc """

# #Create a request to the chat completions endpoint
# response = client.chat.completions.create(
#     model='gpt-4o-mini',
#     max_completion_tokens=100,
#     messages=[
#         {'role': 'user', 'content': prompt}
#     ],
#     temperature=1
# )

# print(response.choices[0].message.content)



### 1. Text Generation. In this lesson, we’re going to learn about **text generation**—how AI models generate text and how this is used in real-world applications like chatbots, marketing, and product descriptions.
#That’s because AI models are non-deterministic, meaning they use probability to decide the next word. So even with the same prompt, the response can change slightly.
## Controlling randomness in responses. In many situations, randomness is **not a good thing**.For example:- In a **customer support chatbot**, we don’t want different answers for the same question.- But at the same time, we want the model to understand **different user inputs**.This is where the **temperature** parameter comes in.- **Temperature = 0** → very predictable, almost the same answer every time- **Temperature = 1** → balanced (default)- **Temperature = 2** → very creative and random.If we increase the temperature, the response may become more unusual or creative—sometimes even strange. So there’s always a **trade-off between consistency and creativity**.


# Create a detailed prompt
# prompt = """
# I need a product description for SonicPro headphones, wireless headphone with 40 hour of battery life. Active noise cancellation (ANC), foldable design
# """

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}],
#     # Experiment with max_completion_tokens and temperature settings
#     max_completion_tokens=100,
#     temperature=2
# )

# print(response.choices[0].message.content)





#Short prompting
# But the big question is: **how do we get better and more accurate answers from the AI?**The answer is by writing **better prompts**.

#Prompting examples
#One powerful way to improve AI answers is by **giving examples inside the prompt**.When we show the AI what we want, it understands our expectation more clearly.This technique is called **shot prompting**.

## What is Shot Prompting?**Shot prompting** means adding examples to your prompt to guide the AI.
# There are **three main types**:- **Zero-shot prompting**    👉 No examples, only instructions.- **One-shot prompting**    👉 One example is given.- **Few-shot prompting**    👉 Multiple examples are given.The more examples we give, the better the AI understands the task.

## Why is Shot Prompting Important?Giving examples helps AI perform better in many tasks, such as:
# - **Classification** – putting text into categories- **Sentiment analysis** – finding emotions like positive or negative- **Data extraction** – pulling specific information from text. In short: **better prompts = better results**.

## Zero-Shot Prompting (No Examples)
# Let’s say we want the AI to rate restaurant reviews from **1 to 5**:- 1 = very bad- 5 = amazing
# In **zero-shot prompting**, we only give instructions, like:> “Give a number from 1 to 5 for each review.”
# Because we didn’t show any example, the AI:- gave the number **and**- added extra text like **“Neutral”**, which we didn’t ask for.So the result was **not exactly what we wanted**.

## Zero-Shot Prompting (No Examples)
# Let’s say we want the AI to rate restaurant reviews from **1 to 5**:- 1 = very bad- 5 = amazing
# In **zero-shot prompting**, we only give instructions, like:> “Give a number from 1 to 5 for each review.”
# Because we didn’t show any example, the AI:- gave the number **and**- added extra text like **“Neutral”**, which we didn’t ask for.So the result was **not exactly what we wanted**.

## One-Shot Prompting (One Example)
# Now we add **one example** before the real reviews.Example:> “The food was terrible → 1”Then we give the new reviews
# This helps the AI understand:- only the **number** is needed- the **format** we want.Now the output is cleaner and more accurate.

## Few-Shot Prompting (Multiple Examples)
# Next, we add **two or three examples**.This is called **few-shot prompting**.With more examples:- formatting becomes **consistent**- scores become **more reasonable**


## Exercise - **Zero-shot prompting with reviews**
# prompt = """Classify the sentiment of each review from 1 to 5.:
# 1. Unbelievably good!
# 2. Shoes fell apart on the second use.
# 3. The shoes look nice, but they aren't very comfortable. 
# 4. Can't wait to show them off!"""

# # Create a request to the Chat Completions endpoint
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[{"role": "user", "content": prompt}],
#   max_completion_tokens=100
# )

# print(response.choices[0].message.content)


# # Exercise - One-shot prompting: will it be enough?
# # Add the example to the prompt
# prompt = """Classify sentiment as 1-5 (negative to positive):
# 1. Love these! = 5
# 2. Unbelievably good! = 
# 3. Shoes fell apart on the second use. = 
# 4. The shoes look nice, but they aren't very comfortable. = 
# 5. Can't wait to show them off! =
 
#  """

# response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
# print(response.choices[0].message.content)


# Few-shot prompting: all the examples!
# Add the final example
# prompt = """Classify sentiment as 1-5 (negative to positive):
# 1. ____
# 2. Love these! = 5
# 3. Unbelievably good! = 
# 4. Shoes fell apart on the second use. = 
# 5. The shoes look nice, but they aren't very comfortable. = 

# """

# response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
# print(response.choices[0].message.content)

# Add the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = """

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)
