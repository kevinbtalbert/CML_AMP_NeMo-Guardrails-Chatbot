# Contextual Chatbot with Guardrails
## Cloudera Community AMPs

A similarity-search based chatbot built using <b>Langchain, OpenAI embeddings, Pinecone Vector DB and NeMo-Guardrails</b><br>
This chatbot is designed to showcase how organizations can leverage AI safely and responsibly by implementing guardrails.

### NeMo Guardrails (by NVIDIA)

NeMo Guardrails is an innovative, open-source toolkit designed to empower developers with the ability to integrate programmable guardrails into large language model (LLM)-based conversational applications. It offers a versatile approach to managing the output of LLMs, ensuring conversations are safe, secure, and aligned with specified guidelines.

#### Key Features
Programmable Guardrails: Customize the behavior of your LLM applications to avoid unwanted topics, adhere to predefined dialog paths, or ensure a specific interaction style.


Comprehensive Protection: Includes mechanisms to safeguard against common LLM vulnerabilities such as jailbreaks and prompt injections.


Versatile Use Cases: Ideal for question answering systems, domain-specific assistants, LLM endpoints, and more.


Easy Integration: Minimal changes needed to incorporate guardrails into existing LLM applications, supported by both Python API and a dedicated guardrails server.


Supported LLMs: Compatible with a range of LLMs including OpenAI's GPT-3.5, GPT-4, and others.


### Implementation
This AMP requires an account with OpenAI and Pinecone.io (specifically an API key with both).

<h3> Querying the bot</h3>
<img src="assets/query.png" />

<h3>Testing the guardrails</h3>
<img src="assets/guardrails.png" />


#### Content for Semantic Search in `/docs`

Here we leverage several chapters of the free textbook "Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville available for free at https://www.deeplearningbook.org/
It is intended that the user will update the contents of the `/docs` directory with their own document repository. This is intended to demonstrate our capabilities with using PDFs (.pdf) as opposed to text (.txt) documents. The user may update with their own set of PDFs or perhaps update the job syntax entirely to support a different data type.

Bibliographic / Citation Information:

@book{Goodfellow-et-al-2016,
    title={Deep Learning},
    author={Ian Goodfellow and Yoshua Bengio and Aaron Courville},
    publisher={MIT Press},
    note={\url{http://www.deeplearningbook.org}},
    year={2016}
}