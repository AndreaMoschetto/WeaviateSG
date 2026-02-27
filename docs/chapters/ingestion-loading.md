# Loading Documents

Our `Article` collection is created and waiting. Now, we need to populate it with some actual text. 

In a real-world Big Data scenario, you would be loading thousands of rows from a JSON file, a CSV, or scraping a company wiki. To keep things simple and focused on the mechanics, we will define a small list of dictionaries directly in our Python script.

Create a new file named `03_insert_data.py` in your `src` folder and add the following code:

```python
import weaviate
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv

load_dotenv()

documents = [
    {
        "title": "Introduction to Vector Databases",
        "content": "A vector database is a type of database that stores data as high-dimensional vectors. This allows for similarity search, where the database can find data that is semantically similar to a given query, rather than just exact keyword matches."
    },
    {
        "title": "Understanding RAG",
        "content": "Retrieval-Augmented Generation (RAG) is a technique that enhances large language models by retrieving relevant information from an external knowledge base before generating a response. This reduces hallucinations and keeps the information up to date."
    },
    {
        "title": "Weaviate Architecture",
        "content": "Weaviate is an open-source vector database. It uses modular architecture, allowing users to plug in different machine learning models for vectorization, such as Google Gemini, Hugging Face, or Cohere. It stores both objects and vectors."
    }
]

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(os.getenv("WEAVIATE_API_KEY")),
    headers={"X-Goog-Studio-Api-Key": os.getenv("GEMINI_API_KEY")}
) as client:
    
    collection = client.collections.get("Article")
    
    print(f"Inserting {len(documents)} documents into Weaviate...")
    
    # Batch insertion
    response = collection.data.insert_many(documents)
    
    if response.has_errors:
        print("Errors occurred during insertion:")
        for error in response.errors:
            print(error)
    else:
        print("Successfully inserted all documents!")
        print("Notice: We did not calculate any vectors manually. Weaviate called Gemini in the background.")

```

### The Magic of Automatic Vectorization

Run the script from your terminal:

```bash
python src/03_insert_data.py

```

If it succeeds, pause for a moment and look at the code. **Did you notice what is missing?**

Nowhere in this script did we import an AI library to calculate embeddings. We didn't write code to convert our text strings into arrays of floats. We just threw standard Python strings at Weaviate.

Because we configured the Collection with `text2vec_google_gemini()`, Weaviate intercepted our raw data, securely sent it to Google AI Studio to get the vector coordinates, and stored both the text and the vectors together.

This completes the **Ingestion** phase. Our database is now fully populated and vectorized. Next, we will learn how to extract this knowledge using Semantic Search.
