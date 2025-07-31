import os
import json
import random

# Path to your request_tok directory
input_dir = "/shared/mrkouch/OTT-QA/data/traindev_request_tok"

# Output file
output_file = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/passages/ottqa_10000_random_passages.txt"

# Collect all (title, text) pairs
passages = []

for filename in os.listdir(input_dir):
    if not filename.endswith(".json"):
        continue
    with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
        data = json.load(f)
        for title, text in data.items():
            passages.append({
                "title": title,
                "text": text.strip().replace("\n", " ")
            })

print(f"Collected {len(passages)} total passages.")

# Sample 10,000 random ones
sampled_passages = random.sample(passages, 10000)

# Save to file (one JSON object per line)
with open(output_file, "w", encoding="utf-8") as f:
    for passage in sampled_passages:
        f.write(json.dumps(passage, ensure_ascii=False) + "\n")

print(f"✅ Saved 10,000 random passages to {output_file}")
