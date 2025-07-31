import os
import json
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

# Step 1: Load tables and tokenize content
folder_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/1000_random_tables"
corpus = []
file_names = []

# add the gold document to the corpus
gold_dir = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/gold_tables"
gold_path = os.path.join(gold_dir, "Budapest_0")
with open(gold_path, "r", encoding="utf-8") as f:
        table_data = json.load(f)
        table_str = json.dumps(table_data)
        tokens = table_str.split()
        corpus.append(tokens)
        file_names.append("Budapest_0")

for filename in os.listdir(folder_path):
    if not filename.endswith(".json"):
        continue
    path = os.path.join(folder_path, filename)
    with open(path, "r", encoding="utf-8") as f:
        table_data = json.load(f)
        table_str = json.dumps(table_data)
        tokens = table_str.split()
        corpus.append(tokens)
        file_names.append(filename)

# Step 2: Initialize BM25
bm25 = BM25Okapi(corpus)

# Step 3: Define and tokenize your query
query = "How many academic staff are at the university in Budapest that has the official abbreviation BME ?"
tokenized_query = query.split()


# Step 4: Score all documents
scores = bm25.get_scores(tokenized_query)

# Step 5: Print top 50 results
ranked = sorted(zip(file_names, scores), key=lambda x: x[1], reverse=True)[:50]

print("\nTop 50 documents ranked by BM25:")
for i, (fname, score) in enumerate(ranked):
    print(f"{i+1:>2}. {fname:50} | Score: {score:.4f}")

print("------------------------------------------------------------------------------------")

generated = None
generated_dir = "OTT-QA/work-with-OTT-QA/generated_tables"
generaed_path = os.path.join(generated_dir, "Budapest_0.json")
with open(generaed_path, "r", encoding="utf-8") as f:
        table_data = json.load(f)
        table_str = json.dumps(table_data)
        generated = table_str.split()

scores_2 = bm25.get_scores(generated)
ranked_2 = sorted(zip(file_names, scores_2), key=lambda x: x[1], reverse=True)[:50]
print("\nTop 50 documents ranked by BM25:")
for i, (fname, score) in enumerate(ranked_2):
    print(f"{i+1:>2}. {fname:50} | Score: {score:.4f}")