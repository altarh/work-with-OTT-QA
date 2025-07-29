import sys
import os
import json
sys.path.append(r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\multi-embedding-comparator")
import embedding_distances.visualization as visualization
import embedding_distances.interface as interface
import tables_creating

####nonso alonzo
# folder_path = "random_tables"
# download_folder = r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\random_tables"
#
# all_data = ["Who created the series in which the character of Robert , played by actor Nonso Anozie , appeared ?"]
#
# nonzo_folder_path = 'gold_tables'
# nonzo_filename = "Nonso_Anozie_1"
# file_path = os.path.join(nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")
#
#
# gen_nonzo_folder_path = 'generated_tables'
# gen_nonzo_filename = "Nonso_Anozie_1"
# file_path = os.path.join(gen_nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")

####Sevens_Grand_prix_series_0
folder_path = "random_tables"
download_folder = r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\random tables"

all_data = ["What did the 2nd championship win at the Sevens Grand Prix Series for the team with the most top 4 finishes qualify them for ?"]

nonzo_folder_path = 'gold_tables'
nonzo_filename = "Sevens_Grand_prix_series_0"
file_path = os.path.join(nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")


gen_nonzo_folder_path = 'generated_tables'
gen_nonzo_filename = "Sevens_Grand_prix_series_0"
file_path = os.path.join(gen_nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")



##adding all the random_tables
for filename in os.listdir(download_folder):
    # if filename.endswith(".json"):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_data.append(data)
encoded_list = interface.encode_text_list(all_data)

# Now all_data is a list of all JSON contents
print(f"Loaded {len(all_data)} JSON files.")

sentences = tables_creating.questions
gold_tables = ""
# print(interface.calculate_distance_list(
#             all_data,
#             encoded_list
#         ))
labels = [i for i in range(len(encoded_list))]

fig = visualization.plot_embeddings_2d_with_distances(encoded_list, labels, highlight_index=2, hover_texts=all_data)
fig.show()

print(all_data)

# def plot_distances_query_to_others(encoded_list, labels, highlight_index = 1)
