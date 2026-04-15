# ---
# pipeline_tag: image-to-image
# library_name: diffusers
# license: apache-2.0
# tags:
# - medical
# - x-ray
# - diffusion-models
# - image-generation
# - miccai
# ---

# # SV-DRR: High-Fidelity Novel View X-Ray Synthesis Using Diffusion Model

# **Paper:** [SV-DRR: High-Fidelity Novel View X-Ray Synthesis Using Diffusion Model](https://huggingface.co/papers/2507.05148) | **Code:** [https://github.com/xiechun298/SV-DRR](https://github.com/xiechun298/SV-DRR)

# ## Abstract
# X-ray imaging is a rapid and cost-effective tool for visualizing internal human anatomy. While multi-view X-ray imaging provides complementary information that enhances diagnosis, intervention, and education, acquiring images from multiple angles increases radiation exposure and complicates clinical workflows. To address these challenges, we propose a novel view-conditioned diffusion model for synthesizing multi-view X-ray images from a single view. Unlike prior methods, which are limited in angular range, resolution, and image quality, our approach leverages the Diffusion Transformer to preserve fine details and employs a weak-to-strong training strategy for stable high-resolution image generation. Experimental results demonstrate that our method generates higher-resolution outputs with improved control over viewing angles. This capability has significant implications not only for clinical applications but also for medical education and data extension, enabling the creation of diverse, high-quality datasets for training and analysis.

# ## TL;DR
# We propose a novel view-conditioned diffusion model for synthesizing multi-view X-ray images up to 1024x1024 resolution from a single view.

# <p align="center">
#     <img src="https://github.com/xiechun298/SV-DRR/raw/main/assets/demo2.gif" alt="demo2.gif" width="500"/>
# </p>

# ## Visual Comparison with SOTA Methods
# ![visulization](https://github.com/xiechun298/SV-DRR/raw/main/assets/visulization.svg)

# ## DRR vs. SV-DRR
# The name SV-DRR, short for Single-View DRR, is inspired by Digitally Reconstructed Radiography (DRR).

# Unlike DRR, which renders X-ray projections from a 3D CT volume, our method synthesizes novel views directly from a single 2D projection.

# ![SV_DRR](https://github.com/xiechun298/SV-DRR/raw/main/assets/SV_DRR.svg)

# ## Usage

# ### 🚀 Quick Start

# #### 🛠️ Environment Setup

# To ensure compatibility and reproducibility, follow these steps to set up the environment:

# 1.  **Clone the Repository**:
#     ```bash
#     git clone https://github.com/xiechun-tsukuba/svdrr.git
#     cd svdrr
#     ```

# 2.  **Create a Python Virtual Environment**:
#     ```bash
#     conda create -f environment.yaml
#     ```

# #### ⏬ Download Pretrained Models

# You can download the pretrained models by either:

# **Option 1: Automated Download (Recommended)**
# ```bash
# python scripts/download_models.py
# ```
# This will download all models into the `models/` directory. Shared components will be stored in the `shared/` folder, and symbolic links will be created in each model folder accordingly.

# **Option 2: Manual Download from Hugging Face**
# - 256 resolution: https://huggingface.co/xiechun-tsukuba/svdrr-dit-fb-256
# - 512 resolution: https://huggingface.co/xiechun-tsukuba/svdrr-dit-fb-512
# - 1024 resolution: https://huggingface.co/xiechun-tsukuba/svdrr-dit-fb-1024

# ### 🔍 Inference

# **Important Note:** The coordinate system of LIDC-IDRI-DRR is opposite to the intuitive one — the polar angle increases downward, and the azimuth angle increases when rotating to the left. To invert the pose coordinate system, use the `--flip_pose` option.

# #### Single Image Inference

# **Default views (azimuth angles from -90° to 90° in 5° increments):**
# ```bash
# python test_svdrr_DiT.py --model_path models/DiT-fb-512 \
#     --image_path demo/real_xray.jpg \
#     --log_dir outputs/ \
#     --image_size 512 \
#     --simple_pose
# ```

# ## Citation
# If you find this work useful, a citation will be appreciated via:

# ```bibtex
# @InProceedings{XieChu_SVDRR_MICCAI2025,
#         author = { Xie, Chun AND Yoshii, Yuichi AND Kitahara, Itaru},
#         title = { { SV-DRR: High-Fidelity Novel View X-Ray Synthesis Using Diffusion Model } },
#         booktitle = {proceedings of Medical Image Computing and Computer Assisted Intervention -- MICCAI 2025},
#         year = {2025},
#         publisher = {Springer Nature Switzerland},
#         volume = {LNCS 15963},
#         month = {September},
#         page = {572 -- 582},
#         doi = {https://doi.org/10.1007/978-3-032-04965-0_54}
# }

# @misc{xie2025svdrr,
#         title = {SV-DRR: High-Fidelity Novel View X-Ray Synthesis Using Diffusion Model}, 
#         author = {Chun Xie and Yuichi Yoshii and Itaru Kitahara},
#         year = {2025},
#         eprint = {2507.05148},
#         archivePrefix = {arXiv},
#         doi = {https://doi.org/10.48550/arXiv.2507.05148}, 
# }
# ```

#import the pipeline
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

for result in results:
    print(result['generated_text'])
    
    
#Experimenting different prompts
results = gpt2_pipeline(
    "How to build a successful startup",
    max_new_tokens=15,
    num_return_sequences=3
)

































#AI ChatGPT clear step by step explaination
# You’re doing the right thing by slowing down and understanding the mechanics instead of just copying code. Hugging Face pipelines are designed to **abstract the complexity of machine learning models**, so beginners can use powerful models like GPT-2 with only a few lines of code.

