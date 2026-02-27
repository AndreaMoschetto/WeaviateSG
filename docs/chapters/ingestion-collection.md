# Creating a Collection

Now that we have successfully connected to our database, we need to create a place to store our data. In Weaviate, this is called a **Collection**. 

Think of a Collection as a blueprint. We need to tell Weaviate what properties (columns) our data will have, and more importantly, which AI model it should use to generate the vector embeddings.

Create a new file in your `src` folder named `02_create_collection.py` and add the following code:

```python
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
            model="gemini-2.5-flash" # this model name could change in the future, check the documentation for the latest Gemini models available in Weaviate
        )
    )

    print(f"Collection '{collection_name}' created successfully with Gemini integrations!")

```

### Breaking Down the Code

Let's look at the most important parts of this script:

* **`wvcc.Property(...)`**: Here we define the shape of our data. For this simple RAG example, our `Article` collection will only have a `title` and the main `content`. Both are defined as text.
* **`vector_config`**: This is where Weaviate shines. By setting this to `text2vec_google_gemini()`, we instruct Weaviate to take the text we insert, automatically call Google's embedding API in the background, and store the resulting vector coordinates alongside our text.
* **`generative_config`**: Weaviate also has built-in RAG capabilities. By defining a generative module here and passing a specific model like `gemini-2.5-flash`, we allow Weaviate to take search results and pass them directly to the LLM to generate an answer, all in a single database query.

Run the script from your terminal:

```bash
python src/02_create_collection.py

```

With our `Article` blueprint successfully created, our database is finally ready to receive data.
