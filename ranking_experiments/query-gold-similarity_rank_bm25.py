import os
import json
import random
import re
from rank_bm25 import BM25Okapi
import statistics

def clean_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Load random tables into corpus
random_tables_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/2000_random_tables"
corpus = []
file_names = []

for filename in os.listdir(random_tables_path):
    if not filename.endswith(".json"):
        continue
    path = os.path.join(random_tables_path, filename)
    with open(path, "r", encoding="utf-8") as f:
        table_data = json.load(f)
        table_str = json.dumps(table_data)
        tokens = clean_tokenize(table_str)
        corpus.append(tokens)
        file_names.append(filename)

# Load question -> gold table mapping
question_to_table_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/question_table_map.json"
with open(question_to_table_path, "r", encoding="utf-8") as f:
    question_table_map = json.load(f)

# Sample 100 question-gold_table pairs
sample_map = random.sample(list(question_table_map.items()), 100)

gold_tables_dir = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/all_gold_tables"
results = []

for question, table_name in sample_map:
    # Add gold table to the corpus temporarily
    gold_table_path = os.path.join(gold_tables_dir, table_name)
    with open(gold_table_path, "r", encoding="utf-8") as f:
        table_data = json.load(f)
        table_str = json.dumps(table_data)
        gold_tokens = clean_tokenize(table_str)

    # Temporary corpus including gold table
    temp_corpus = corpus + [gold_tokens]
    temp_file_names = file_names + [table_name + " (gold)"]

    # Initialize BM25
    bm25 = BM25Okapi(temp_corpus)
    tokenized_query = clean_tokenize(question)
    scores = bm25.get_scores(tokenized_query)

    # Rank documents
    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    gold_index = len(temp_corpus) - 1  # It's always the last one added

    # Find the rank of the gold table
    rank = ranked_indices.index(gold_index) + 1  # +1 for 1-based rank
    print(f"Query: {question[:80]}... | Gold table rank: {rank}")
    results.append(rank)

print("All ranks:", results)
average = sum(results) /len(results)
print("average rank of tthe gold table: " + str(average))
print(statistics.median(results))


print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")