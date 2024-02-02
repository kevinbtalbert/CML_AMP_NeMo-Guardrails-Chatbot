<h1> dlchatbot </h1>

A similarity-search based chatbot built using
``` Langchain,OpenAI embeddings,Pinecone Vectordatabase and NeMO-Guardrails ``` <br/>
The chatbot answers questions from the book: Deep Learning with Python by Francois Chollet

<h2> Implementation </h2>

 ```
streamlit run app.py
```

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