import sys
import os
import json
sys.path.append(r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\multi-embedding-comparator")
import embedding_distances.visualization as visualization
import embedding_distances.interface as interface
import tables_creating
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')

def tokenize(text):
    return [word.lower() for word in word_tokenize(text) if word.isalnum()]

####nonso alonzo
folder_path = "random_tables"
download_folder = r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\random_tables"

all_data = ["Who created the series in which the character of Robert , played by actor Nonso Anozie , appeared ?"]

top_50 =([
    "2010_in_American_television_7.json",
    "Hayden_Panettiere_0.json",
    "Matt_Lanter_2.json",
    "Hayden_Panettiere_1.json",
    "National_Recording_Registry_1.json",
    "Jake_Abel_1.json",
    "List_of_lacrosse_teams_in_Canada_15.json",
    "Timeline_of_open-source_software_2.json",
    "The_Jump_3.json",
    "List_of_fictional_princesses_0.json",
    "National_Recording_Registry_12.json",
    "Editio_Regia_0.json",
    "1959_British_Lions_tour_to_Australia_and_New_Zealand_0.json",
    "Olu_Jacobs_2.json",
    "List_of_Baldur's_Gate_characters_0.json",
    "Mischa_Barton_0.json",
    "List_of_fictional_princesses_6.json",
    "Awards,_lectures_and_medals_of_the_Royal_Society_0.json",
    "Dinky_Toys_0.json",
    "Celia_Kaye_1.json",
    "Sioux_0.json",
    "List_of_longest_tunnels_in_the_world_1.json",
    "National_Recording_Registry_4.json",
    "List_of_electronic_sports_tournaments_0.json",
    "Stanley_Cup_Finals_2.json",
    "Super_Bowl_2.json",
    "Harry_Lloyd_3.json",
    "Michael_Sheen_performances_0.json",
    "List_of_National_Historic_Sites_of_Canada_in_Kingston,_Ontario_0.json",
    "Fatal_dog_attacks_in_the_United_States_6.json",
    "List_of_film_spoofs_in_Mad_4.json",
    "WLIR_0.json",
    "List_of_American_Civil_War_Generals_(Union)_12.json",
    "Case_citation_8.json",
    "List_of_closed_railway_lines_in_Great_Britain_0.json",
    "List_of_National_Trust_properties_in_Somerset_0.json",
    "List_of_programs_broadcast_by_Toonami_1.json",
    "List_of_Nobel_laureates_affiliated_with_the_University_of_Pennsylvania_0.json",
    "List_of_Medal_of_Honor_recipients_for_World_War_II_4.json",
    "List_of_fictional_crocodiles_and_alligators_4.json",
    "McDonald's_All-American_Game_3.json",
    "List_of_Medal_of_Honor_recipients_for_World_War_II_8.json",
    "Rubina_Dilaik_0.json",
    "Warren_Alpert_Foundation_Prize_0.json",
    "List_of_places_of_worship_in_Arun_1.json",
    "Neighborhoods_in_Detroit_0.json",
    "List_of_Jewish_actors_11.json",
    "Chinese_Super_League_3.json",
    "World_record_progression_200_metres_breaststroke_3.json",
    "List_of_MLS_Cup_finals_0.json"
])


nonzo_folder_path = 'gold_tables'
nonzo_filename = "Nonso_Anozie_1"
file_path = os.path.join(nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")


gen_nonzo_folder_path = 'generated_tables'
gen_nonzo_filename = "Nonso_Anozie_1"
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

####Sevens_Grand_prix_series_0

# all_data = ["What did the 2nd championship win at the Sevens Grand Prix Series for the team with the most top 4 finishes qualify them for ?"]
#
#
# top_50 = ([
#     "1990_French_Grand_Prix_0.json",
#     "List_of_NFL_franchise_post-season_droughts_6.json",
#     "2007_NCAA_Division_I_Baseball_Tournament_1.json",
#     "2013_Champions_League_Twenty20_2.json",
#     "1967_College_Baseball_All-America_Team_0.json",
#     "List_of_Indycar_races_0.json",
#     "2004_Japanese_Grand_Prix_0.json",
#     "Judd_Trump_0.json",
#     "Whiz_Kids_(baseball)_0.json",
#     "2007–08_Scottish_Premier_League_13.json",
#     "Super_League_XVIII_0.json",
#     "List_of_Romanian_football_champions_3.json",
#     "Super_League_XIV_0.json",
#     "2004_Hungarian_Grand_Prix_0.json",
#     "Dancing_with_the_Stars_(U.S._season_16)_0.json",
#     "List_of_MLS_Cup_finals_0.json",
#     "2003_Spanish_Grand_Prix_0.json",
#     "List_of_French_football_champions_0.json",
#     "UAE_Arabian_Gulf_League_2.json",
#     "Survivor_Series_(1995)_0.json",
#     "List_of_Major_League_Baseball_home_run_champions_0.json",
#     "2012_Los_Angeles_Galaxy_season_1.json",
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
#     "2012_NCAA_Women's_Division_I_Basketball_Tournament_0.json"])
#
# ###adding gold
# nonzo_folder_path = 'gold_tables'
# nonzo_filename = "Sevens_Grand_prix_series_0"
# file_path = os.path.join(nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")
#
# ###adding generated
# gen_nonzo_folder_path = 'generated_tables'
# gen_nonzo_filename = "Sevens_Grand_prix_series_0"
# file_path = os.path.join(gen_nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")
#
#
# ##adding top 50 BM25
# the_1000_path = "1000_random_tables"
# for filename in top_50:
#     file_path = os.path.join(the_1000_path, filename)
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
#         all_data.append(f"{data}")
# #################################





#######################
####Kishore_Kumar_1

# all_data = ["The 1995 Tooheys 1000 driver who was second-to-last in the Tooheys Top 10 was born where ?"]
# top_50 = ([    "List_of_Bolivian_submissions_for_the_Academy_Award_for_Best_Foreign_Language_Film_0.json",
#     "Paul_Verhoeven_0.json",
#     "List_of_songs_recorded_by_Rufus_Wainwright_0.json",
#     "Basil_Wallace_0.json",
#     "List_of_songs_in_Guitar_Hero_II_1.json",
#     "List_of_Belgian_submissions_for_the_Academy_Award_for_Best_Foreign_Language_Film_0.json",
#     "List_of_sports_films_10.json",
#     "Debbie_Reynolds_0.json",
#     "List_of_longest_tunnels_in_the_world_1.json",
#     "List_of_World_War_II_science_fiction,_fantasy,_and_horror_films_2.json",
#     "List_of_whistleblowers_3.json",
#     "List_of_films_with_associated_hip_hop_songs_1.json",
#     "List_of_television_series_produced_by_Paramount_Television_6.json",
#     "Pamela_Chopra_0.json",
#     "List_of_highest-grossing_Bollywood_films_9.json",
#     "2010_in_American_television_7.json",
#     "List_of_Greek_submissions_for_the_Academy_Award_for_Best_Foreign_Language_Film_0.json",
#     "Anna_Paquin_0.json",
#     "National_Recording_Registry_4.json",
#     "World_Heritage_Sites_of_Poland_0.json",
#     "List_of_National_Trust_properties_in_Somerset_0.json",
#     "National_Recording_Registry_12.json",
#     "List_of_best-selling_singles_8.json",
#     "Felixstowe_Branch_Line_1.json",
#     "National_Recording_Registry_1.json",
#     "List_of_Luxembourgish_submissions_for_the_Academy_Award_for_Best_Foreign_Language_Film_0.json",
#     "Masoom_(1983_film)_0.json",
#     "List_of_Bulgarian_submissions_for_the_Academy_Award_for_Best_Foreign_Language_Film_0.json",
#     "List_of_fictional_princesses_6.json",
#     "Olu_Jacobs_2.json",
#     "National_Register_of_Historic_Places_listings_in_Faribault_County,_Minnesota_0.json",
#     "David_O._Selznick_filmography_2.json",
#     "List_of_Atari_arcade_games_19.json",
#     "List_of_best-selling_singles_5.json",
#     "List_of_film_spoofs_in_Mad_4.json",
#     "Dinky_Toys_0.json",
#     "List_of_places_of_worship_in_Arun_1.json",
#     "Paul_Bettany_1.json",
#     "Fatal_dog_attacks_in_the_United_States_6.json",
#     "Survivor_Series_(1995)_0.json",
#     "Major_crimes_in_the_United_Kingdom_13.json",
#     "National_Register_of_Historic_Places_listings_in_Calumet_County,_Wisconsin_0.json",
#     "List_of_highest-grossing_Indian_films_worldwide_4.json",
#     "List_of_places_of_worship_in_Worthing_1.json",
#     "Prime_Minister's_Literary_Awards_0.json",
#     "Editio_Regia_0.json",
#     "Politics_of_China_0.json",
#     "List_of_sports_films_44.json",
#     "The_World's_Billionaires_7.json",
#     "List_of_sports_films_49.json"
# ])
#
# ###adding gold
# nonzo_folder_path = 'gold_tables'
# nonzo_filename = "1995_Tooheys_1000_0"
# file_path = os.path.join(nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")
#
# ###adding generated
# gen_nonzo_folder_path = 'generated_tables'
# gen_nonzo_filename = "1995_Tooheys_1000_0"
# file_path = os.path.join(gen_nonzo_folder_path, nonzo_filename)
# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     all_data.append(f"{data}")
#
#
# ##adding top 50 BM25
# the_1000_path = "1000_random_tables"
# for filename in top_50:
#     file_path = os.path.join(the_1000_path, filename)
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
#         all_data.append(f"{data}")

##################################################
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

# fig = visualization.plot_embeddings_2d_with_distances(encoded_list, labels, highlight_index=0, hover_texts=all_data)
# fig.show()

# print(all_data)

tokenized_docs = [tokenize(doc) for doc in all_data]

# Build BM25 index
bm25 = BM25Okapi(tokenized_docs)

# Tokenize query (use actual query text instead of a document!)
query = all_data[0]
tokenized_query = tokenize(query)

# Score all documents
scores = bm25.get_scores(tokenized_query)

# Display results
scores_list = list(zip(all_data, scores))
for i, (doc, score) in enumerate(scores_list, start=1):
    if i == 1:
        print(f"query: {score:.4f}")
    elif i == 2:
        print(f"gold: {score:.4f}")
    elif i == 3:
        print(f"gen: {score:.4f}")
    else:
        print(f"{i}: {score:.4f}")