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
