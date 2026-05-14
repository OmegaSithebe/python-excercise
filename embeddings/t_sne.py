"""Embeddings t-SNE visualizer (Jupyter-friendly).

Usage (in Jupyter/notebook cell):
    - Run this file as a module OR copy-paste the main() contents.

This script:
- Creates embeddings for the same sample dataset used in world_embedding.py
- Reduces them to 2D with t-SNE
- Plots in an interactive-friendly way using matplotlib

Expected environment:
- .env with OPENAI_API_KEY=...
"""

from __future__ import annotations

import os
from dataclasses import dataclass

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI


def get_client() -> OpenAI:
    """Create an OpenAI client using OPENAI_API_KEY from .env."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Create a .env file in the project root with: "
            "OPENAI_API_KEY=..."
        )
    return OpenAI(api_key=api_key)


@dataclass
class Article:
    headline: str
    topic: str
    embedding: list[float] | None = None


def build_articles() -> list[Article]:
    return [
        Article("Government announces new tax reform", "politics"),
        Article("Local team wins national championship", "sports"),
        Article("New AI model beats humans at chess", "technology"),
        Article("Stock market hits record high", "business"),
        Article("President meets foreign leaders for climate summit", "politics"),
        Article("New law passed to improve public healthcare", "politics"),
        Article("Star player scores hat-trick in final match", "sports"),
        Article("Olympic committee announces new events", "sports"),
        Article("Breakthrough in quantum computing announced", "technology"),
        Article("Tech company releases next-gen smartphone", "technology"),
        Article("Global oil prices see significant drop", "business"),
        Article("Startup raises millions in funding round", "business"),
        Article("Scientists discover new species in rainforest", "science"),
        Article("Space agency plans mission to Mars", "science"),
        Article("New movie breaks box office records", "entertainment"),
        Article("Famous actor wins international award", "entertainment"),
    ]


def create_embeddings(client: OpenAI, texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    response = client.embeddings.create(model=model, input=texts)
    return [item.embedding for item in response.data]


def reduce_embeddings_tsne(embeddings_array: np.ndarray, random_state: int = 42) -> np.ndarray:
    """Reduce embeddings to 2D using t-SNE."""
    try:
        from sklearn.manifold import TSNE
    except ImportError as e:
        raise RuntimeError(
            "scikit-learn is not installed. Install it to use t-SNE visualization: pip install scikit-learn"
        ) from e

    n_samples = embeddings_array.shape[0]
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


def plot_tsne(embeddings_2d: np.ndarray, articles: list[Article]) -> None:
    # Jupyter-friendly plotting: do not create multiple plt.show() blocks.
    import matplotlib.pyplot as plt

    x = embeddings_2d[:, 0]
    y = embeddings_2d[:, 1]

    plt.figure(figsize=(10, 7))
    plt.scatter(x, y)

    for i, article in enumerate(articles):
        plt.annotate(article.topic, (x[i], y[i]))

    plt.title("t-SNE of OpenAI text embeddings")
    plt.xlabel("t-SNE component 1")
    plt.ylabel("t-SNE component 2")

    # In Jupyter, this displays automatically, but show() helps when running in scripts.
    plt.show()


def main() -> None:
    client = get_client()
    articles = build_articles()

    headlines = [a.headline for a in articles]
    embeddings = create_embeddings(client, headlines)

    for i, a in enumerate(articles):
        a.embedding = embeddings[i]

    embeddings_array = np.array([a.embedding for a in articles], dtype=np.float32)
    embeddings_2d = reduce_embeddings_tsne(embeddings_array)

    plot_tsne(embeddings_2d, articles)


if __name__ == "__main__":
    main()

