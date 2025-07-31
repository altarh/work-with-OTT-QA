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
folder_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/1000_random_tables"  # Update with your folder path

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
query = "How many academic staff are at the university in Budapest that has the official abbreviation BME ?"

# === Step 5: Retrieve and display top documents ===
# After retrieving results:
results = retriever.get_relevant_documents(query)

# 1. Get the internal BM25 object (not public API, but works)
bm25_index = retriever._bm25  # underscore = protected, but accessible

# 2. Tokenize your query just like the retriever would
tokenized_query = bm25_index.tokenizer(query)

# 3. Get scores for ALL documents
scores = bm25_index.bm25.get_scores(tokenized_query)  # 1 score per document

# 4. Map scores to file names
filename_score_pairs = []
for doc, score in zip(documents, scores):
    filename = doc.metadata['source']
    filename_score_pairs.append((filename, score))

# 5. Sort and print top 50
top_50 = sorted(filename_score_pairs, key=lambda x: x[1], reverse=True)[:50]

for i, (fname, score) in enumerate(top_50):
    print(f"{i+1:>2}. {fname:50} | BM25 score: {score:.4f}")
