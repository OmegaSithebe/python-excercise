from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer (manual text2text-generation process)
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
"""

# Tokenize input
inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)

# Generate summary
summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=20, do_sample=False)

# Decode summary
summary_text = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]
print(summary_text)


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
# Coding Example: Extractive-style Summary
# from transformers import pipeline
# summarizer=pipeline(
# task="summarization",
# model="facebook/bart-large-cnn"
# )
# text="""
# Data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms, and systems to extract knowledge and insights from data.
# It combines statistics, computer science, and domain expertise.
# """
# result=summarizer(text)
# print(result)
# [{'summary_text': 'Data science uses scientific methods and algorithms to extract insights by combining statistics, computer science, and domain expertise.'}]
# 📌 The model selects and restructures **important parts** of the original content
# 📌 Factual and concise
## 7️⃣ Abstractive Summarization in Action
# The **main difference** lies in the **model choice**.
# Here, we use **DistilBART**, designed for **abstractive summarization**.
### ✅ Coding Example: Abstractive Summary
# from transformers import pipeline
# summarizer=pipeline(
# task="summarization",
# model="sshleifer/distilbart-cnn-12-6"
# )
# result=summarizer(text)
# print(result)
# [{'summary_text': 'Data science combines statistics and computing to extract valuable insights from data.'}]
# 📌 More natural
# 📌 Rephrased
# 📌 Easier to read
# ⚠️ But may occasionally **add or omit details**
## 8️⃣ Parameters for Summarization
# We can control the **length and quality** of summaries using parameters.
### 🔑 Important Parameters
# - `min_new_tokens` → minimum summary length
# - `max_new_tokens` → maximum summary length
# 🔹 Tokens are **units of text** (words or subwords) used by models.
### ✅ Example with Parameters
# summary=summarizer(
# text,
# min_new_tokens=30,
# max_new_tokens=60
# )
# print(summary)
# These parameters ensure:
# - Summary is not too short
# - Summary is not too verbose
# - Output remains meaningful
## 🔟 Key Challenges in Summarization (Discussion)
# - Long documents may exceed model limits
# - Abstractive models may hallucinate
# - Domain-specific language needs fine-tuning
# 📌 Solution strategies:
# - Chunk long texts
# - Choose extractive models for safety
# - Fine-tune on domain data
## ✅ Key Takeaways for Students
# - Summarization reduces text while keeping meaning
# - Extractive = safe and factual
# - Abstractive = natural and readable
# - Hugging Face pipelines make summarization simple
# - Length control is essential for good summaries


## **Exercise**

# **Summarizing long text**
# Summarization reduces large text into manageable content, helping readers quickly grasp key points from lengthy articles or documents.
# There are two main types: **extractive**, which selects key sentences from the original text, and **abstractive**, which generates new sentences summarizing main ideas.
# In this exercise, you’ll create an **abstractive summarization pipeline** using Hugging Face's `pipeline()` function and the `cnicu/t5-small-booksum` model. You’ll summarize text from a Wikipedia page on Greece, comparing the abstractive model's rephrased output to the original.
# The `pipeline` function from the `transformers` library and the `original_text` have already been loaded for you.
# **Instructions**
# • Create the summarization `pipeline` using the task "summarization" and save as `summarizer`.
# • Use the new pipeline to create a summary of the text and save as `summary_text`.
# • Compare the length of the original and summary text.
# - • Create the summarization `pipeline` using the task "summarization" and save as `summarizer`.
# - • Use the new pipeline to create a summary of the text and save as `summary_text`.
# - • Compare the length of the original and summary text.

original_text = """
Greece, officially the Hellenic Republic, is a country located in Southeast Europe. It shares borders with Albania, North Macedonia, Bulgaria, and Turkey. Greece has a rich history and is often considered the cradle of Western civilization, being the birthplace of democracy, philosophy, and the Olympic Games. The country is known for its stunning landscapes, including beautiful islands, ancient ruins, and vibrant culture.
"""

# Create the summarization pipeline
summarizer = pipeline("summarization" , model="cnicu/t5-small-booksum")

# Summarize the text
summary_text =summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")


# **Adjusting the summary length**
# The `pipeline()` function, has two important parameters: `min_new_tokens` and `max_new_tokens`. These are useful for adjusting the length of the resulting summary text to be short, longer, or within a certain number of words. You might want to do this if there are space constraints (i.e., small storage), to enhance readability, or improve the quality of the summary.
# You'll experiment with a short and long summarizer by setting these two parameters to a small range, then a wider range.
# `pipeline` from the `transformers` library and the `original_text` have already been loaded for you.
# **Instructions 1/2**
#     - Create a summarization pipeline to summarize `original_text` to between 1 and 10 tokens.
#     - Repeat these steps for a summarization pipeline that has a minimum length of `50` and maximum of `150`.
    
# Generate a summary of original_text between 1 and 10 tokens
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=1, max_new_tokens=10)

short_summary_text = short_summarizer(original_text)

print(short_summary_text[0]["summary_text"])







