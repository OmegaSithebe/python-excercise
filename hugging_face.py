# 1. 1Working with Hugging Face## What is Hugging Face?Welcome to this course on **Hugging Face** 🎉Hugging Face is a platform that brings together the **global AI community**. It allows people to:- Access powerful AI models- Share and use datasets- Build and test AI applications👉 **Important:**You do **NOT** need to be a Machine Learning Engineer to use Hugging Face. Beginners, developers, and researchers can all use it.

## The Home of the AI CommunityHugging Face is often called **“the home of the AI community”** because it hosts:- ✅ Open-source **models**- ✅ Public **datasets**- ✅ Ready-to-use **applications (apps)**All of these are shared openly so others can learn, build, and improve on them.

## The Hugging Face HubThe **Hugging Face Hub** is a **central place** where everything lives.Using the Hub, you can:- 🔍 Find the best models for your project- 📊 Download datasets for training or fine-tuning- 🧪 Test models directly in the browser- 🚀 Build and share applications💡 **Key idea:**You can do many things **without writing code**, directly from your browser.

## Hugging Face Libraries (Python Support)If you want to work with Hugging Face using **Python**, Hugging Face provides powerful libraries with excellent documentation.These libraries help you:- Explore models and datasets from the Hub- Run models for inference (prediction)- Train or fine-tune models- Deploy AI applications📌 In this course, we will use some of these Python libraries step by step.

## Community & Open-Source ContributionsHugging Face works because of its **strong open-source community**.People openly share:- Models they trained- Datasets they created- Applications they builtMany large organizations also contribute, including:- **Google**- **Meta**- **DeepSeek**👉 **Student takeaway:**If you fine-tune a model, create a dataset, or build an app, you can share it on Hugging Face so others can benefit.

## What You’ll Learn in This CourseIn this **2-hour course**, you will learn how to:- Navigate the Hugging Face Hub- Explore and use models and datasets- Work both:    - Directly in the Hub (browser)    - Using Hugging Face’s Python libraries

## AI Tasks Covered in This CourseWe will use Hugging Face tools to perform common **Natural Language Processing (NLP)** tasks such as:- 📝 Text summarization- 🏷️ Text classification- ❓ Document question answeringThese tasks are widely used in real-world applications like chatbots and document analysis.

## Learning Path Beyond This CourseThis course is the **first part of a larger learning journey**.Upcoming topics include:- Hugging Face for **Large Language Models (LLMs)**- Prompting and fine-tuning- Other modalities:    - 🖼️ Images    - 🔊 Audio    - 🎥 Video- Efficient and optimized model training📌 **Encouragement:** Stay tuned and keep practicing!

## Example: Finding the Right Model### ScenarioImagine your company wants to build an **internal chatbot**.Steps you would follow:1. Go to the **Models** section of the Hub2. Select the **Text Generation** task filter3. Browse:    - Latest models    - Most downloaded models    - Trending modelsThis helps you quickly narrow down the best options.

## Understanding a Model CardEach model on the Hub comes with a **model card**.A model card contains:- Model name and author (user or company)- Supported tasks- Supported modalities (text, image, etc.)- Languages supported- License information- Intended use and limitations- Training details and datasets used- Evaluation results (for comparison)- Sometimes, linked research papers👉 **Why this matters:**Model cards help you decide **which model is safe, suitable, and legal** for your project.

# **Why build with Hugging Face?**Hugging Face is a powerful platform that provides many benefits for building AI solutions, simplifying workflows and making advanced models accessible.

# **Exploring models on the Hub!**
# You're a research scientist working on a new type of X-ray imaging device. This device offers increased image resolution, which you hope to use to detect illnesses like pneumonia earlier. Rather than *training* a machine learning model from scratch, you want to *fine-tune* an existing model trained for a similar purpose to your new images, and the **model card** for such a model is shown.The model can also be used for image generation



# 1.2 Running Hugging Face Models
## **Learning Objectives**By the end of this class, students will be able to:- Understand what **model inference** is- Explain **local inference vs inference providers**- Run a model locally using the **Transformers pipeline**- Adjust generation parameters- Perform inference using **Hugging Face Inference Providers (API-based)**

## **Recap & Class Context**Great work exploring the Hugging Face Hub in the previous class!Now that we know **where models live**, it’s time to **run them** 🚀👉 Running a model = **Inference**- Giving input to a trained model- Getting predictions or generated outputExamples:- Text → generated text- Image → caption- Audio → transcription

## **What is Inference? (Core Concept)****Inference** means:> Using a trained AI model to make predictions on new data> When running Hugging Face models, we have **two main options**:1. **Local inference**2. **Inference using providers (via API)**