# I'll walk you through this **step-by-step like we would with a junior engineer in a production environment.**

# ---

# # 1. What Hugging Face Actually Is

# Hugging Face provides open-source tools and pre-trained AI models. Instead of training your own AI model (which requires huge datasets and GPUs), you **download a trained model and use it immediately**.

# The key library you’re using is:

# * Transformers

# It contains thousands of models for tasks like:

# | Task               | Example             |
# | ------------------ | ------------------- |
# | Text generation    | GPT-2               |
# | Translation        | English → French    |
# | Sentiment analysis | Positive / Negative |
# | Question answering | Chatbots            |

# ---

# # 2. What a Pipeline Is (Core Concept)

# A **pipeline** is a **ready-made workflow** that does 3 things automatically:

# 1️⃣ Loads the model
# 2️⃣ Loads the tokenizer
# 3️⃣ Runs inference on your input

# Without pipelines, using models would look like **100+ lines of code**.

# With pipelines:

# ```python
# pipeline("text-generation")
# ```

# That's it.

# ---

# # 3. Step 1 — Install Required Libraries

# Your code shows:

# ```bash
# uv add torch transformers
# ```

# But beginners typically use:

# ```bash
# pip install torch transformers
# ```

# ### What these libraries do

# | Library      | Purpose                    |
# | ------------ | -------------------------- |
# | torch        | Deep learning engine       |
# | transformers | Hugging Face model library |

# ---

# # 4. Step 2 — Import the Pipeline

# ```python
# from transformers import pipeline
# ```

# This imports the **pipeline function** from the Transformers library.

# Think of it like importing a tool from a toolbox.

# ---

# # 5. Step 3 — Create a Text Generation Pipeline

# Your code:

# ```python
# gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")
# ```

# ### What this does internally

# | Step | What Happens                |
# | ---- | --------------------------- |
# | 1    | Downloads GPT-2 model       |
# | 2    | Downloads tokenizer         |
# | 3    | Prepares inference pipeline |

# The model used is:

# GPT-2

# GPT-2 is a **language model trained to predict the next word in a sentence**.

# Example training idea:

# ```
# Input: The cat sat on the
# Prediction: mat
# ```

# ---

# # 6. Step 4 — Provide a Prompt

# Your code:

# ```python
# results = gpt2_pipeline("What if AI", max_new_tokens=10, num_return_sequences=2)
# ```

# This sends a **prompt** to the model.

# Prompt:

# ```
# "What if AI"
# ```

# The model then predicts **what words should come next**.

# ---

# # 7. Understanding the Parameters

# ### max_new_tokens

# ```python
# max_new_tokens=10
# ```

# This tells the model:

# > Generate **at most 10 new words/tokens**

# Example:

# Prompt:

# ```
# What if AI
# ```

# Output:

# ```
# What if AI could learn emotions and build deeper relationships
# ```

# But it will **stop after ~10 tokens**.

# ---

# ### num_return_sequences

# ```python
# num_return_sequences=2
# ```

# This tells the model:

# > Generate **2 different answers**

# Example output:

# ```
# 1. What if AI became smarter than humans overnight
# 2. What if AI started writing its own laws
# ```

# The model produces **different variations**.

# ---

# # 8. Step 5 — Print the Results

# Your code:

# ```python
# for result in results:
#     print(result['generated_text'])
# ```

# Important concept:

# The pipeline returns a **list of dictionaries**.

# Example structure:

# ```python
# [
#   {"generated_text": "What if AI ruled the world someday"},
#   {"generated_text": "What if AI discovered a new form of intelligence"}
# ]
# ```

# Your loop extracts the text.

# ---

# # 9. Full Working Code (Clean Version)

# ```python
# from transformers import pipeline

# # Create the pipeline
# gpt2_pipeline = pipeline(
#     task="text-generation",
#     model="openai-community/gpt2"
# )

# # Generate text
# results = gpt2_pipeline(
#     "What if AI",
#     max_new_tokens=10,
#     num_return_sequences=2
# )

# # Print results
# for result in results:
#     print(result["generated_text"])
# ```

# ---

# # 10. Example Output

# You might see something like:

# ```
# What if AI becomes powerful enough to control human decisions

# What if AI could design cities smarter than humans ever could
# ```

# Outputs change **every time you run the code**.

# ---

# # 11. Experiment (What Hugging Face Wants You To Do)

# Try prompts like:

# ```
# "What if humans lived on Mars"
# ```

# ```
# "How to become successful"
# ```

# ```
# "In the future AI will"
# ```

# ---

# # 12. Important Engineering Insight

# A pipeline like this is **inference**, not training.

# Meaning:

# | Action    | Meaning               |
# | --------- | --------------------- |
# | Training  | Teaching a model      |
# | Inference | Using a trained model |

# You are doing **inference**.

# ---

# # 13. Real World Application

# This same pipeline architecture powers:

# * Chatbots
# * Code generators
# * Writing assistants
# * Customer service AI
# * AI copilots

# For example:

# * GPT-4
# * ChatGPT

# are **advanced versions of this concept**.

# ---

# # 14. What Hugging Face Is Secretly Teaching You

# This small exercise introduces **three critical ML engineering skills**:

# 1️⃣ Model loading
# 2️⃣ Prompt engineering
# 3️⃣ Output control

# ---

# # 15. Your Next Level (What I Would Assign an Intern)

# Try modifying this:

# ```python
# results = gpt2_pipeline(
#     "How to build a successful startup",
#     max_new_tokens=15,
#     num_return_sequences=3
# )
# ```

# Then observe:

# * How outputs change
# * How token length changes
# * How creativity changes




