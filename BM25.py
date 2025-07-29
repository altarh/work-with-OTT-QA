import os
import json
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download("punkt")
nltk.download("stopwords")

# Path to the folder containing the table JSON files
folder_path = "many_random_tables"

# Load and preprocess all tables
tables = []
table_contents = []
file_paths = []

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        file_paths.append(file_path)
        tables.append(data)

        # Concatenate text fields for BM25 matching
        text_parts = [data.get("title", ""), data.get("section_title", ""), data.get("section_text", ""),
                      data.get("intro", "")]

        # Also extract header and cell content
        for row in data.get("data", []):
            for cell in row:
                if cell and isinstance(cell, list) and cell[0]:
                    text_parts.append(cell[0])

        # Tokenize and remove stopwords
        tokens = word_tokenize(" ".join(text_parts).lower())
        tokens = [t for t in tokens if t.isalnum() and t not in stopwords.words("english")]
        table_contents.append(tokens)

# Initialize BM25
bm25 = BM25Okapi(table_contents)

# Your query
query = "What did the 2nd championship win at the Sevens Grand Prix Series for the team with the most top 4 finishes qualify them for ?"
query_tokens = [t for t in word_tokenize(query.lower()) if t.isalnum() and t not in stopwords.words("english")]

# Get scores
scores = bm25.get_scores(query_tokens)

# Get top 30 tables
top_n = 30
top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_n]

# Output results
top_tables = [tables[i] for i in top_indices]
top_file_paths = [file_paths[i] for i in top_indices]

# Example: print file names of top matches
for i, path in enumerate(top_file_paths):
    print(f"{i + 1}. {path} (Score: {scores[top_indices[i]]:.2f})")
