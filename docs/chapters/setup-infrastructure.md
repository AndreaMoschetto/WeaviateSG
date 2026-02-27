# Weaviate Infrastructure

Weaviate is not just a Python library; it is a full-fledged database server. This means you need to have a Weaviate instance running somewhere before your Python code can interact with it.

For this tutorial, you have two choices for setting up your infrastructure. We highly recommend **Option A** for this course, as it requires zero setup and won't consume your laptop's resources.

---

### Option A: Weaviate Cloud (Recommended)

Weaviate Cloud (WCD) provides a free "Sandbox" tier. This is a fully managed, serverless instance of Weaviate that lives in the cloud and lasts for 14 days (perfect for a university project).



**Step-by-step setup:**
1. Go to the [Weaviate Cloud Console](https://console.weaviate.cloud/) and create a free account.
2. Click on **Create cluster**.
3. Select the **Free Sandbox** tier.
4. Give your cluster a name (e.g., `bigdata-rag-project`) and click **Create**.
5. Wait a minute or two for the cluster to provision. Once it shows a green "Ready" status, click on **Details**.

You will need two crucial pieces of information from this details page:
* **REST Endpoint:** The URL of your cluster (e.g., `https://bigdata-rag-project-xyz.weaviate.network`).
* **Admin API Key:** Click on the "API Keys" button to reveal it.

Open the `.env` file you created in the previous chapter and add these new variables:

```env
# .env file
OPENAI_API_KEY="sk-your-openai-api-key-here"
WEAVIATE_URL="https://your-cluster-url.weaviate.network"
WEAVIATE_API_KEY="your-weaviate-admin-key"

```

---

### Option B: Local Docker Deployment (Advanced)

If you prefer to run everything locally on your own machine, Weaviate provides official Docker images.

Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running. Then, create a file named `docker-compose.yml` in the root of your project folder and paste the following configuration:

```yaml
---
services:
  weaviate:
    command:
    - --host
    - 0.0.0.0
    - --port
    - '8080'
    - --scheme
    - http
    image: cr.weaviate.io/semitechnologies/weaviate:1.24.4
    ports:
    - 8080:8080
    - 50051:50051
    environment:
      QUERY_DEFAULTS_LIMIT: 25
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
      PERSISTENCE_DATA_PATH: '/var/lib/weaviate'
      DEFAULT_VECTORIZER_MODULE: 'text2vec-openai'
      ENABLE_MODULES: 'text2vec-openai,generative-openai'
      CLUSTER_HOSTNAME: 'node1'

```

Open your terminal in the same folder as the `docker-compose.yml` file and run:

```bash
docker compose up -d

```

Your local Weaviate instance will now be running at `http://localhost:8080` (without needing a Weaviate API key).

---

Now that our Python environment is ready and our database is running, the real fun begins. Let's write our first Python script!