## **Local Inference (Run Models on Your Own Machine)**### **What is Local Inference?**Running a model:- On your laptop- On your desktop- Or inside a cloud dev environment (like Colab)
### **Advantages**✅ Free✅ No API key required✅ Full control over the model### **Limitations**⚠️ Slow on large models⚠️ High RAM & CPU usage⚠️ Large models need **GPUs**, which most laptops don’t have📌 **Best for**:- Small to medium models- Learning & experimentation

## **Inference Providers (API-Based Inference)**### **What are Inference Providers?**Inference providers are **partner companies** that:- Host powerful machines (GPUs/TPUs)- Run models for us remotelyWe:1. Send input + model name2. Provider runs the model3. We receive the outputAll through **Hugging Face APIs**
### **Why Use Them?**✅ Much faster✅ No hardware stress✅ Can run large LLMs, image & video models✅ Free credits to get started📌 **Best for**:- Large language models- Image / video generation- Production-ready apps

## **Introduction to the Transformers Library**To run models locally, we use:**Transformers**### **Why Transformers?**- Easy access to thousands of pre-trained models- Same API for NLP, vision, audio- Works for **inference & training**

## **The `pipeline()` – Fastest Way to Run a Model**

### **What is a Pipeline?**A **pipeline** is a high-level wrapper that:- Loads the model- Handles tokenization- Runs inference- Returns readable output
# Basic Example: Text Generation
# from transformers import pipeline

# generator=pipeline(
# task="text-generation",
# model="openai-community/gpt2"
# )

# result=generator("What if AI")
# print(result[0]["generated_text"])

### **What’s Happening Here?**- `task="text-generation"` → tells what we want- `model="openai-community/gpt2"` → model name from the Hub- Input text → `"What if AI"`- Output → dictionary with `generated_text`📌 Model details come from the **model card** on the Hub.

## **Adjusting Pipeline Parameters**We can **control the output** using parameters.
### **Example: Limit Tokens & Generate Multiple Outputs**
# results=generator(
# "What if AI",
# max_new_tokens=10,
# num_return_sequences=2
# )

# for res in results:
#     print(res["generated_text"])

### **Common Parameters**- `max_new_tokens` → limits output length- `num_return_sequences` → multiple responses- `temperature` → creativity- `top_k`, `top_p` → randomness control📌 Output becomes a **list of dictionaries**

## **Using Hugging Face Inference Providers**Now let’s run models **without using our own hardware**.
### **Steps**1. Create an inference client2. Choose an inference provider3. Add Hugging Face API key4. Send input as messagesExample provider:**Together.ai**

## **Conversational Text Generation (API Style)**Most modern LLMs use a **chat-based format**.### **Message Structure**
# messages= [
#     {"role":"user","content":"Explain AI in simple terms"}
# ]
# - `role: "user"` → input from us- `content` → the promptThe provider:- Runs the model remotely- Sends back the generated response✅ Fast✅ No GPU needed✅ No laptop overheating 😄

## **Key Takeaways (Wrap-Up)**### **Local Inference**- Free & simple- Limited by hardware### **Inference Providers**- Fast & scalable- Ideal for large models- Uses API + credits### **Transformers Pipeline**- Easiest way to run models locally- Great for learning and prototyping

# Building a text generation pipeline

#import thr pipeline
from transformers import pipeline

# Create the pipeline
gpt2_pipeline = pipeline(
    task="text-generation", 
    model="openai-community/gpt2"
    )

#Generate three text outputs with a maximum length of 10 tokens
results = gpt2_pipeline(
    'What if AI', 
    max_new_tokens=10, 
    num_return_sequences=2
    )

results = gpt2_pipeline(
    'How to build a successful startup',
    max_new_tokens=15,
    num_return_sequences=3
)

for result in results:
    print(result['generated_text'])
    
    
    
# Exercise
# Inference providers
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider='together',
    api_key=os.environ['HF_TOKEN'],
)

completion = client.chat.completions.create(
    model='deepseek-ai/Deepseek-V3',
    messages=[
        {'role': 'user', 'content': 'what is the capital of France?'}
    ]
)

print(completion.choices[0].message.content)



# 1.3 Hugging Face Datasets
## Introduction to Hugging Face DatasetsWelcome back!So far, we’ve explored **models** on the Hugging Face Hub and learned how to **run inference** using them.Now, we move to an equally important component of machine learning workflows:👉 **Datasets**Without good datasets, even the best models fail to perform well.---

## 2️⃣ What Are Hugging Face Datasets?The **Hugging Face Hub** provides a large collection of **community-curated datasets** covering:- Natural Language Processing (NLP)- Computer Vision- Audio & Speech- Multimodal tasksThese datasets are hosted under the **Datasets** section of the Hub:👉 https://huggingface.co/datasetsJust like models, datasets come with:- Metadata- Documentation- Licenses- Preview tools---

