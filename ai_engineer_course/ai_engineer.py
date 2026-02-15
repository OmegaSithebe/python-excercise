#WHat is OpenAI? - is a company that: researches & develop artificial intelligence systems - builds powerful AI models (is a data structure to handle certain work(e.g AI Models to predict the text - these models are fed with lot of data called training the AI Model(machine learning) the company OpenAI does the training)- Makes them available to developers - one of their famous development is chatGPT
#AI models which is trained on hospital data, reason for RAG (Retrieval-Augmented Generation - is a rapidly growing AI framework designed to enhance the accuracy, relevance, & reliablity of Large Language Models (LLMs) by connecting them to external, trusted knowledge base) systems is because not all data we do not know if the model has complete knowledge/idea of our information/data. That is where the RAG come in the middle, the rag uses the rag systems called rag workflow. We store our data in a database, then we search data ourselves from our storage. With that information we send to the model. Here is my data, can you look at this data & give an answer back based on my information & not yours. You (AI) predict answer based on my information given. That is why when it said built knowledge bot it is based on your data, your knowledge. 
#What OpenAI actually provides - Language models (LLMs) to predict -> (text, chat, reasoning) - Image models - Speech models - Embedding models (have lot of data, you need a model that will take the data & embedd, break it down & put it somewhere. Break it down to a certain size of data, that's called embedding (take that data & later can be stored in a database.) we use models for embedding, managing our data, break down our data. )
#What is ChatGPT? - A **ready-made application - Runs in a web browser - Designed for humans to chat with AI 
#OpenAI is a company, which develops artificial intelligence systems & chatGPT is one of their product. 
#Simple comparison: ChatGPT - OpenAI API | Web app - Developer tool | Used by humans - Used by code | Manual input - Automated | Fixed UI - Fully customizable | For personal use - For apps, startups, companies


# uv add openai 

from chatai_engineer import OpenAI # Create a client (make sure your OPENAI_API_KEY is set in your environment)

key = "sk-proj-HayZxDGrniwhoT8k33cSqjtwCTZ1L-X riDLJAMfygvJGHRiLtLFsMhQ624ZRX5dhitmxQE yRLjT3BLbkFJbgNsr_Jp2ewjGatNUvx0d5LmLIV NmqWav9@LIJ11HxtFxxuJhCy_3k6NFohQjLsTAX 700IixsA"

client = OpenAI(key)# Replace the prompt below with your own question or instruction

prompt = "Could you explain about OpenAI"

response = client.chat.reponse.create(
    model="gpt-4o-mini",
    input=prompt,
)

print(response)