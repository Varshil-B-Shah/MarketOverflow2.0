import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("EMBED_MODEL")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

response = client.embeddings.create(
    input="How do I use Python in VS Code?",
    model=deployment_name
)
print(response.data[0].embedding)