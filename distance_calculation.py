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

all_data = ["What did the 2nd championship win at the Sevens Grand Prix Series for the team with the most top 4 finishes qualify them for ?"]


top_50 = ([
    "1990_French_Grand_Prix_0.json",
    "List_of_NFL_franchise_post-season_droughts_6.json",
    "2007_NCAA_Division_I_Baseball_Tournament_1.json",
    "2013_Champions_League_Twenty20_2.json",
    "1967_College_Baseball_All-America_Team_0.json",
    "List_of_Indycar_races_0.json",
    "2004_Japanese_Grand_Prix_0.json",
    "Judd_Trump_0.json",
    "Whiz_Kids_(baseball)_0.json",
    "2007–08_Scottish_Premier_League_13.json",
    "Super_League_XVIII_0.json",
    "List_of_Romanian_football_champions_3.json",
    "Super_League_XIV_0.json",
    "2004_Hungarian_Grand_Prix_0.json",
    "Dancing_with_the_Stars_(U.S._season_16)_0.json",
    "List_of_MLS_Cup_finals_0.json",
    "2003_Spanish_Grand_Prix_0.json",
    "List_of_French_football_champions_0.json",
    "UAE_Arabian_Gulf_League_2.json",
    "Survivor_Series_(1995)_0.json",
    "List_of_Major_League_Baseball_home_run_champions_0.json",
    "2012_Los_Angeles_Galaxy_season_1.json"])
#     "Christian_Taylor_(athlete)_1.json",
#     "List_of_NFL_franchise_post-season_droughts_3.json",
#     "2004_Canadian_Grand_Prix_0.json",
#     "List_of_television_series_produced_by_Paramount_Television_6.json",
#     "2010_IAAF_World_Half_Marathon_Championships_2.json",
#     "List_of_Philadelphia_Flyers_award_winners_2.json",
#     "1999_San_Marino_Grand_Prix_0.json",
#     "Cornwall_League_1_4.json",
#     "Huskies_of_Honor_1.json",
#     "SC_Toronto_0.json",
#     "List_of_Masonic_buildings_in_the_United_States_23.json",
#     "History_of_Michigan_Wolverines_football_in_the_Crisler_years_0.json",
#     "List_of_politicians,_lawyers,_and_civil_servants_educated_at_Jesus_College,_Oxford_2.json",
#     "Veikkausliiga_2.json",
#     "Jon_Finkel_0.json",
#     "Dancing_with_the_Stars_(U.S._season_3)_3.json",
#     "English_Premiership_(rugby_union)_0.json",
#     "2013_FKF_Division_One_2.json",
#     "Golden_Spike_Ostrava_0.json",
#     "Montenegrin_First_League_3.json",
#     "2012_Calgary_Stampeders_season_0.json",
#     "2013_Thai_Division_2_League_North_Eastern_Region_0.json",
#     "CZW_Cage_of_Death_7.json",
#     "2013_Canadian_Soccer_League_season_1.json",
#     "List_of_sports_films_10.json",
#     "Kimiko_Date-Krumm_1.json",
#     "The_Jump_3.json",
#     "2012_NCAA_Women's_Division_I_Basketball_Tournament_0.json"
# ]

###adding gold
nonzo_folder_path = 'gold_tables'
nonzo_filename = "Sevens_Grand_prix_series_0"
file_path = os.path.join(nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")

###adding generated
gen_nonzo_folder_path = 'generated_tables'
gen_nonzo_filename = "Sevens_Grand_prix_series_0"
file_path = os.path.join(gen_nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")


##adding top 50 BM25
the_1000_path = "1000_random_tables"
for filename in top_50:
    file_path = os.path.join(the_1000_path, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_data.append(f"{data}")

encoded_list = interface.encode_text_list(all_data)

# Now all_data is a list of all JSON contents
print(f"Loaded {len(all_data)} JSON files.")

sentences = tables_creating.questions
gold_tables = ""
# print(interface.calculate_distance_list(
#             all_data,
#             encoded_list
#         ))
labels = ["query"] + ["gold"] + ["gen"] + [i for i in range(len(encoded_list) - 3)]

fig = visualization.plot_embeddings_2d_with_distances(encoded_list, labels, highlight_index=0, hover_texts=all_data)
fig.show()

print(all_data)

# def plot_distances_query_to_others(encoded_list, labels, highlight_index = 1)
