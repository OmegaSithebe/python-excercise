from transformers import pipeline

# Create text classification pipeline
classifier = pipeline("sentiment-analysis")

# Test sentences
texts = [
    "I love learning machine learning!",
    "This course is terrible and confusing."
]

# Run predictions
results = classifier(texts)

for text, result in zip(texts, results):
    print("\nText:", text)
    print("Prediction:", result)
    
    
    
    
    
    
    
    
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

sentences = [
    "I absolutely love this product!",
    "This is the worst service ever.",
    "The movie was fantastic!",
    "I am disappointed with the quality.",
    "The tutorial was very helpful."
]

results = classifier(sentences)

for sentence, result in zip(sentences, results):
    print("\nSentence:", sentence)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 3))
    
    
    
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

while True:
    text = input("\nEnter a sentence (or type 'exit'): ")

    if text.lower() == "exit":
        break

    result = classifier(text)[0]

    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 3))