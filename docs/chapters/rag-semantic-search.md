# Semantic Search

We have reached the **Retrieval** phase of our RAG pipeline. Our database is populated with vectorized documents, and now we want to extract the most relevant information using a natural language question.

In a traditional SQL database, if you search for "How does the AI access external information?", the database looks for those exact words. If the document says "Retrieval-Augmented Generation," the SQL database will return zero results. 

A Vector Database, however, maps the *meaning* of your question and finds the documents closest to it in the vector space.



### Writing the Search Script

Create a new file named `04_vector_search.py` in your `src` folder and add the following code:

```python
import weaviate
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv

load_dotenv()

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(os.getenv("WEAVIATE_API_KEY")),
    headers={"X-Goog-Studio-Api-Key": os.getenv("GEMINI_API_KEY")}
) as client:
    
    collection = client.collections.get("Article")
    
    user_query = "What happens when an AI model invents fake facts?"
    
    print(f"Executing semantic search for: '{user_query}'\n")
    print("-" * 50)
    
    # The 'near_text' function now automatically vectorizes our query using Gemini
    response = collection.query.near_text(
        query=user_query,
        limit=2,
        return_properties=["title", "content"]
    )
    
    for i, obj in enumerate(response.objects, 1):
        print(f"Result {i}:")
        print(f"Title: {obj.properties['title']}")
        print(f"Content: {obj.properties['content']}")
        print("-" * 50)

```

### Running the Search

Run the script from your terminal:

```bash
python src/04_vector_search.py

```

### Understanding the Output

Look closely at the results in your terminal. You asked about an AI model inventing "fake facts." Weaviate should have returned the article titled "Understanding RAG" as the top result.

Why? Because that article mentions the word "hallucinations." The AI embedding model knows that "inventing fake facts" and "hallucinations" share a very similar semantic meaning, placing their vectors close together.

Weaviate seamlessly handled the vectorization of your search query and the complex K-Nearest Neighbors (KNN) math required to find the closest matches.

Now we have the retrieved context. The final step is to pass this context to an LLM to generate a clean, conversational answer for the user.