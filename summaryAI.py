#Prompt We Send to the Model
# Update the following biography:
# - Change the name to Sarah
# - Change pronouns to she/her
# - Change job title to Senior Software Engineer

# """
# Alex is a software developer. He works at a startup and loves teaching programming.
# """
# We use **triple quotes (`"""`)** to clearly separate:- Instructions- The text to be edited. This makes long or multi-line text easy to handle.

#E.g. 
# chat = """
# Customer: My internet is very slow.
# Agent: I’m sorry to hear that. Have you tried restarting the router?
# Customer: Yes, but it didn’t help.
# Agent: I will escalate this issue to our technical team.
# """
# prompt =f"Summarize the following customer support chat in 2 sentences:\n{chat}"
#AI Output - The customer reported slow internet issues that were not resolved by restarting the router. The agent escalated the issue to the technical team for further investigation.

import os
from dotenv import load_dotenv
from openai import OpenAI

#Load the environment variable
load_dotenv()

#Initialize the API key
api_key = os.getenv('OPENAI_API_KEY')

#Check if api_key loads
if not api_key:
    raise ValueError('OpenAI API key not loaded: Please check api key variable on the environment file (.env)')

# #Creating client
client = OpenAI(api_key=api_key)

# //Find & Replace first challenge
# prompt="""Replace car with plane and adjust phrase:
# A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# response = client.chat.completions.create(
#     model='gpt-4o-mini',
#     max_completion_tokens=100,
#     messages=[
#         {'role': 'user', 'content': prompt}
#     ]
# )

# print(response.choices[0].message.content)

#//Text Summarization challenge

finance_text = """
Essential financial content focuses on improving financial literacy through budgeting, saving, investing, and debt management. Key topics include creating a budget, understanding credit, building an emergency fund, and investing to grow wealth, often delivered via blogs, social media "finfluencers," and expert, evergreen content. 
Key Financial Content Pillars & Tips
Budgeting & Savings: Spend less than you earn, automate savings, and track expenses.
Investing Basics: Diversify portfolios using stocks, bonds, or mutual funds to combat inflation.
Credit & Debt Management: Understand how credit scores work and aim to reduce high-interest debt.
Financial Literacy: Utilize resources like Investopedia and finfluencer content to understand complex topics such as inflation, taxes, and market trends.
Consumer Trends: Many are adopting minimalist, cost-cutting approaches to, for example, high school fees and mortgage debt. 
Effective financial content often simplifies complex ideas, provides actionable tips, and, as seen with ERNIE and Premium Bonds, uses storytelling to engage audiences. 
"""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# # Create a request to the Chat Completions endpoint
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[{"role": "user", "content": prompt}],
#   max_completion_tokens=400
# )

# print(response.choices[0].message.content)



#//Calculating the cost

max_completion_tokens = 100

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")


#That’s about **one-tenth of a cent**. Important for production:- Long documents- Large user traffic- Powerful models. Costs can grow quickly.**Always estimate token usage before deploying at scale.**


