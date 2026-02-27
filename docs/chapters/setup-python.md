# Python Environment

It is time to transition from theory to practice. In this section, we will set up a clean, isolated Python workspace for our RAG project. 

Keeping your project dependencies isolated is a fundamental best practice in data engineering and software development. We will achieve this using Python's built-in virtual environments.

### 1. Create a Virtual Environment

Open your terminal, navigate to the root folder of your project (where you plan to write your code, outside of the `docs` folder), and run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv

```

### 2. Activate the Environment

Before installing any packages, you must activate the environment. The command depends on your operating system:

* **macOS and Linux:**

```bash
source venv/bin/activate

```

* **Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat

```

* **Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1

```

*(You will know it worked if you see `(venv)` at the beginning of your terminal prompt).*

### 3. Install Dependencies

With the environment activated, we need to install the required libraries. We will be using the official **Weaviate v4 Python client**, which is completely rewritten to be highly intuitive and strongly typed. We also need `python-dotenv` to securely manage our API keys.

Run this command:

```bash
pip install -U weaviate-client python-dotenv

```

*Optional:* If you want to use OpenAI's LLMs for the final text generation step of our RAG pipeline, you should also install their official client:

```bash
pip install openai

```

### 4. Secure Your API Keys

Since Weaviate will be reaching out to external AI models (like OpenAI, Cohere, or Google) to generate vectors, it needs an API key. **Never hardcode API keys directly into your Python scripts!** If you push hardcoded keys to GitHub, they will be compromised immediately.

Instead, create a file named exactly `.env` in the root of your project folder. Add your keys there like this:

```env
# .env file
OPENAI_API_KEY="sk-your-openai-api-key-here"

```

Next, create a `.gitignore` file in the same folder and add `.env` to it. This ensures Git will ignore your secrets.

We will use the `python-dotenv` library to load these variables securely into our Python scripts later.

<details>
<summary><strong>✨ Want to use Google Gemini instead? (Click to expand)</strong></summary>

If you prefer to use **Google Gemini** instead of OpenAI for your embeddings and text generation (which is a great choice and offers a generous free tier for developers!), the setup is very similar.

First, you might want to install the Google GenAI SDK (optional, but useful if you want to test the model outside of Weaviate):

```bash
pip install google-genai

```

Then, in your `.env` file, simply add your Gemini API key instead:

```env
# .env file
GEMINI_API_KEY="your-gemini-api-key-here"

```

Later in the code, you will pass this key to Weaviate to enable its built-in Google integration modules (`text2vec-google` and `generative-google`).

</details>

---

Your local machine is now prepped and ready for coding! Next, we need to actually get our Vector Database up and running.
