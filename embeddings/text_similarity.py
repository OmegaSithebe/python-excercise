# Text similarity
# Measuring Text Similarity with Embeddings

## 1. Introduction
# In previous classes, we learned:
# - What **embeddings** are
# - How text is converted into **vectors**
# - How embeddings are stored and visualized
# Today we will learn something very powerful:
# **How to measure similarity between two pieces of text using embeddings.**
# This ability allows us to build systems such as:
# - Semantic search
# - Recommendation engines
# - Text classification


# 2. Recap: Embeddings and Vector Space

# Embedding models convert text into **vectors (lists of numbers)**.
# Important concept:

# - **Semantically similar text → vectors close together**
# - **Semantically different text → vectors far apart**

# Text	Similarity
# teacher – student -	close
# teacher – school -	close
# teacher – car -	far

# 3. Measuring Similarity Between Vectors
# There are multiple ways to measure similarity in high-dimensional space.

# Common methods include:

# - Euclidean distance
# - Manhattan distance
# - Cosine similarity / cosine distance

# Today we will use **cosine distance**.
# 4. What is Cosine Distance?

# Cosine distance measures the **angle between two vectors**.

# Key idea:

# - Smaller cosine distance → **more similar**
# - Larger cosine distance → **less similar**


# 5. Computing Cosine Distance in Python
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

# We can compute cosine distance using a simple helper.
def cosine_distance(v1, v2):
    dot = sum(x * y for x, y in zip(v1, v2))
    norm1 = sum(x * x for x in v1) ** 0.5
    norm2 = sum(y * y for y in v2) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 1.0
    return 1.0 - dot / (norm1 * norm2)

vector1 = [1, 2]
vector2 = [2, 4]

result = cosine_distance(vector1, vector2)

print(result)


# 7. Creating a Reusable Embedding Function
# Note: The original function used OpenAI's embeddings API. To keep this
# example runnable without network/API keys we provide a simple local
# embedding fallback. This preserves the original commented information
# while making the script executable.
def create_embeddings(texts):
    """
    Create simple local embeddings for the given text or list of texts.
    This fallback creates a bag-of-words count vector over the
    vocabulary of the provided texts.
    """
    if isinstance(texts, str):
        texts = [texts]

    # build vocabulary
    vocab = {}
    for t in texts:
        for w in t.lower().split():
            if w not in vocab:
                vocab[w] = len(vocab)

    embeddings = []
    for t in texts:
        vec = [0] * len(vocab)
        for w in t.lower().split():
            vec[vocab[w]] += 1
        # normalize to unit vector to behave like typical embeddings
        norm = sum(x * x for x in vec) ** 0.5
        if norm > 0:
            vec = [x / norm for x in vec]
        embeddings.append(vec)

    return embeddings


# This function:
# - accepts **one string or list of strings**
# - returns **embeddings**

# 9. Comparing Similarity with Headlines
# Now we compute the similarity between the query and each headline.


# Step 1: Import Libraries
from scipy.spatial import distance
import numpy as np

### Step 2: Compute Distances
query = "AI and computers are semantically related"

headlines = [article["headline"] for article in articles]
all_embeddings = create_embeddings([query] + headlines)
query_embedding = all_embeddings[0]
for idx, article in enumerate(articles):
    article["embedding"] = all_embeddings[idx + 1]

# Create an empty list:
distances = []

# Loop through articles:
for article in articles:
    headline_embedding = article["embedding"]
    similarity = distance.cosine(query_embedding, headline_embedding)
    distances.append(similarity)

# Now the list contains cosine distances.


# 10. Finding the Most Similar Text
# The **most similar headline** will have the **smallest distance**.
closest_index = np.argmin(distances)

# Now we retrieve the headline.
most_similar_article = articles[closest_index]

print(most_similar_article["headline"])

# Because AI and computers are semantically related.


# 12. Key Takeaways
# Today we learned:
# 1. Embeddings allow us to measure **text similarity**
# 2. Similar texts have **vectors close together**
# 3. We measure similarity using **cosine distance**
# 4. The **smallest distance = most similar text**
# This enables powerful applications like:
# - Semantic search
# - Recommendation engines
# - Text classification


## **Exercise**
# **More repeatable embeddings**
# Define a create_embeddings function
# We use a local fallback implementation to keep this example runnable.
def create_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]

    vocab = {}
    for t in texts:
        for w in t.lower().split():
            if w not in vocab:
                vocab[w] = len(vocab)

    embeddings = []
    for t in texts:
        vec = [0] * len(vocab)
        for w in t.lower().split():
            vec[vocab[w]] += 1
        norm = sum(x * x for x in vec) ** 0.5
        if norm > 0:
            vec = [x / norm for x in vec]
        embeddings.append(vec)

    return embeddings

short_description = "A handheld device that can make phone calls and browse the internet."
list_of_descriptions = [
    "A smartphone with a large display",
    "A washing machine for homes",
    "A laptop for everyday computing",
]

# Embed short_description and print
print(create_embeddings(short_description)[0])

# Embed list_of_descriptions and print
print(create_embeddings(list_of_descriptions))


# Finding the most similar product
products = [
    {"short_description": desc}
    for desc in list_of_descriptions
]

search_text = "soap"
all_embeddings = create_embeddings([search_text] + list_of_descriptions)
search_embedding = all_embeddings[0]
product_embeddings = all_embeddings[1:]

for product, emb in zip(products, product_embeddings):
    product["embedding"] = emb

# Compute the cosine distance for each product description

distances = []
for product in products:
    dist = distance.cosine(search_embedding, product["embedding"])
    distances.append(dist)

# Find and print the most similar product short_description
min_dist_ind = np.argmin(distances)
print(products[min_dist_ind]['short_description'])

