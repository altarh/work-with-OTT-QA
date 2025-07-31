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

all_data = ["How many academic staff are at the university in Budapest that has the official abbreviation BME ?"]


top_50 = ([
    "Savilian_Professor_of_Astronomy_0.json",
"Awards,_lectures_and_medals_of_the_Royal_Society_0.json",
"List_of_University_of_Oregon_alumni_20.json",
"Editio_Regia_0.json",
"List_of_University_of_Oregon_alumni_5.json",
"Debbie_Reynolds_0.json",
"List_of_founding_Fellows,_Scholars_and_Commissioners_of_Jesus_College,_Oxford_1.json",
"List_of_University_of_Oregon_alumni_19.json",
"Turkish_minorities_in_the_former_Ottoman_Empire_0.json",
"Natural_Monuments_of_South_Korea_0.json",
"List_of_lacrosse_teams_in_Canada_15.json",
"List_of_University_of_Texas_at_Austin_alumni_16.json",
"List_of_longest_tunnels_in_the_world_1.json",
"List_of_Washington_&_Jefferson_College_alumni_13.json",
"2010_in_American_television_7.json",
"List_of_Brigham_Young_University_alumni_0.json",
"List_of_universities_and_colleges_in_Thailand_0.json",
"Neighborhoods_in_Detroit_0.json",
"Offshoring_Research_Network_0.json",
"Boca_Juniors_1.json",
"Case_citation_8.json",
"McDonald's_All-American_Game_3.json",
"List_of_Christmas_carols_0.json",
"Solar_power_in_Germany_2.json",
"International_Six_Days_Enduro_0.json",
"List_of_Nobel_laureates_affiliated_with_the_University_of_Pennsylvania_0.json",
"National_Recording_Registry_1.json",
"Olu_Jacobs_2.json",
"West_Bromwich_Albion_F.C._0.json",
"List_of_closed_railway_lines_in_Great_Britain_0.json",
"National_Recording_Registry_12.json",
"1500_metres_1.json",
"List_of_whistleblowers_3.json",
"ECAC_Division_II_Lacrosse_League_0.json",
"Blaenplwyf_transmitting_station_7.json",
"England_at_the_2010_Commonwealth_Games_(medalists)_1.json",
"Deities_of_Slavic_religion_5.json",
"2013_Canadian_Soccer_League_season_1.json",
"WWE_Diva_Search_5.json",
"WWE_Diva_Search_4.json",
"List_of_places_of_worship_in_Eastbourne_1.json",
"World_Heritage_Sites_of_Poland_0.json",
"States_and_territories_of_Australia_4.json",
"List_of_Baltimore_Orioles_(19th_century)_Opening_Day_starting_pitchers_0.json",
"List_of_BBC_properties_1.json",
"UAE_Arabian_Gulf_League_2.json",
"Felixstowe_Branch_Line_1.json",
"List_of_colleges_and_universities_in_Oregon_0.json",
"Venues_of_the_1992_Winter_Olympics_0.json",
"List_of_TV_Guide_covers_(2010s)_5.json"
])
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
nonzo_filename = "Budapest_0"
file_path = os.path.join(nonzo_folder_path, nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")

###adding generated
gen_nonzo_folder_path = 'generated_tables'
gen_nonzo_filename = "Budapest_0.json"
file_path = os.path.join(gen_nonzo_folder_path, gen_nonzo_filename)
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    all_data.append(f"{data}")


##adding top 50 BM25
the_1000_path = '1000_random_tables'
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
