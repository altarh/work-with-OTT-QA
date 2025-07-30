import os
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Ensure required NLTK data is available
nltk.download('punkt')
nltk.download('stopwords')

# === Step 1: Load documents from a folder ===
folder_path = "1000_random_tables"  # Update with your folder path

documents = []
for filename in os.listdir(folder_path):
    # if filename.endswith(".txt"):
    with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
        text = f.read()
        documents.append(Document(page_content=text, metadata={"source": filename}))

# === Step 2: Initialize BM25 Retriever ===
retriever = BM25Retriever.from_documents(documents)

# === Step 3: Preprocess and set search parameters ===
retriever.k = 50  # number of top documents to retrieve

# === Step 4: Define your query ===
query = "What did the 2nd championship win at the Sevens Grand Prix Series qualify the team for?"

# === Step 5: Retrieve and display top documents ===
results = retriever.get_relevant_documents(query)

print(f"\nTop {len(results)} relevant documents:")
for i, doc in enumerate(results):
    # print(f"{i+1}. Source: {doc.metadata['source']}")
    print(f"{doc.metadata['source']}")
    # print(doc.page_content[:200] + "...\n")  # Print first 200 characters
