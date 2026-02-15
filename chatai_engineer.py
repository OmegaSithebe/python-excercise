from openai import OpenAI

# Create a client (make sure your OPENAI_API_KEY is set in your environment)
# WARNING: Your API key is exposed in this code! Never share or commit API keys.
client = OpenAI(api_key="sk-proj-HayZxDGrniwhoT8k33cSqjtwCTZ1L-XriDLJAMfygvJGHRiLtLFsMhQ624ZRX5dhitmxQEyRLjT3BLbkFJbgNsr_Jp2ewjGatNUvx0d5LmLIVNmqWav9@LIJ11HxtFxxuJhCy_3k6NFohQjLsTAX700IixsA")

prompt = "Could you explain about OpenAI"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)