# 2.3 Auto Models and Auto Tokenizers (Hugging Face)
## 1️⃣ Introduction

# Welcome back! 👋

# In previous classes, we used **pipelines** to quickly run tasks like **text classification** and **summarization**.

# Today, we’ll go **one level deeper** and learn how to gain **full control** over models and tokenization using:

# 👉 **AutoModels and AutoTokenizers**

# ---

## 2️⃣ Pipelines: Fast and Simple

# Pipelines are a **high-level abstraction** provided by **Hugging Face Transformers**.

### ✅ What pipelines do for us

# - Load the model
# - Load the tokenizer
# - Preprocess input
# - Run inference
# - Format output

# All in **one line of code**.
### 📌 Example

# ```python
# from transformers import pipeline

# classifier=pipeline("text-classification")
# classifier("I love learning AI!")
# ```

# ✔ Perfect for:

# - Demos
# - Beginners
# - Rapid experimentation

# ❌ But… pipelines hide many details.

# ---

## 3️⃣ Auto Classes: Flexible and Powerful

# When we need **more control**, pipelines become limiting.

# That’s where **Auto classes** come in.

### 🔹 What are Auto Classes?

# Auto classes automatically:

# - Load the **correct model architecture**
# - Load the **correct tokenizer**
# - Match them properly

# But **you control each step**.

### 📌 Comparison

# | Pipelines | Auto Classes |
# | --- | --- |
# | Simple | Flexible |
# | Less control | Full control |
# | Best for demos | Best for production & research |

## 4️⃣ AutoModels

# AutoModels simplify model loading **without hardcoding architectures**.

### 🎯 Example: Text Classification

# For text classification (also called **sequence classification**), we use:

# 👉 `AutoModelForSequenceClassification`

### ✅ Loading a model

# ```python
# from transformers import AutoModelForSequenceClassification

# model=AutoModelForSequenceClassification.from_pretrained(
# "distilbert-base-uncased-finetuned-sst-2-english"
# )
# ```

# 📌 What happens internally:

# - Correct model class is selected
# - Pretrained weights are downloaded
# - Model is ready for inference or fine-tuning

# ---

## 5️⃣ AutoTokenizers

# Models **do not understand raw text**.

# They only understand **numbers (tokens)**.

# That’s why we need **tokenizers**.

### ⚠️ Important Rule

# 👉 **Always use the tokenizer paired with the model**

# Pipelines do this automatically.

# With Auto classes, **you do it manually**.

### ✅ Loading the tokenizer

# ```python
# from transformers import AutoTokenizer

# tokenizer=AutoTokenizer.from_pretrained(
# "distilbert-base-uncased-finetuned-sst-2-english"
# )
# ```

# 📌 This ensures:

# - Same preprocessing
# - Same vocabulary
# - Same token rules used during training

# ---

## 6️⃣ Tokenizing Text with AutoTokenizer

### 🔍 What does a tokenizer do?

# 1. Cleans text (lowercase, accents, punctuation)
# 2. Splits text into **tokens**
# 3. Maps tokens to **IDs**

### ✅ Example

# ```
# tokens=tokenizer.tokenize("I love learning AI!")
# print(tokens)
# ```

### 🧾 Output (example)

# ```
# ['i', 'love', 'learning', 'ai', '!']
# ```

# 📌 These tokens are what the model actually processes.

# ---

## 7️⃣ Different Models, Different Tokenizers

# Not all models tokenize text the same way.

### 📌 Example

# - BERT → word-piece tokens
# - GPT → byte-pair encoding
# - SentencePiece → subword units

# The **same sentence** can produce **different tokens** depending on the model.

# 👉 This is why **mixing tokenizers and models is dangerous**.

# ---
## 8️⃣ Building a Custom Pipeline with Auto Classes
# Now let’s build a **pipeline manually** using Auto classes.
### ✅ Custom Sentiment Analysis Pipeline
# ```python
# fromtransformersimport (
# AutoTokenizer,
# AutoModelForSequenceClassification,
# pipeline
# )
# model_name="distilbert-base-uncased-finetuned-sst-2-english"
# tokenizer=AutoTokenizer.from_pretrained(model_name)
# model=AutoModelForSequenceClassification.from_pretrained(model_name)
# custom_pipeline=pipeline(
# task="text-classification",
# model=model,
# tokenizer=tokenizer
# )
# custom_pipeline("This course is absolutely amazing!")
# 📌 Same result as a normal pipeline
# 📌 But now **you can customize every step**

