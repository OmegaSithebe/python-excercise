from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
"""

result = summarizer(text, max_length=50, min_length=20)

print(result[0]['summary_text'])

# 2.2 Text Summarization with Hugging Face
## 1️⃣ Introduction to Text SummarizationWelcome back!After exploring **text classification**, we now move to another **core NLP task**:👉 **Text Summarization**Summarization helps machines **condense large amounts of text** into shorter, meaningful versions—saving time while preserving important information.---

## 2️⃣ What Is Text Summarization?**Text summarization** is the process of reducing a long piece of text into a **shorter summary**, while retaining the **key ideas and essential information**.
### 📌 ExampleOriginal text:> Data science combines statistics, programming, and domain expertise to extract insights from data...> Summary:> Data science uses statistics and programming to extract insights from data.> ✔ Shorter✔ Clear✔ Key meaning preserved---

## 3️⃣ Extractive vs Abstractive SummarizationThere are **two main types** of summarization:---

### 🔹 Extractive Summarization- Selects **important sentences directly** from the original text- Does **not generate new words**- Faster and more resource-efficient- Very factual and safe📉 Limitations:- May feel less natural- Summary can feel fragmented---

### 🔹 Abstractive Summarization- **Generates new sentences**- Rephrases content for clarity- Produces more **human-like summaries**📉 Limitations:- Requires more computation- May introduce **hallucinations** (fabricated information)---

## 4️⃣ Use Cases of Extractive SummarizationExtractive summarization is best when **accuracy is critical**.
### 📌 Real-world examples- **Legal Document Analysis**    - Highlighting key clauses    - No risk of changing meaning- **Financial Research**    - Extracting important findings    - Ensures no new facts are introduced✔ Faithful to the source✔ High precision---

## 5️⃣ Use Cases of Abstractive SummarizationAbstractive summarization focuses on **readability and clarity**.

### 📌 Real-world examples- **News Article Summaries**    - Short, engaging overviews- **Content Recommendations**    - Generating descriptions users want to read✔ More natural✔ More engaging---

## 6️⃣ Extractive Summarization in Action We use **pipelines** from the **Hugging Face Transformers** library.
### 🧠 Reminder: PipelineA pipeline handles:- Tokenization- Model inference- Output formatting

#Clear term definition explained: 
#what is a pipeline in simple terms - In simple terms, a pipeline is a series of connected steps or stages that move something from a starting point to a finish line. Just as a physical pipe moves water from a reservoir to your tap, a "pipeline" in other fields moves items, data, or projects through a sequence of actions until they are complete
#Tokens are units of text (words or subwords) used by models.
#"NLP" typically refers to one of two very different fields: Natural Language Processing in technology or Neuro-Linguistic Programming in personal development. 
# 1. Natural Language Processing (Technology)In the context of artificial intelligence (AI), NLP is a subfield of computer science and linguistics that focuses on enabling computers to understand, interpret, and generate human language. How it works: It uses machine learning and deep learning to bridge the gap between human communication and computer data. It breaks language into smaller parts (tokenisation), identifies grammatical roles (part-of-speech tagging), and extracts meaning (sentiment analysis).

