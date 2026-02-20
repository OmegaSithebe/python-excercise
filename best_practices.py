## What Is Prompt Engineering?
# **Prompt engineering** means:> Writing clear and well-structured instructions (prompts) for AI models to get the output we want.

### Simple Definition- Prompt engineering = **how you ask the question matters**

## Prompt Engineering Is Like a Recipe 🍳Think of prompt engineering like **cooking a meal**.- Ingredients → words in your prompt- Recipe → structure of your prompt- Dish → AI response
### 🧠 Key IdeaJust like a chef carefully chooses ingredients,we carefully choose **words, instructions, and examples**.

### The Three Roles
### 🟦 SystemGives **instructions** to the AIControls behavior and rules 'System: You are a helpful Python tutor.'

### User - The **prompt or question** from the user 'User: What is a variable in Python?'

### Assistant - The **AI’s reply** 'Assistant: A variable is used to store data.'

## Recap: Control Parameters - The API provides parameters to control responses. 
### Temperature - Controls randomness (0 → 2)
# | Value | Behavior |
# | --- | --- |
# | 0 | Very accurate & consistent |
# | 1 | Balanced |
# | 2 | Very creative & random |
#  For learning & explanations → use temperature = 0


#  Creating a get_response() Function
import os
from dotenv import load_dotenv
from openai import OpenAI

#Load the environment variable
load_dotenv()

#Initialize & Get the environment variable
api_key = os.getenv('OPENAI_API_KEY')

#Catch API key error if not loaded
if not api_key:
    raise ValueError('API key not loaded: Please check environment file (.env)')

#Create OpenAI API client
client = OpenAI(api_key=api_key)


#creating a get response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content

response = get_response('What is prompt engineering?')
print(response)




## Improving Prompts (Very Important) - ### Improved Prompt```Explain prompt engineering ina waya5-year-old can understand```✔️ Result:- simpler words- friendly explanation- real-life comparison
### Example Response Style> Prompt engineering is like telling your friend exactly what you want so they can help you better.

## Final Summary✔️ Prompt engineering = asking better questions✔️ Clear prompts → better AI answers✔️ System, user, assistant roles matter✔️ Temperature controls creativity✔️ Small prompt changes can improve output a lot


# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing event for my friend merrage"}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)


#Practice exercise for creating a poem OpenAI ChatBot with function
prompt2 = 'Generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand.'

#Creating a get_poem function
def get_poem(prmpt2):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'system', 'content': 'You are deep philosophical poet, that challenges & explore the human nature.'},
            {'role': 'user', 'content': prompt2},
            {'role': 'assistant', 'content': 'Need a poem that will challenge my thinking, perspective & belief. Not in complicated English writing but understandable.'}
        ]
    )
    return response.choices[0].message.content

response = get_poem(prompt2)
print(response)





# 1.2 Key principles of prompt engineering
## Three Key Principles of Prompt Engineering
# We’ll focus on **three core principles**:1. Using **action verbs**2. Giving **detailed and precise instructions**3. Writing **well-structured prompts using delimiters**

### Good Action Verbs- write- explain- describe- summarize- compare- evaluate- list

## Avoid Ambiguous Verbs - Some verbs are **unclear** and should be avoided.### ❌ Ambiguous Verbs- think- understand- feel- try- knowThese verbs do not tell the model **what output you want**.

## Formulating Detailed InstructionsGood prompts also include **details**, such as:- context- output format- length- style- target audience

### Example❌ Too broad:```Tellme about dogs```✅ Detailed prompt:```Describe the behavior and characteristics of Golden Retrievers and explain why they are  suitable for families```👉 More detail = more accurate output.

## Limiting Output LengthSometimes we want:- short answers- summaries- limited explanationsThere are **two ways** to control length.

### Method 1: Using `max_tokens`- Enforces a **hard limit**- May cut responses mid-sentence ❌

### Method 2: Specify Length in Prompt (Recommended)```Explain Python in no more than 3 sentences```✔️ More natural✔️ Usually complete answers

## Understanding Prompt ComponentsA prompt often has **two parts**:1. **Instruction** → what to do2. **Input data** → content to work on

## Using Delimiters for Well-Structured PromptsTo avoid confusion, we **separate input data** using delimiters.### 🔹 Common Delimiters- (triple backticks)- """ """- [ ]  [ ]- ( )---
### 🧪 Example```Summarize the following text in one paragraph:```Artificial intelligence is transforming industries...👉 Delimiters clearly tell the model:- where input starts- where input ends

## Using Python f-Strings for Prompts- Instead of writing long text inside the prompt, we can store it in a variable.### 🧪 Example```python text ="Artificial intelligence is transforming industries..."prompt = f"""Summarize the following text in one sentence:```{text}```"""```✔️ Cleaner code✔️ Easier to reuse✔️ Perfect for long inputs👉 This pattern will be used **a lot** in the course.

