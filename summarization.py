from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Test with a sample text
text = """
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, 
and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. 
During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest 
man-made structure in the world, a title it held for 41 years until the Chrysler Building in New 
York City was finished in 1930. It was the first structure to reach a height of 300 metres. 
Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller 
than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is 
the second tallest free-standing structure in France after the Millau Viaduct.
"""

# Tokenize input
inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)

# Generate summary
summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=25, do_sample=False)

# Decode summary
summary_text = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]
print(summary_text)