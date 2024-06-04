# Contextual Chatbot with Guardrails
## Cloudera Community AMPs

This Applied Machine Learning Prototype (AMP) builds a similarity-search based chatbot built using **Langchain, OpenAI embeddings, Pinecone Vector DB, and NeMo-Guardrails**. This chatbot is designed to showcase how organizations can leverage AI safely and responsibly by implementing guardrails.

![](/assets/demo.png)

### NeMo Guardrails (by NVIDIA)
NeMo Guardrails, developed by NVIDIA, is a cutting-edge solution aimed at ensuring the safety of AI-powered applications across the industry. It is compatible with many large language models (LLMs) including OpenAI's ChatGPT, allowing developers to implement applications that are secure, accurate, and domain-specific. The software introduces three main types of guardrails: topical guardrails that keep conversations within desired subjects, safety guardrails that ensure responses are appropriate and factually accurate, and security guardrails that limit connections to safe, external applications. NeMo Guardrails is accessible to developers of all skill levels, requiring only minimal coding to establish new rules. Its open-source nature ensures compatibility with widely-used enterprise tools like LangChain and integration platforms such as Zapier, highlighting its versatility in enhancing AI application safety without needing extensive machine learning expertise. The initiative has been met with enthusiasm from industry professionals, underscoring its potential to make AI a reliable and trusted technology for the future.

![](/assets/programmable_guardrails_flow.png)

#### Key Features
**1. Programmable Guardrails:** Customize the behavior of your LLM applications to avoid unwanted topics, adhere to predefined dialog paths, or ensure a specific interaction style.


**2. Comprehensive Protection:** Includes mechanisms to safeguard against common LLM vulnerabilities such as jailbreaks and prompt injections.


**3. Versatile Use Cases:** Ideal for question answering systems, domain-specific assistants, LLM endpoints, and more.


**4. Easy Integration:** Minimal changes needed to incorporate guardrails into existing LLM applications, supported by both Python API and a dedicated guardrails server.


<br>5. Supported LLMs:** Compatible with a range of LLMs including OpenAI's GPT-3.5, GPT-4, and others.


### Implementation
This AMP requires an account with OpenAI and Pinecone.io (specifically an API key with both).

<h3> Querying the bot</h3>
<img src="assets/query.png" />

<h3>Testing the guardrails</h3>
<img src="assets/guardrails.png" />

####

### Hardware Requirements
#### CML Instance Types
Given that this leverages OpenAI for its LLM capabilities, NO GPU is required for this to work OOTB.

#### Recommended Runtime
JupyterLab - Python 3.11 - Standard - 2023.08 (or higher)

#### Resource Requirements
This AMP creates the following workloads with resource requirements:
- CML Session: `2 CPU, 8GB MEM`
- CML Jobs: `2 CPU, 4GB MEM`
- CML Application: `2 CPU, 8GB MEM`

#### External Resources
This AMP requires pip packages and models from huggingface. Depending on your CML networking setup, you may need to whitelist some domains:
- pypi.python.org
- pypi.org
- pythonhosted.org
- huggingface.co
- pinecone.io
- platform.openai.com 


#### Content for Semantic Search in `/docs`

Here we leverage several docs from our Cloudera Machine Learning public documentation in `.pdf` format. It is intended that the user will update the contents of the `/docs` directory with their own document repository. This is intended to demonstrate our capabilities with using PDFs (.pdf) as opposed to text (.txt) documents. The user may update with their own set of PDFs or perhaps update the job syntax entirely to support a different data type.

## NeMo Guardrails (from https://github.com/NVIDIA/NeMo-Guardrails)

NeMo Guardrails enables developers building LLM-based applications to easily add **programmable guardrails</br> between the application code and the LLM.

![](/assets/programmable_guardrails.png)

Key benefits of adding programmable guardrails include:

- **Building Trustworthy, Safe, and Secure LLM-based Applications:** you can define rails to guide and safeguard conversations; you can choose to define the behavior of your LLM-based application on specific topics and prevent it from engaging in discussions on unwanted topics.

- **Connecting models, chains, and other services securely:** you can connect an LLM to other services (a.k.a. tools) seamlessly and securely.

- **Controllable dialog:** you can steer the LLM to follow pre-defined conversational paths, allowing you to design the interaction following conversation design best practices and enforce standard operating procedures (e.g., authentication, support).

#### Protecting against LLM Vulnerabilities
NeMo Guardrails provides several mechanisms for protecting an LLM-powered chat application against common LLM vulnerabilities, such as jailbreaks and prompt injections. Below is a sample overview of the protection offered by different guardrails configuration for the example ABC Bot included in this repository. For more details, please refer to the LLM Vulnerability Scanning page.

![](/assets/abc-llm-vulnerability-scan-results.png)

#### Use Cases
You can use programmable guardrails in different types of use cases:

**1. Question Answering over a set of documents (a.k.a. Retrieval Augmented Generation):** Enforce fact-checking and output moderation.


**2. Domain-specific Assistants (a.k.a. chatbots):** Ensure the assistant stays on topic and follows the designed conversational flows.


**3. LLM Endpoints:** Add guardrails to your custom LLM for safer customer interaction.


**4. LangChain Chains:** If you use LangChain for any use case, you can add a guardrails layer around your chains.


Copyright (c) 2023 - 2024 - Cloudera, Inc. All rights reserved.