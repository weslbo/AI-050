import os
import openai
import json
from dotenv import load_dotenv
from openai import AzureOpenAI
from IPython.core.magic import (register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.display import display, Markdown

load_dotenv()

apikey = os.getenv('apikey')
endpoint = os.getenv('endpoint')
deployment = os.getenv('deployment')

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=endpoint,
    api_key=apikey
)

dalle_apikey = os.getenv('dalle_apikey')
dalle_endpoint = os.getenv('dalle_endpoint')
dalle_deployment = os.getenv('dalle_deployment')

dalle_client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=dalle_endpoint,
    api_key=dalle_apikey
)

      
@register_line_cell_magic
def chat(line, cell=None):
    msg = cell if cell is not None else line

    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=[
                {
                    "role": "user",
                    "content": msg,
                }
            ]
        )
    
        display(Markdown(completion.choices[0].message.content))
    except Exception as error:
        print("An exception occurred:", error) 

@register_line_cell_magic
def dalle(line, cell=None):
    msg = cell if cell is not None else line

    try:
        result = dalle_client.images.generate(
            model = dalle_deployment,
            prompt = msg
        )

        display(result.data[0].url)
    except Exception as error:
        print("An exception occurred:", error)         