## 3️⃣ Exploring Datasets on the HubThe dataset search experience is **very similar to models**:You can filter datasets by:- **Modality** (Text, Image, Audio, etc.)- **Task** (Text Generation, Translation, Classification, etc.)- **Language**- **Size**- **License**This helps us quickly find the **most suitable dataset** for our task.---

## 4️⃣ Example: Italian Text Generation Dataset### 🎯 GoalWe want to **fine-tune a text generation model** to improve **Italian language output**.### 🔍 Step-by-step filtering1. Go to **Datasets**2. Select **Text** modality3. Choose **Text Generation** task4. Add keyword search: *Italian*After filtering, we find a dataset that looks promising for Italian text generation.✅ This process mirrors **real-world dataset discovery**.---

## 5️⃣ Dataset Card & Dataset ViewerEach dataset has a **Dataset Card**, similar to a model card.

### 📄 Dataset Card includes:- How the dataset was created- Source of data- License (very important!)- Number of rows- Available splits (train / test / validation)
### 👀 Dataset Viewer- Lets us preview rows directly in the browser- Helps understand structure and content quickly

### 🧪 Data StudioFor deeper exploration, Hugging Face provides **Data Studio**, where we can:- Inspect columns- Run queries- Explore large datasets interactively---

## 6️⃣ Querying Datasets with SQLInside **Data Studio**, datasets can be queried using **SQL**.### Example use caseWe want to find Italian sentences containing the word **"bella"** (means *beautiful*).```SELECT*FROM datasetWHERE textLIKE'%bella%'```✔ This helps us:- Filter relevant samples- Clean noisy data- Prepare high-quality training dataOnce satisfied, we move to **Python** for real processing.---

## 7️⃣ Installing the Datasets LibraryHugging Face provides a dedicated Python package called:📦 **datasets**### Installation```pip install datasets```### Why use it?The `datasets` library allows us to:- Download datasets- Load large datasets efficiently- Process data with minimal code- Share datasets easilyOfficial docs:👉 https://huggingface.co/docs/datasets/loading---

## 8️⃣ Downloading a Dataset in PythonWe use the `load_dataset()` function.### Basic example```fromdatasetsimportload_datasetdataset=load_dataset("dataset_name")```
### Loading a specific split```dataset=load_dataset("dataset_name",split="train")```📌 Common splits:- `train` → training the model- `test` → evaluation- `validation` → tuning & monitoringAlways check the **dataset card** to know which splits are available.---

## 9️⃣ Apache Arrow Dataset FormatMost Hugging Face datasets use **Apache Arrow**.
### Why Apache Arrow?- Column-based storage- Faster querying- Lower memory usage- Efficient for large datasets⚠️ Arrow datasets behave differently than Pandas DataFrames.---

## 🔟 Data Manipulation: Filtering RowsTo filter rows, we use the `.filter()` method.

### Example: Find rows containing "bella"```filtered_dataset=dataset.filter(lambdarow:"bella"inrow["text"])```✔ The lambda function runs on each row✔ Returns a new filtered dataset✔ Very efficient for large datasets
## 1️⃣1️⃣ Data Manipulation: Selecting RowsTo select rows by index, we use `.select()`.

### Example: Select first two rows```small_dataset=dataset.select(range(2))```### Access a specific entry```small_dataset[0]["text"]```✔ Useful for:- Debugging- Inspecting samples- Teaching & demos---

## ✅ Key Takeaways for Students- Hugging Face Datasets are **easy to discover and use**- Dataset cards are **critical for understanding data**- SQL + Python = powerful dataset exploration- Apache Arrow enables **fast and scalable data processing**- `.filter()` and `.select()` are core dataset operations


from datasets import load_dataset

dataset = load_dataset("imdb")

dataset = dataset.map(lambda x: {"length": len(x["text"])})

import datasets
print(datasets.__version__)

dataset = load_dataset("imdb")
print(dataset)


# 2. 1 Building Pipelines with Hugging Face
## Introduction to Text Classification
# Welcome back!
# So far, we’ve explored **models**, **datasets**, and **inference**.
# Now, we’ll focus on a **core machine learning task** used across real-world applications:
# 👉 **Text Classification**
# Text classification helps machines **understand and organize text** by assigning labels or categories.

## 2️⃣ What Is Text Classification?Text classification is the task of **assigning predefined categories (labels)** to a piece of text.

### 🔍 Common Use Cases
# - Sentiment analysis (positive / negative)
# - Spam detection
# - Topic classification
# - Grammar checking
# - Question answering systems

### 📌 Example: Sentiment Analysis
# | Sentence | Label |
# | --- | --- |
# | *I love pine apple on pizza* | **Positive** |
# | *I dislike pine apple on pizza* | **Negative** |
# This technique helps extract **opinions, emotions, and attitudes**, especially useful in:
# - Product reviews
# - Social media monitoring
# - Customer feedback analysis


