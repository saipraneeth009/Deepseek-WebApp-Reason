import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from azure.ai.inference.models import SystemMessage, UserMessage

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")
model_name = "DeepSeek-R1"

client = ChatCompletionsClient(
    endpoint=os.environ["AZURE_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["AZURE_KEY"]),
    api_version="2024-05-01-preview"
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Can you use python for creating a frontend app?"),
    ],
    model=model_name
)

# print("Response:", response.choices[0].message.content)
for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
