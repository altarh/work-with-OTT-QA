import json

# Load JSON data from file
with open(r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\gold.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a dictionary of question to table_id
question_table_map = {item["question"]: item["table_id"] for item in data}

# Optional: print or save to verify
for question, table_id in question_table_map.items():
    print(f"Question: {question}\nTable ID: {table_id}\n")

# Save to new JSON file
with open("question_table_map.json", "w", encoding="utf-8") as f_out:
    json.dump(question_table_map, f_out, indent=2, ensure_ascii=False)
