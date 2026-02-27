# What is a Vector Database?

To understand what a Vector Database is, we first need to understand how traditional databases fail when it comes to Artificial Intelligence.

In a standard relational database (like PostgreSQL or MySQL), data is stored in rows and columns. If you want to find information, you query it using exact matches or specific keywords. If you search for "dog", the database looks for the exact word "dog". It won't return results containing "puppy" or "canine" unless you explicitly tell it to. Traditional databases lack **context**.

AI models, however, don't read words like humans do; they read numbers.

## The Magic of Embeddings

To make an AI understand text, images, or audio, we must translate that data into arrays of numbers called **Vectors** (or **Embeddings**). 

Imagine a massive multidimensional map. An embedding model assigns coordinates to every piece of data. Concepts that share similar meanings are placed physically close to each other on this map, while unrelated concepts are placed far apart.



For example, the vector coordinates for "apple" will be very close to "banana" (both are fruits), but very far from "spaceship". 

## Why Do We Need a Vector Database?

A Vector Database is purpose-built to store, manage, and query these massive lists of numbers efficiently. 

While a traditional database searches for exact keyword matches, a Vector Database performs a **Semantic Search** (or Similarity Search). When you ask a question, the system converts your question into a vector and looks for the stored vectors that are physically closest to it in that multidimensional space.



**In summary, a Vector Database allows you to:**
* **Search by meaning:** You can search for "how to fix a flat tire" and find an article titled "repairing a punctured wheel," even if they share zero keywords.
* **Handle unstructured data:** Easily manage raw text, PDFs, images, and audio without forcing them into rigid tables.
* **Power AI applications:** Quickly retrieve the most relevant information to feed into an LLM (which is exactly what we will do with RAG).

Now that we know what a Vector Database does, it's time to meet the tool we will be using to build our project.