## 9️⃣ Use Cases for AutoModels and AutoTokenizers
# We prefer Auto classes when tasks require **advanced customization**.
### 🔹 1. Advanced Text Preprocessing
# - Custom cleaning rules
# - Domain-specific normalization
### 🔹 2. Custom Thresholding
# - Adjust confidence cutoffs
# - Prefer certain labels (e.g., route more queries to **Support**)
### 🔹 3. Complex NLP Pipelines
# - Multi-step workflows
# - Combine classification, summarization, and embeddings
# - Integrate with databases or APIs
# 📌 Auto classes give **precision and control**, essential for real-world systems.
## ✅ Key Takeaways for Students
# - Pipelines = fast & beginner-friendly
# - Auto classes = flexible & powerful
# - AutoModels load the **right architecture automatically**
# - AutoTokenizers ensure **correct text preprocessing**
# - Never mix models and tokenizers randomly
## 📌 When to Use AutoModels and AutoTokenizers
# You should use **AutoModels** and **AutoTokenizers** when you need **more control, customization, or flexibility** than what simple pipelines provide.
## 1️⃣ When Pipelines Are *Not Enough*
# Pipelines are great for:
# - Quick experiments
# - Demos
# - Learning basics
# But they **hide internal steps**, such as:
# - How text is tokenized
# - How inputs are passed to the model
# - How outputs are processed
# 👉 When you want to **control these steps**, use AutoModels and AutoTokenizers.
## 2️⃣ Advanced Text Preprocessing
# Use AutoTokenizers when you need:
# - Custom text cleaning
# - Special handling of domain-specific text
#     (e.g., legal, medical, code, chat logs)
# - Explicit control over truncation, padding, or max length
# 📌 Example use case:
# - Cleaning customer support messages before classification
# - Handling very long documents by chunking text manually
## 3️⃣ Model–Tokenizer Compatibility (Best Practice)
# AutoTokenizers ensure the **exact tokenizer used during model training** is loaded.
# Why this matters:
# - Different models tokenize text differently
# - Wrong tokenizer = wrong inputs = bad predictions
# 👉 Always use:
# ```
# AutoTokenizer.from_pretrained(model_name)
# AutoModel.from_pretrained(model_name)
## 4️⃣ Custom Thresholding & Decision Logic
# In real applications, we don’t always accept the model’s top prediction blindly.
# Use AutoModels when you want:
# - Custom confidence thresholds
# - Business logic on predictions
    
#     (e.g., classify as *Support* only if confidence > 0.8)
# 📌 Example:
# - Route messages to human agents if confidence is low
# - Prioritize certain labels in customer service systems
## 5️⃣ Fine-Tuning and Training Models
# Pipelines are **mostly for inference**.
# If you want to:
# - Fine-tune a pretrained model
# - Train on your own dataset
# - Adjust loss functions or training steps
# 👉 You **must** use AutoModels and AutoTokenizers.
# This is how almost all **production and research workflows** are built.
## 6️⃣ Building Complex NLP Workflows
# Use Auto classes when your system involves:
# - Multiple NLP tasks (classification + summarization)
# - Custom batching
# - Integration with databases or APIs
# - Deployment in production environments
# 📌 Example:
# - A chatbot that classifies intent, summarizes history, and generates replies
## 7️⃣ Performance and Optimization Needs
# AutoModels give access to:
# - Model outputs (logits, hidden states)
# - GPU / CPU control
# - Batch inference optimizations
# This is **not possible** with high-level pipelines alone.
# ---
## 🧠 Simple Rule
# > **Use pipelines to learn and experiment.
# Use AutoModels and AutoTokenizers to build real systems.**
# > 
## ✅ One-Line Summary (Great for Exams / Interviews)
# > AutoModels and AutoTokenizers are used when we need full control over tokenization, model behavior, thresholds, fine-tuning, and complex NLP workflows beyond simple pipelines.
# > 

## Exercise

# **Tokenizing text with AutoTokenizer**
# AutoTokenizers simplify text preparation by automatically handling cleaning, normalization, and tokenization. They ensure the text is processed just as the model expects.
# In this exercise, explore how AutoTokenizer transforms text into tokens ready for machine learning tasks.
# **Instructions**
# - **Import** the required class from `transformers`, **load** the tokenizer using the correct method, and **split** input text into tokens.
# ```python
# # Import necessary library for tokenization
# from transformers import AutoTokenizer
# # Load the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
# # Split input text into tokens
# tokens = tokenizer.tokenize("AI: Making robots smarter and humans lazier!")
# # Display the tokenized output
# print(f"Tokenized output: {tokens}")

## Exercise
# **Using AutoClasses**
# You’ve seen how tokenizers work and explored their role in preparing text for models. Now, let’s take it a step further by combining AutoModels and AutoTokenizers with the `pipeline()` function. It's a nice balance of control and convenience.
# Continue with the sentiment analysis task and combine AutoClasses with the pipeline module.
# `AutoModelForSequenceClassification`, `AutoTokenizer` and `pipeline` from the `transformers` library have already been imported for you.
# **Instructions**
# - Download the model and tokenizer and save as `my_model` and `my_tokenizer`, respectively.
# - Create the pipeline and save as `my_pipeline`.
# - Predict the output using `my_pipeline` and save as `output`.
# ```python
# # Download the model and tokenizer
# my_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
# my_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
# my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# # Predict the sentiment
# output =my_pipeline("This course is pretty good, I guess.")
# print(f"Sentiment using AutoClasses: {output[0]['label']}")
# ```







