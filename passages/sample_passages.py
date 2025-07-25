import os
import json
import random

# Path to your request_tok directory
input_dir = "/shared/mrkouch/OTT-QA/data/traindev_request_tok"

# Output file
output_file = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/passages/ottqa_50_random_passages.txt"

# Collect all passages
passages = []

for filename in os.listdir(input_dir):
    if not filename.endswith(".json"):
        continue
    with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
        data = json.load(f)
        # Drop the "/wiki/..." keys, keep only text
        passages.extend(data.values())

print(f"Collected {len(passages)} total passages.")

# Sample 50 random ones
sampled_passages = random.sample(passages, 50)

# Save to file
with open(output_file, "w", encoding="utf-8") as f:
    for passage in sampled_passages:
        f.write(passage.strip().replace("\n", " ") + "\n")

print(f"Saved 50 random passages to {output_file}")
