# Unstructured Text Example
# We are hiring a Data Scientist to join our team in New York.
# The candidate should have experience with Python, machine learning, and data analysis.

# Structured Data Format
# {
#   "job": "Data Scientist",
#   "location": "New York"
# }

# Structured data is easier to:
# - Store in databases
# - Process in applications
# - Use for automation

# Using Function Calling to Extract Data
# Instead of simply prompting the model to return JSON, we can define a function** that specifies exactly what data we want.
# This is done using the **`tools` parameter** in the OpenAI API request.
# The model will then return the output following the **function structure

# Implementing Function Calling
# tools = [
#   {
#     "type": "function",
#     "function": {
#       "name": "extract_job_info",
#       "description": "Extract job information from text",
#       "parameters": {
#         "type": "object",
#         "properties": {
#           "job": {
#             "type": "string",
#             "description": "The job title mentioned in the text"
#           },
#           "location": {
#             "type": "string",
#             "description": "The office location mentioned in the text"
#           }
#         }
#       }
#     }
#   }
# ]


# Understanding the Function Structure
#  1. Type
# "type": "function"
# This tells the API that we are defining a **user-created function**.
#  2. Function Name
# "name": "extract_job_info"

# The name identifies the function that the model can call.
#  3. Description
# "description": "Extract job information from text"
# The description tells the model **what the function should do**.


#  Parameters
# The parameters section defines what data we want to extract.
# "parameters": {
#   "type": "object",
#   "properties": {
#     "job": {...},
#     "location": {...}
#   }
# }
# "job": {
#   "type": "string",
#   "description": "The job title mentioned in the text"
# }


# Example Response
# {
#   "tool_calls": [
#     {
#       "function": {
#         "name": "extract_job_info",
#         "arguments": {
#           "job": "Data Scientist",
#           "location": "New York"
#         }
#       }
#     }
#   ]
# }


# Class Exercise Idea:
# Our company is hiring a Machine Learning Engineer in London.
# The role requires experience with Python and TensorFlow.
# {
#  "job": "Machine Learning Engineer",
#  "location": "London"
# }