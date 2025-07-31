import os
import json
from rank_bm25 import BM25Okapi
from nltk.tokenize import wordpunct_tokenize
import nltk

nltk.download("punkt")



# Step 1: Load tables and tokenize content
file_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/passages/ottqa_10000_random_passages.txt"
corpus = []
file_names = []

# add the gold document to the corpus
gold_passage_1_name = "/wiki/Gibson_Motorsport (gold)"
gold_passage_1 = "Gibson Motorsport was an Australian motor racing team that competed in the Australian Touring Car Championship from 1981 until 2003 , though the team had its roots in Gibson 's Road & Track team which ran a series of Ford Falcon GTHOs in Series Production during the late 1960s and early 1970s . The name of the team was also the name of Fred Gibson 's automotive business in Sydney . As Gibson was also a driver for the Ford Works Team , his team was sometimes a pseudo-works team when the Ford factory did not enter ."
gold_passage_2_name = "/wiki/Tony_Longhurst (gold)"
gold_passage_2 = "Tony Longhurst ( born 1 October 1957 in Sydney ) is an Australian racing driver and former Australian Champion water skier . He is most noted for his career in the Australian Touring Car Championship and V8 Supercar series ."

file_names.append(gold_passage_1_name)
file_names.append(gold_passage_2_name)

corpus.append(gold_passage_1)
corpus.append(gold_passage_2)

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            passage_data = json.loads(line)
            file_names.append(passage_data["title"])
            corpus.append(passage_data["text"])
        except json.JSONDecodeError:
            print(f"⚠️ Skipping invalid line: {line[:100]}...")

print(f"✅ Final corpus size: {len(corpus)} (including 2 gold passages)")

# Step 2: Initialize BM25
# Tokenize corpus
tokenized_corpus = [wordpunct_tokenize(doc.lower()) for doc in corpus]
# Initialize BM25 with tokenized documents
bm25 = BM25Okapi(tokenized_corpus)


# Step 3: Define and tokenize your query
query = "The 1995 Tooheys 1000 driver who was second-to-last in the Tooheys Top 10 was born where ?"
# Tokenize query
tokenized_query = wordpunct_tokenize(query.lower())

# Score documents
scores = bm25.get_scores(tokenized_query)


# Step 5: Print top 50 results
ranked = sorted(zip(file_names, scores), key=lambda x: x[1], reverse=True)[:200]

print("\nTop 200 documents ranked by BM25:")
for i, (fname, score) in enumerate(ranked):
    print(f"{i+1:>2}. {fname:200} | Score: {score:.4f}")

# print("------------------------------------------------------------------------------------")

# generated = None
# generated_dir = "OTT-QA/work-with-OTT-QA/generated_tables"
# generaed_path = os.path.join(generated_dir, "Budapest_0.json")
# with open(generaed_path, "r", encoding="utf-8") as f:
#         table_data = json.load(f)
#         table_str = json.dumps(table_data)
#         generated = table_str.split()

# scores_2 = bm25.get_scores(generated)
# ranked_2 = sorted(zip(file_names, scores_2), key=lambda x: x[1], reverse=True)[:50]
# print("\nTop 50 documents ranked by BM25:")
# for i, (fname, score) in enumerate(ranked_2):
#     print(f"{i+1:>2}. {fname:50} | Score: {score:.4f}")