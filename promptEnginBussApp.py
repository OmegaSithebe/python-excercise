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