## Final Summary (For Students)✔️ Use **action verbs**✔️ Avoid vague language✔️ Give **clear and detailed instructions**✔️ Control output length clearly✔️ Use delimiters for structured prompts✔️ Use f-strings for dynamic prompts

# Practice Tasks - Task 1
# Think about climate change - (You are a weather forecast specialist/analysis & your job is to give helpful, accurate answers & feedbacks based on the questions asked about weather, climate, global matters or anything of that matter. The weather this days has been raining heavily especially on the south coast of South Africa. I reside in Cape Town South Africa & it has been raining heavily in the afternoon but sunny in the meanwhile, what could be the problem. Respond in a clear, concise manner that is direct & clearly to understand & follow.)

#Task 2
# Write a prompt that:- explains JavaScript- targets beginners- uses max 5 sentences


# Using delimited prompts with f-strings
# 2. What is a "Delimited" Prompt?A delimiter is a sequence of characters used to mark the beginning and end of a specific block of text. This helps the AI understand exactly where the "instructions" end and the "story content" begins. Common delimiters: """, ---, ###, or <story>.Example: ### Once upon a time... ### (The ### are the delimiters).

# Story to be completed
story = 'As of today, when I wake up I realize that I am a consscious being. Being aware of this I also realize that my choices, decisions & action not only affect me but...'

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""
 
#Create a get response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0
    ) 
    
    return response.choices[0].message.content

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


# Building specific and precise prompts
# Story to be completed
story = 'As of today, when I woke up I realized that I am a conscious being. Being aware of this I also realize that my choices, decisions & action not only affect me but...'

system = 'In the style of Shakespare'

assistant = 'in only two paragraphs'

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""
 
#Create a get response function
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        max_completion_tokens=150,
        messages=[
            {'role': 'user', 'content': prompt},
            {'role': 'system', 'content': system},
            {'role': 'assistant', 'content': assistant}
        ],
        temperature=0
    ) 
    
    return response.choices[0].message.content

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)




# 1.3 Structured outputs and conditional prompts
## What Are Structured Outputs?By default, language models generate **plain text**.They **do not automatically** create:- tables- lists- formatted paragraphs- custom layouts👉 If we want structured output, we must **explicitly tell the model** what format to follow.

## Generating TablesTo generate a table, we must:- clearly say **“create a table”**- specify the **column names**### 🧪 Example: Table Prompt```Create a table with the following columns: Title and Rating.List five popular action movies.```

## Generating ListsLists are useful when we want:- rankings- steps- collections of items### 🧪 Example: Numbered List```Generate a numbered list of the top five cities to visit in Europe.```👉 Output will be:1. City 12. City 23. City 3

## Structured ParagraphsSometimes we want paragraphs with:- headings- subheadings- organized sectionsTo achieve this, we must **mention the structure in the prompt**.---### 🧪 Example Prompt```Write a structured paragraph about the benefits of exercise.Use the following headings:- Introduction- Physical Health Benefits- Mental Health Benefits```

## Custom Output FormatsSometimes, we need **custom formats** that don’t fit tables or lists.### 🔹 Best ApproachBreak the prompt into:1. Instructions2. Output format3. Input text---### 🧪 Example: Custom Format (Story Title)**Input Text**```Once upon a time, there was a boy named David who loved exploring forests...```**Prompt**```You are given a story opening.Tasks:1. Generate a suitable title for the story.2. Keep the original text unchanged.Output format:Title: <generated title>Story:<originaltext>```This guarantees:- correct structure- correct content placement- predictable output

## What Are Conditional Prompts?Conditional prompts allow us to add **logic** inside prompts.Basic structure:```If conditionis true →do X Else →do Y```👉 This is similar to `if-else` in programming.

## Conditional Prompt Example (Language Check)### 🧪 Prompt```If the following text is written in English, suggest a suitable title.Otherwise, respond with: "I only understand English."Text: <inserttext here>```### ✅ Result- English text → title generated- Non-English text → "I only understand English"

## Final Summary (For Students)✔️ Models need **explicit formatting instructions**✔️ Tables require **column definitions**✔️ Lists require **format clarity**✔️ Structured paragraphs need **headings specified**✔️ Custom formats work best when broken into parts✔️ Conditional prompts allow **logic-based responses**

## Practice Tasks
### 🔹 Task 1Write a prompt to generate:- a table of 5 programming languages- columns: Name, Use Case---

### 🔹 Task 2Write a conditional prompt that:- summarizes text only if it is in English- otherwise says: "Unsupported language"---

### 🔹 Task 3Create a custom output format for:- blog title- introduction paragraph- conclusion


## Exercise
# **Generating a table**



# Customizing output format



# Using conditional prompts