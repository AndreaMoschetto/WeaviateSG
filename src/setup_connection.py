import weaviate
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the keys securely
weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 3. Establish the connection using a context manager
with weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
    headers={
        "X-Goog-Studio-Api-Key": gemini_api_key  # We pass this so Weaviate can use Google Gemini
    }
) as client:

    # 4. Check if the connection was successful
    if client.is_ready():
        print("Successfully connected to Weaviate!")
    else:
        print("Failed to connect to Weaviate.")

    # As soon as we exit this 'with' block, the client automatically disconnects.
