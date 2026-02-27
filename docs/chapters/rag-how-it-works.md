# How RAG Works

**Retrieval-Augmented Generation (RAG)** might sound like a complex academic term, but the concept is actually very straightforward. Think of it as giving an AI an "open-book exam." Instead of relying on its flawed internal memory, the AI is allowed to look up the exact facts in a trusted database before answering.



A standard RAG pipeline is always divided into three distinct phases: **Ingestion**, **Retrieval**, and **Generation**.

### Phase 1: Ingestion (Data Preparation)
Before we can search for anything, we need to populate our database. This happens behind the scenes before the user even asks a question.
1. **Load Data:** We gather our private documents (PDFs, text files, website scrapes).
2. **Chunking:** LLMs and embedding models have limits on how much text they can process at once. We break our large documents into smaller, meaningful pieces called "chunks" (e.g., a few paragraphs each).
3. **Embedding:** We pass these chunks through an AI model to convert the text into numerical vectors. 
4. **Storage:** We save the original text and its corresponding vector into our Vector Database (**Weaviate**).

### Phase 2: Retrieval (The Search)
Now the system is ready for the user. 
1. **The Query:** The user asks a question in natural language (e.g., *"What is the university's policy on remote exams?"*).
2. **Query Embedding:** The system takes the user's question and converts it into a vector using the *exact same* embedding model used in Phase 1.
3. **Semantic Search:** Weaviate compares the question's vector against all the document vectors in the database. It instantly retrieves the "Top K" (e.g., the top 3) most mathematically similar chunks. These chunks represent the most relevant information needed to answer the question.

### Phase 3: Generation (The Answer)
This is where the magic happens. We don't just show the raw retrieved chunks to the user; we use an LLM to synthesize a perfect answer.
1. **Prompt Construction:** We build a prompt that combines the user's original question with the text of the retrieved chunks. We give the LLM strict instructions: *"Answer the user's question using ONLY the provided context."*
2. **Final Output:** The LLM reads the context, understands it, and generates a natural, accurate, and conversational response for the user. No hallucinations, just facts!

---

### 💡 The Librarian Analogy
To easily remember this, think of RAG as a team effort between a **Librarian** and a **Scholar**:
* The **Vector Database (Weaviate)** is the ultra-fast Librarian. When you ask a question, the Librarian runs into the archives, finds the three most relevant book pages, and hands them to the Scholar.
* The **LLM (ChatGPT, Llama, etc.)** is the brilliant Scholar. The Scholar doesn't need to memorize the entire library. They just read the three pages the Librarian provided and write a beautiful, accurate essay based on them.

With this theory out of the way, we are finally ready to get our hands dirty with code!