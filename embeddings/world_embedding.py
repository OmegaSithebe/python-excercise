# Embeddings: script demo for OpenAI text embeddings + t-SNE dimensionality reduction.
# This script prints output only (no plotting).

import os

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI


def get_client() -> OpenAI:
    """Create an OpenAI client using OPENAI_API_KEY from .env."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Create a .env file with: OPENAI_API_KEY=..."
        )
    return OpenAI(api_key=api_key)


def create_embedding(client: OpenAI, text: str, model: str = "text-embedding-3-small") -> list[float]:
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding


def create_embeddings(client: OpenAI, texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    response = client.embeddings.create(model=model, input=texts)
    return [item.embedding for item in response.data]


def reduce_embeddings_tsne(embeddings_array: np.ndarray, random_state: int = 42) -> np.ndarray:
    """Reduce embeddings to 2D using t-SNE."""
    try:
        from sklearn.manifold import TSNE
    except ImportError:
        raise RuntimeError(
            "scikit-learn is not installed. Install it to use t-SNE visualization."
        )

    n_samples = embeddings_array.shape[0]
    # t-SNE perplexity must be < n_samples.
    max_perplexity = max(1, (n_samples - 1) // 3)
    perplexity = min(30, max_perplexity)

    tsne = TSNE(
        n_components=2,
        random_state=random_state,
        learning_rate="auto",
        init="random",
        perplexity=perplexity,
    )
    return tsne.fit_transform(embeddings_array)


def main() -> None:
    client = get_client()

    # --- Exercise - Creating embeddings (single input) ---
    response_dict = client.embeddings.create(
        model="text-embedding-3-small",
        input="This can contain any text.",
    ).model_dump()

    print(response_dict)
    print(response_dict["data"][0]["embedding"])
    print(response_dict["usage"]["total_tokens"])

    # --- Investigating the Vector Space (Working with Multiple Embeddings) ---
    articles = [
        {"headline": "Government announces new tax reform", "topic": "politics"},
        {"headline": "Local team wins national championship", "topic": "sports"},
        {"headline": "New AI model beats humans at chess", "topic": "technology"},
        {"headline": "Stock market hits record high", "topic": "business"},
        {"headline": "President meets foreign leaders for climate summit", "topic": "politics"},
        {"headline": "New law passed to improve public healthcare", "topic": "politics"},
        {"headline": "Star player scores hat-trick in final match", "topic": "sports"},
        {"headline": "Olympic committee announces new events", "topic": "sports"},
        {"headline": "Breakthrough in quantum computing announced", "topic": "technology"},
        {"headline": "Tech company releases next-gen smartphone", "topic": "technology"},
        {"headline": "Global oil prices see significant drop", "topic": "business"},
        {"headline": "Startup raises millions in funding round", "topic": "business"},
        {"headline": "Scientists discover new species in rainforest", "topic": "science"},
        {"headline": "Space agency plans mission to Mars", "topic": "science"},
        {"headline": "New movie breaks box office records", "topic": "entertainment"},
        {"headline": "Famous actor wins international award", "topic": "entertainment"},
    ]

    headlines = [article["headline"] for article in articles]
    print(headlines)

    # Batch embeddings for all headlines.
    embeddings = create_embeddings(client, headlines)

    response_dict = client.embeddings.create(
        model="text-embedding-3-small",
        input=headlines,
    ).model_dump()

    print(response_dict["data"])

    for i, article in enumerate(articles):
        article["embedding"] = embeddings[i]

    embeddings_array = np.array([article["embedding"] for article in articles])
    embeddings_2d = reduce_embeddings_tsne(embeddings_array)

    print("Reduced embeddings shape:", embeddings_2d.shape)
    print(embeddings_2d)


if __name__ == "__main__":
    main()

# - Semantic search
# - Recommendation systems
# - Text classification

# Exercise - Creating embeddings

import os
from dotenv import load_dotenv
from openai import OpenAI

#get API key from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client
client = OpenAI(api_key=api_key)

# Create a request to obtain embeddings
response = client.embeddings.create(
  model="text-embedding-3-small",
  input="This can contain any text."
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)


# Exercise - Digging into the embeddings response

# Extract the embeddings from response_dict
print(response_dict['data'][0]['embedding'])

# Extract and print the total_tokens used
print(response_dict['usage']['total_tokens'])



# Investigating the Vector Space (Working with Multiple Embeddings)
## Introduction
# In the previous class, we learned:
# - What **embeddings** are
# - How to convert text into **vectors (numbers)**
# - Why embeddings help machines understand **semantic meaning**


# Example Dataset: News Headlines

articles = [
    {"headline":"Government announces new tax reform","topic":"politics"},
    {"headline":"Local team wins national championship","topic":"sports"},
    {"headline":"New AI model beats humans at chess","topic":"technology"},
    {"headline":"Stock market hits record high","topic":"business"},

    {"headline":"President meets foreign leaders for climate summit","topic":"politics"},
    {"headline":"New law passed to improve public healthcare","topic":"politics"},
    
    {"headline":"Star player scores hat-trick in final match","topic":"sports"},
    {"headline":"Olympic committee announces new events","topic":"sports"},
    
    {"headline":"Breakthrough in quantum computing announced","topic":"technology"},
    {"headline":"Tech company releases next-gen smartphone","topic":"technology"},
    
    {"headline":"Global oil prices see significant drop","topic":"business"},
    {"headline":"Startup raises millions in funding round","topic":"business"},
    
    {"headline":"Scientists discover new species in rainforest","topic":"science"},
    {"headline":"Space agency plans mission to Mars","topic":"science"},
    
    {"headline":"New movie breaks box office records","topic":"entertainment"},
    {"headline":"Famous actor wins international award","topic":"entertainment"},
]


# Goal:We want to **convert each headline into an embedding vector**.


# Embedding Multiple Inputs
# Instead of sending **one API request per headline**, we can send **all headlines together**.
# This is called **batch embedding**, and it is **much more efficient**.


# Extract Headlines
# We extract all headlines using list comprehension.

headlines= [article["headline"] for article in articles]
print(headlines)

['Government announces new tax reform', 'Local team wins national championship', 'New AI model beats humans at chess', 'Stock market hits record high', 'President meets foreign leaders for climate summit', 'New law passed to improve public healthcare', 'Star player scores hat-trick in final match', 'Olympic committee announces new events', 'Breakthrough in quantum computing announced', 'Tech company releases next-gen smartphone', 'Global oil prices see significant drop', 'Startup raises millions in funding round', 'Scientists discover new species in rainforest', 'Space agency plans mission to Mars', 'New movie breaks box office records', 'Famous actor wins international award']


# Creating Embeddings for Multiple Inputs
# Now we generate embeddings for **all headlines at once**.
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

response=client.embeddings.create(
model="text-embedding-3-small",
input=headlines
)

response_dict = response.model_dump()
print(response_dict['data'])


# # Storing Embeddings in the Dataset
# Now we add each embedding back into the **articles dataset**.
# We use **enumerate()** to match the index.

for i, article in enumerate(articles):
    article["embedding"] = response.data[i].embedding
    
# Now the dataset looks like this:
    {
"headline":"Government announces new tax reform",
"topic":"politics",
"embedding": [0.123,-0.532,0.231, ...]
}
# Each article now contains its vector representation.

# # Embedding Vector Length
# One important property of OpenAI embedding models:
# The vector length is **always the same**, regardless of input size.

# Understanding High-Dimensional Vector Space
# Each embedding is a point in **1536-dimensional space**.
# But humans cannot visualize **1536 dimensions**.
# So we reduce it to **2 dimensions** for visualization.
# This process is called **Dimensionality Reduction**.


# Dimensionality Reduction
# Dimensionality reduction converts:
#     So we can plot it on a **2D graph**.
# Many techniques exist:
# - PCA
# - UMAP
# - t-SNE
# Today we use **t-SNE**.

# What is t-SNE?
# t-SNE stands for:
# **t-distributed Stochastic Neighbor Embedding**
# Purpose:
# - Reduce high dimensional vectors
# - Preserve **similarity relationships**
# - Allow **visualization**
# Important note:
# Some information is lost during reduction, so it should be used mainly for **visualization**.


try:
    from sklearn.manifold import TSNE
except ImportError:
    TSNE = None

import numpy as np
embeddings = [article["embedding"] for article in articles]
embeddings_array = np.array(embeddings)

if TSNE is not None:
    # t-SNE requires perplexity < n_samples.
    n_samples = embeddings_array.shape[0]
    max_perplexity = max(1, (n_samples - 1) // 3)  # common rule-of-thumb
    perplexity = min(30, max_perplexity)

    tsne = TSNE(
        n_components=2,
        random_state=42,
        learning_rate="auto",
        init="random",
        perplexity=perplexity,
    )
    embeddings_2d = tsne.fit_transform(embeddings_array)
    print("Reduced embeddings shape:", embeddings_2d.shape)
    print(embeddings_2d)
else:
    print("scikit-learn is not installed. Install it to use t-SNE visualization.")


# ==========================================================

# Embeddings: script demo for OpenAI text embeddings + t-SNE dimensionality reduction.
# This script prints output only (no plotting).

# import os

# import numpy as np
# from dotenv import load_dotenv
# from openai import OpenAI


# def get_client() -> OpenAI:
#     """Create an OpenAI client using OPENAI_API_KEY from .env."""
#     load_dotenv()
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise RuntimeError(
#             "Missing OPENAI_API_KEY. Create a .env file with: OPENAI_API_KEY=..."
#         )
#     return OpenAI(api_key=api_key)


# def create_embedding(client: OpenAI, text: str, model: str = "text-embedding-3-small") -> list[float]:
#     response = client.embeddings.create(model=model, input=text)
#     return response.data[0].embedding


# def create_embeddings(client: OpenAI, texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
#     response = client.embeddings.create(model=model, input=texts)
#     return [item.embedding for item in response.data]


# def reduce_embeddings_tsne(embeddings_array: np.ndarray, random_state: int = 42) -> np.ndarray:
#     """Reduce embeddings to 2D using t-SNE."""
#     try:
#         from sklearn.manifold import TSNE
#     except ImportError:
#         raise RuntimeError(
#             "scikit-learn is not installed. Install it to use t-SNE visualization."
#         )

#     n_samples = embeddings_array.shape[0]
#     # t-SNE perplexity must be < n_samples.
#     max_perplexity = max(1, (n_samples - 1) // 3)
#     perplexity = min(30, max_perplexity)

#     tsne = TSNE(
#         n_components=2,
#         random_state=random_state,
#         learning_rate="auto",
#         init="random",
#         perplexity=perplexity,
#     )
#     return tsne.fit_transform(embeddings_array)


# def main() -> None:
#     client = get_client()

#     # --- Exercise - Creating embeddings (single input) ---
#     response_dict = client.embeddings.create(
#         model="text-embedding-3-small",
#         input="This can contain any text.",
#     ).model_dump()

#     print(response_dict)
#     print(response_dict["data"][0]["embedding"])
#     print(response_dict["usage"]["total_tokens"])

#     # --- Investigating the Vector Space (Working with Multiple Embeddings) ---
#     articles = [
#         {"headline": "Government announces new tax reform", "topic": "politics"},
#         {"headline": "Local team wins national championship", "topic": "sports"},
#         {"headline": "New AI model beats humans at chess", "topic": "technology"},
#         {"headline": "Stock market hits record high", "topic": "business"},
#         {"headline": "President meets foreign leaders for climate summit", "topic": "politics"},
#         {"headline": "New law passed to improve public healthcare", "topic": "politics"},
#         {"headline": "Star player scores hat-trick in final match", "topic": "sports"},
#         {"headline": "Olympic committee announces new events", "topic": "sports"},
#         {"headline": "Breakthrough in quantum computing announced", "topic": "technology"},
#         {"headline": "Tech company releases next-gen smartphone", "topic": "technology"},
#         {"headline": "Global oil prices see significant drop", "topic": "business"},
#         {"headline": "Startup raises millions in funding round", "topic": "business"},
#         {"headline": "Scientists discover new species in rainforest", "topic": "science"},
#         {"headline": "Space agency plans mission to Mars", "topic": "science"},
#         {"headline": "New movie breaks box office records", "topic": "entertainment"},
#         {"headline": "Famous actor wins international award", "topic": "entertainment"},
#     ]

#     headlines = [article["headline"] for article in articles]
#     print(headlines)

#     # Batch embeddings for all headlines.
#     embeddings = create_embeddings(client, headlines)

#     response_dict = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=headlines,
#     ).model_dump()

#     print(response_dict["data"])

#     for i, article in enumerate(articles):
#         article["embedding"] = embeddings[i]

#     embeddings_array = np.array([article["embedding"] for article in articles])
#     embeddings_2d = reduce_embeddings_tsne(embeddings_array)

#     print("Reduced embeddings shape:", embeddings_2d.shape)
#     print(embeddings_2d)


# if __name__ == "__main__":
#     main()



# Implementing t-SNE in Python
# We use **scikit-learn**, a popular machine learning library.

# Parameter -	Meaning
# n_components -	number of dimensions (2 for visualization)
# perplexity -	controls how clusters are formed


# Interpreting the Visualization
# When we plot the embeddings, something interesting happens.
# Articles with **similar topics appear close together**.

# Key Takeaways
# 1. How to embed **multiple inputs**
# 2. How to **store embeddings in datasets**
# 3. That embeddings always have **fixed vector length (1536)**
# 4. How to reduce dimensions using **t-SNE**
# 5. How to **visualize embeddings**
# Important concept:
# Embeddings map **text with similar meaning closer together in vector space**.


# Exercise - Embedding product descriptions
import os
from dotenv import load_dotenv
from openai import OpenAI


# Each product contains:
# title
# description (this is what we care about)
# price, category, etc.
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    },
    {
        "title": "Wireless Noise-Canceling Headphones",
        "short_description": "Premium over-ear headphones with active noise cancellation and up to 30 hours of battery life.",
        "price": 249.99,
        "category": "Electronics",
        "features": [
            "Active noise cancellation",
            "Bluetooth 5.2 connectivity",
            "Comfort-fit ear cushions",
            "40mm high-fidelity drivers"
        ]
    },
    {
        "title": "4K Ultra HD Smart TV",
        "short_description": "A 55-inch smart TV with 4K resolution, HDR support, and built-in streaming apps.",
        "price": 699.99,
        "category": "Electronics",
        "features": [
            "55-inch 4K UHD display",
            "HDR10+ support",
            "Voice remote with Alexa",
            "Built-in streaming apps"
        ]
    },
]

# 2. Extract the text you want to embed
short_descriptions = [product["short_description"] for product in products]

# 3. What is an embedding?
# An embedding is:
# A list of numbers (vector) that represents the meaning of a sentence.
# Why embeddings matter
# They allow machines to understand meaning, not just keywords.

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=api_key)

# 4. Sending text to OpenAI to convert to vectors
# Create embeddings properly
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=short_descriptions
)

# Extract embeddings
product_embeddings = [item.embedding for item in response.data]

# Attach embeddings back to products
for product, embedding in zip(products, product_embeddings):
    product["short_description_embedding"] = embedding

print("Created embeddings for product short_description fields.")

# This allows semantic search.
# Example:
# User searches:
# "Good headphones for travel"
# Instead of matching words like "headphones", the system:
# Converts the query to embedding
# Compares it to all product embeddings
# Finds the closest match

# "Embeddings convert text into numbers that capture meaning.
# This allows us to compare sentences by meaning instead of exact words, enabling smarter search and recommendations."

# Semantic search is an AI-powered technique that understands the contextual meaning and intent behind a user's query, rather than just matching exact keywords. It uses Natural Language Processing (NLP) and vector embeddings to grasp the relationship between words, resulting in more relevant, accurate search results, even if query terms don't match the content.
# Key Aspects of Semantic SearchIntent Interpretation: Analyzes what the user actually wants (e.g., to purchase vs. to inform) rather than just what they typed.Context Awareness: Considers location, search history, and word relationships (e.g., understanding "football" means "soccer" in the USA).Vector Embeddings: Transforms text into numerical vectors, mapping them into a space where similar meanings are clustered together for comparison.Beyond Keywords: Unlike traditional search (e.g., SQL LIKE or basic Lucene search), it moves beyond exact term matching to conceptual searching
# How It WorksEmbedding: The system converts text data (documents, queries) into vector embeddings using machine learning models.Indexing: These vectors are stored and indexed for fast retrieval, often using vector databases.Similarity Search: When a query is made, it is also converted into a vector, and the system finds the closest vectors (most relevant documents) in the vector space using techniques like k-nearest neighbor (kNN)Semantic search is an AI-powered technique that understands the contextual meaning and intent behind a user's query, rather than just matching exact keywords. It uses Natural Language Processing (NLP) and vector embeddings to grasp the relationship between words, resulting in more relevant, accurate search results, even if query terms don't match the content.
# Key Aspects of Semantic SearchIntent Interpretation: Analyzes what the user actually wants (e.g., to purchase vs. to inform) rather than just what they typed.Context Awareness: Considers location, search history, and word relationships (e.g., understanding "football" means "soccer" in the USA).Vector Embeddings: Transforms text into numerical vectors, mapping them into a space where similar meanings are clustered together for comparison.Beyond Keywords: Unlike traditional search (e.g., SQL LIKE or basic Lucene search), it moves beyond exact term matching to conceptual searching
# How It WorksEmbedding: The system converts text data (documents, queries) into vector embeddings using machine learning models.Indexing: These vectors are stored and indexed for fast retrieval, often using vector databases.Similarity Search: When a query is made, it is also converted into a vector, and the system finds the closest vectors (most relevant documents) in the vector space using techniques like k-nearest neighbor (kNN)