## 3️⃣ Sentiment Analysis: Coding ExampleHugging Face makes text classification easy using **pipelines** from the **Hugging Face Transformers** library.

### 🧠 What is a pipeline?
# A pipeline bundles:
# - Tokenization
# - Model inference
# - Output formatting 
#     into **one simple interface**.
    

### ✅ Example: Sentiment Analysispythonfrom transformers import pipeline
# classifier=pipeline(task="text-classification",model="distilbert-base-uncased-finetuned-sst-2-english")
# result=classifier("I hate waiting in long queues")print(result)### 🧾 Output (example)[{'label': 'NEGATIVE', 'score': 0.99}]
# ✔ The model predicts **Negative sentiment**✔ The confidence score shows **how sure the model is**


## 4️⃣ Text Classification: Grammatical CorrectnessAnother important type of text classification is **grammatical correctness**.

### 🎯 GoalDetermine whether a sentence is:- **Acceptable** (grammatically correct)- **Unacceptable** (grammatically incorrect)

### 📌 Examples
# | Sentence | Label |
# | *This course is great!* | Acceptable |
# | *Course is gravy* | Unacceptable |

# This task is commonly used in:
# - Grammar checkers
# - Writing assistants
# - Language learning tools


## 5️⃣ Grammatical Correctness: Coding Example
# python
# from transformers import pipeline
# grammar_checker=pipeline(
# task="text-classification",
# model="textattack/bert-base-uncased-CoLA"
# )result=grammar_checker("He eat pizza every day")
# print(result)


### 🧾 Output (example)[{'label': 'LABEL_0', 'score': 0.99}]📌 Interpretation:- `LABEL_0` → grammatically incorrect- High score → strong confidence

## 6️⃣ Text Classification: QNLI### ❓ What is QNLI?QNLI stands for **Question Natural Language Inference**.It checks whether a **given sentence (premise)** answers a **question**.
### 📌 Examples| Question | Premise | Label || --- | --- | --- || What state is Hollywood in? | Hollywood is in California | Entailment (True) || What state is Hollywood in? | Hollywood is known for movies | Not Entailment (False) |This task is crucial for:- Question-answering systems- Fact checking- Information verification

## 7️⃣ QNLI: Coding ExampleFor QNLI, we pass **question and premise together**.pythonfrom transformers import pipelineqnli_classifier=pipeline(task="text-classification",model="textattack/bert-base-uncased-QNLI")result=qnli_classifier("Where is Seattle located?, Seattle is in Washington state.")print(result)

### 🧾 Output (example)[{'label': 'LABEL_0', 'score': 0.98}]📌 Interpretation:- `LABEL_0` → Entailment (True)- The premise answers the question correctly


## 8️⃣ Text Classification: Dynamic Category AssignmentSometimes, categories are **not fixed during training**.This is where **dynamic category assignment** comes in.
### 📌 ExampleText:> *I want to know more about your pricing plans*>Possible categories:- Sales- Marketing- SupportThe model assigns a **confidence score to each category**, choosing the best match.This approach is widely used in:- Customer support systems- Email routing- Content moderation- Recommendation systems

## 9️⃣ Dynamic Category Assignment: Zero-Shot ClassificationThis is done using **zero-shot classification**.
### 🧠 What is Zero-Shot?The model:- Has **not been trained** on your specific labels- Still understands and assigns them using language knowledge

### ✅ Coding Examplepythonfrom transformers import pipelinezero_shot=pipeline(task="zero-shot-classification",model="facebook/bart-large-mnli")result=zero_shot("Hey, we would like to feature your courses in our newsletter!",candidate_labels=["Marketing","Sales","Support"])print(result["labels"][0],result["scores"][0])

### 🧾 Output (example)Support 0.63 Even though the text sounds marketing-related, the model chose **Support**✔ This is expected — zero-shot models reason based on language semantics

## 🔟 Challenges of Text ClassificationDespite its power, text classification has challenges:

### ⚠️ Ambiguity- Same text can have multiple meanings

### ⚠️ Sarcasm & Irony “Great, another bug in production”    → Sounds positive, actually negative ### ⚠️ Multilingual Complexity- Different grammar rules- Cultural context- Language-specific expressions📌 Solving these requires:- Better preprocessing- Larger & multilingual models- Domain-specific fine-tuning---

## ✅ Key Takeaways for Students- Text classification is a **foundation task** in NLP- Hugging Face pipelines make it **easy and fast**- Different models are trained for different classification tasks- Zero-shot classification enables **flexible labeling**- Real-world data introduces ambiguity and complexity


from transformers import pipeline

classifier = pipeline("sentiment-analysis")

import transformers
print(transformers.__version__)