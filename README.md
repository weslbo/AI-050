# AI-050: Develop Generative AI Solutions with Azure OpenAI Service

This repository contains a set of Jupyter notebooks you can use to learn about Azure OpenAI service

- [Notebook 01: Get started with Azure OpenAI Service](./module_01.ipynb)
- [Notebook 02: Use Azure OpenAI APIs in your applications](./module_02.ipynb)
- [Notebook 03: Apply prompt engineering with Azure OpenAI Service](./module_03.ipynb)
- [Notebook 04: Generate code with Azure OpenAI Service](./module_04.ipynb)
- [Notebook 05: Generate images with Azure OpenAI Service](./module_05.ipynb)
- [Notebook 06: Use your own data with Azure OpenAI Service](./module_06.ipynb)

Get AI-050 course materials at [https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/)

## Setup

In order to run these samples yourself, you'll need:

- A subscription with Azure OpenAI resource deployed. Recommended to deploy in East US, as we will have to deploy gpt-4o and dall-e-3. Check out [this](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) article for region availability
    - 2 Deploments: gpt-4o and dalle3
- Visual studio Code, with following extensions:
    - Jupyter: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
    - Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python
    - REST client: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- An environment file named [.env] (you have to create this yourself), containing the following entries:

```txt
apikey=yourapikeyfromgpt-4o
endpoint=https://yourazureopenairesource.openai.azure.com/
deployment=gpt-4o
dalle_endpoint=https://yourazureopenairesource.openai.azure.com/
dalle_deployment=dalle3
dalle_apikey=yourapikeyfordalle
```