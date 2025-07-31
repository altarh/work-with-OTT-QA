import os
import random
import shutil

# Path to your traindev_tables_tok directory
input_dir = "/shared/mrkouch/OTT-QA/data/traindev_tables_tok"

# Output directory for 1000 random tables
output_dir = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/2000_random_tables"
os.makedirs(output_dir, exist_ok=True)

# Collect all .json table filenames
table_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]
print(f"Found {len(table_files)} table files.")

# Sample 2000 files
sampled_files = random.sample(table_files, 2000)

# Move each sampled file
for filename in sampled_files:
    src = os.path.join(input_dir, filename)
    dst = os.path.join(output_dir, filename)
    shutil.move(src, dst)

print(f"Moved 2000 random tables to {output_dir}")
