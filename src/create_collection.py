import weaviate
import weaviate.classes.config as wvcc
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv

load_dotenv()

with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(os.getenv("WEAVIATE_API_KEY")),
    headers={"X-Goog-Studio-Api-Key": os.getenv("GEMINI_API_KEY")}
) as client:

    collection_name = "Article"

    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
        print(f"Old collection '{collection_name}' deleted.")

    print(f"Creating collection '{collection_name}'...")
    client.collections.create(
        name=collection_name,
        properties=[
            wvcc.Property(name="title", data_type=wvcc.DataType.TEXT),
            wvcc.Property(name="content", data_type=wvcc.DataType.TEXT),
        ],

        # 3. Vectorizer for Google Gemini
        vector_config=wvcc.Configure.Vectors.text2vec_google_gemini(),

        # 4. Generative Module: SPECIFYING THE GEMINI MODEL!
        generative_config=wvcc.Configure.Generative.google_gemini(
            model="gemini-2.5-flash"  # this model name could change in the future, check the documentation for the latest Gemini models available in Weaviate
        )
    )

    print(f"Collection '{collection_name}' created successfully with Gemini integrations!")
