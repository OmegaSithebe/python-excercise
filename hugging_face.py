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