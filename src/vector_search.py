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
