from datasets import load_dataset

# Load dataset from Hugging Face Hub
dataset = load_dataset("imdb")

# Print dataset structure
print("Dataset structure:")
print(dataset)

print("\nFirst training example:")
print(dataset["train"][0])

print("\nFirst 3 examples:")

for i in range(3):
    print(dataset["train"][i]["text"][:200])  # show first 200 characters
    print("Label:", dataset["train"][i]["label"])
    print("-" * 40)
    
    
    
    

# Dataset structure:
# DatasetDict({
#   train: Dataset({
#       features: ['text', 'label'],
#       num_rows: 25000
#   })
#   test: Dataset({
#       features: ['text', 'label'],
#       num_rows: 25000
#   })
# })

# First training example:
# {
#  'text': 'I rented this movie...',
#  'label': 0
# }

# First 3 examples:
# I rented this movie because...
# Label: 0
# ----------------------------------------
# This film was amazing...
# Label: 1
# ----------------------------------------
# Terrible movie...
# Label: 0
# ----------------------------------------







from datasets import load_dataset

dataset = load_dataset("imdb")

train_data = dataset["train"]

positive = 0
negative = 0

for i in range(5):
    review = train_data[i]["text"]
    label = train_data[i]["label"]

    print(f"\nReview {i+1}:")
    print(review[:150])
    print("Label:", label)

    if label == 1:
        positive += 1
    else:
        negative += 1

print("\nSummary:")
print("Positive:", positive)
print("Negative:", negative)