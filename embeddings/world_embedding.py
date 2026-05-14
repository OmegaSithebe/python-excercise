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

