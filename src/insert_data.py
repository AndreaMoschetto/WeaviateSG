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
