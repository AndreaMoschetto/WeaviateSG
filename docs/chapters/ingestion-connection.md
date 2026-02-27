# Connecting to the Database

With our environment set up and our database running, it is time to write our first Python script. 

Create a new folder in your project called `src` (or `code`), and inside it, create a file named `01_setup_connection.py`.

### The Python v4 Client

Weaviate's v4 Python client is designed around **Context Managers** (the `with` statement in Python). This is a best practice because it automatically opens the connection to the database when you enter the block and, most importantly, gracefully closes the connection when you exit the block, preventing memory leaks.

Here is the code to connect to your Weaviate Cloud (WCD) instance and verify that it is ready to receive commands:

```python
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

```

### Local Docker Connection Alternative

If you chose **Option B** (Local Docker) in the previous chapter, your connection script is even simpler because you do not need a Weaviate API key or URL. You only need to pass the Gemini key in the headers.

Replace the `connect_to_weaviate_cloud` block with this:

```python
with weaviate.connect_to_local(
    headers={
        "X-Goog-Studio-Api-Key": gemini_api_key
    }
) as client:
    
    if client.is_ready():
        print("Successfully connected to local Weaviate!")
```

### Running the Script

Open your terminal, ensure your virtual environment is still activated, and run the script:

```bash
python src/01_setup_connection.py

```

If everything is configured correctly, you should see `Successfully connected to Weaviate!` printed in your terminal.

Now that we have an active line of communication, we can start shaping how our data will be stored.