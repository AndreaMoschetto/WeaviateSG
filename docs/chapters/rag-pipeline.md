# Connecting the Dots

We have successfully ingested our data and learned how to retrieve it using semantic search. Now, it is time to complete our **RAG (Retrieval-Augmented Generation)** pipeline.

The final step is **Generation**. We need to take the raw documents we retrieved and pass them, along with the user's original question, to a Large Language Model (LLM). The LLM will use those documents as its single source of truth to formulate a conversational, accurate answer.

While you could manually write code to build a prompt and send it to the Google Gemini API yourself, Weaviate makes this incredibly easy. Because we added a `generative_config` when we created our Collection, Weaviate can perform the retrieval and the generation in a single database query!

### The Complete RAG Script

Create a new file named `05_rag_pipeline.py` in your `src` folder and add the following code:

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
    
    user_query = "Can you explain what a vector database is and how RAG improves AI models?"
    
    system_prompt = "Answer the user's question using ONLY the provided information. Be concise and clear."
    
    print(f"User Question: {user_query}\n")
    print("Thinking with Gemini...\n")
    
    # Weaviate will find the documents and pass them to Gemini to generate the answer
    response = collection.generate.near_text(
        query=user_query,
        limit=2,
        grouped_task=system_prompt
    )
    
    print("🤖 AI Generated Answer:")
    print("-" * 50)
    print(response.generative.text)
    print("-" * 50)
    
    print("\n📚 Sources Used:")
    for i, obj in enumerate(response.objects, 1):
        print(f" - {obj.properties['title']}")  
```

### Running the Full Pipeline

Run the final script from your terminal:

```bash
python src/05_rag_pipeline.py

```

### Reviewing the Output

When you look at your terminal, you will see a beautifully formatted, natural language answer.

Behind the scenes, in a fraction of a second, Weaviate:

1. Vectorized your question using Google's embedding model.
2. Searched the vector space for the most relevant chunks of text.
3. Extracted the `title` and `content` properties of those chunks.
4. Assembled a hidden prompt containing your `grouped_task` instructions, your original question, and the retrieved text.
5. Sent that prompt to Google's text generation model (like Gemini 2.5 Flash).
6. Returned the clean, finalized string to your Python script.
Congratulations! You have just built a fully functional Retrieval-Augmented Generation AI system from scratch.