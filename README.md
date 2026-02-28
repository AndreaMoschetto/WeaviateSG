# Weaviate RAG Tutorial - Big Data Project

Welcome to the companion repository for the Weaviate Retrieval-Augmented Generation (RAG) tutorial. This project is designed to help students understand vector databases and build a functional AI pipeline from scratch.

## 📖 Documentation
The complete, step-by-step guide is built with mdBook. 
You can read the tutorial online here: **https://andreamoschetto.github.io/WeaviateSG**

## 💻 Code Structure
All Python scripts mentioned in the tutorial are available in the `code/` directory. They are meant to be executed sequentially:
1. `01_setup_connection.py`: Test the connection to the Weaviate cluster.
2. `02_create_collection.py`: Define the data schema and vectorizer.
3. `03_insert_data.py`: Load sample documents and generate embeddings.
4. `04_vector_search.py`: Perform semantic search.
5. `05_rag_pipeline.py`: Execute the complete RAG query.

## 🚀 Quick Start
To run the code locally, set up your environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
