# Core Concepts

Before we start writing Python code, we need to understand how Weaviate structures and organizes data. If you have ever used a relational database (like MySQL) or a document database (like MongoDB), these concepts will feel very familiar, but with a specific focus on AI and vectors.



### 1. Collections
In Weaviate, the highest level of data organization is a **Collection** (previously called a *Class* in older versions of Weaviate). You can think of a Collection as a "Table" in a SQL database. 
If you are building a movie recommendation RAG, you might have a `Movie` collection and a `Review` collection. 

When you define a Collection, you also define its configuration, such as which embedding model to use (the *Vectorizer*) and what kind of data it will hold.

### 2. Objects and Properties
Inside a Collection, you store **Objects**. An Object is equivalent to a "Row" in SQL or a "Document" in MongoDB. It represents a single item of data, like one specific movie.

Each Object is made up of **Properties** (equivalent to SQL "Columns"). Properties hold the actual data values. For example, a `Movie` object might have the following properties:
* `title` (text)
* `release_year` (integer)
* `description` (text)

### 3. Vectorizers
This is where Weaviate differs from traditional databases. When you create a Collection, you usually assign a **Vectorizer** to it (e.g., `text2vec-openai` or `text2vec-cohere`). 

When you insert a new Object into that Collection, the Vectorizer automatically takes the text from specific Properties (like the `description`), sends it to the AI model to get the numerical embeddings, and stores those vectors alongside your Object. You don't have to calculate the vectors yourself!

### 4. Cross-References
Just like foreign keys in SQL, Weaviate allows you to link Objects together using **Cross-References**. You can link a `Review` object directly to a `Movie` object. This is incredibly powerful for complex searches, allowing you to retrieve a movie based on the vectors of its connected reviews.

---

### Quick Comparison: SQL vs. Weaviate

To summarize, here is how Weaviate's terminology maps to traditional relational databases:

| Traditional SQL DB | Weaviate Vector DB | Description |
| :--- | :--- | :--- |
| Table | **Collection** | A logical grouping of data with a specific schema. |
| Row | **Object** | A single data record. |
| Column | **Property** | A defined field within an object (e.g., text, int, boolean). |
| Index | **Vector Index (HNSW)** | The algorithm used to make searching through millions of vectors incredibly fast. |
| Foreign Key | **Cross-Reference** | A directional link between objects. |

Now that we understand the vocabulary, we are ready to move on to the architectural pattern we will be building: RAG.