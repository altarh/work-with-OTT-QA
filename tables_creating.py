import os

import requests

table_ids_gold = [
    "Nonso_Anozie_1",
    "Sevens_Grand_prix_series_0",
    "Kishore_Kumar_1",
    "Bradford_City_A.F.C._0",
    "Budapest_0",
    "1995_Tooheys_1000_0",
    "2015–16_Arsenal_F.C._season_2",
    "List_of_New_York_University_alumni_22",
    "2009–10_Vancouver_Canucks_season_14",
    "Dancing_with_the_Stars_(U.S._season_5)_0",
    "George_Augustus_Vaughn,_Jr._0",
    "List_of_football_clubs_in_Argentina_2",
    "2018_Emerging_Nations_World_Championship_0",
    "2014–15_Fenerbahçe_S.K._season_7",
    "List_of_YouTube_personalities_0",
    "Trevor_Eyster_0",
    "2015_Kangaroo_Cup_0",
    "2019_Campeonato_Mineiro_0",
    "List_of_ViacomCBS_television_programs_28"
]
table_ids_not_gold = [
    "10,000_metres_0",
    "10,000_metres_1",
    "100_metres_hurdles_0",
    "100th_Wisconsin_Legislature_0",
    "102nd_United_States_Congress_1",
    "105th_United_States_Congress_0",
    "107th_United_States_Congress_1",
    "10th_Legislative_Assembly_of_Manitoba_0",
    "10th_United_States_Congress_0",
    "10th_United_States_Congress_1",
    "110_metres_hurdles_0",
    "111th_United_States_Congress_0",
    "113th_United_States_Congress_1",
    "11th_United_States_Congress_0",
    "11th_United_States_Congress_1",
    "123rd_Ohio_General_Assembly_0",
    "127th_Ohio_General_Assembly_0",
    "127th_Ohio_General_Assembly_1",
    "128th_Ohio_General_Assembly_0",
    "128th_Ohio_General_Assembly_1",
    "129th_Ohio_General_Assembly_0",
    "129th_Ohio_General_Assembly_1",
    "129th_Ohio_General_Assembly_2",
    "129th_Ohio_General_Assembly_3",
    "130th_Ohio_General_Assembly_1",
    "13th_Legislative_Assembly_of_Manitoba_0",
    "13th_United_States_Congress_1",
    "14th_Legislative_Assembly_of_British_Columbia_0",
    "1500_metres_0",
    "1500_metres_1",
    "1500_metres_world_record_progression_0",
    "1500_metres_world_record_progression_1",
    "1500_metres_world_record_progression_2",
    "1500_metres_world_record_progression_3",
    "15th_Legislative_Assembly_of_Puerto_Rico_0",
    "1790_United_States_Census_1",
    "17th_Legislative_Assembly_of_Manitoba_0",
    "17th_Legislative_Assembly_of_Puerto_Rico_0",
    "17th_Legislative_Assembly_of_Puerto_Rico_1",
    "1884_New_Zealand_rugby_union_tour_of_New_South_Wales_0",
    "1884_New_Zealand_rugby_union_tour_of_New_South_Wales_1",
    "1893_New_Zealand_rugby_union_tour_of_Australia_0",
    "18th_United_States_Congress_0",
    "18th_United_States_Congress_1",
    "1903_New_Zealand_rugby_union_tour_of_Australia_0",
    "1903_New_Zealand_rugby_union_tour_of_Australia_1",
    "1910_New_Zealand_rugby_union_tour_of_Australia_0",
    "1911_Notre_Dame_Fighting_Irish_football_team_0"
]
questions = [
    "Who created the series in which the character of Robert , played by actor Nonso Anozie , appeared ?",
    "What did the 2nd championship win at the Sevens Grand Prix Series for the team with the most top 4 finishes qualify them for ?",
    "This 70 's Kishore Kumar song was in a film produced by Alankar Chitra and directed by Shanker Mukherjee ?",
    "What is the full birth name of the Bradford A.F.C player that only played for the team in 2011 ?",
    "How many academic staff are at the university in Budapest that has the official abbreviation BME ?",
    "The 1995 Tooheys 1000 driver who was second-to-last in the Tooheys Top 10 was born where ?",
    "What is the capacity of the home grounds of the club a player transfered from Arsenal FC to FC Dordecht ?",
    "What is the full name of the person who is a NYU prize winner alumnus associated with ARTS ?",
    "What position does 2009–10 season Vancouver Canucks player Rob Davison currently hold with the Toronto Marlies ?",
    "What is the best known song sung by the couple celebrity paired with Jonathan Roberts during the season 5 of Dancing with the Stars in america ?",
    "What department is the location in where the opponent of George Augustus Vaughn Jr. was a double seater reconnaissance biplane in WW 1 ?",
    "The Argentinian Primera B Metropolitana club in the city that won the 1969 Metropolitano plays in what division ?",
    "Which nation participating in the 2018 Emerging Nations World Championship had the lowest RLIF rank number ?",
    "What is Spain 's oldest sporting club solely devoted to football with a 2014–15 Fenerbahçe S.K . season result F-A of 0-2 ?",
    "How many millions have a subscription to the primary channel of the YouTube personality person with the Youtube username MoreAliA ?",
    "Which television show starring Trevor Eyster was based on a 1986 book by Steve Slavkin and Thomas Hill ?",
    "How many residents does the capital city of the country represented by the 2015 Kangaroo Cup single 's player to finally retire in Sept 2017 have ?",
    "What town was the manager born in whose 2019 Campeonato Mineiro club is nicknamed Raposa ?",
    "By what nickname is the network that broadcast the ViacomCBS television program , Canon , sometimes known ?"
]

# download_folder = r'C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\random tables'
# files = ['10,000_metres_0', '10,000_metres_1']
my_url = 'https://raw.githubusercontent.com/wenhuchen/OTT-QA/master/data/traindev_tables_tok/'


import json

# Load the file
with open(r"C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\question_table_map.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(type(data))

# Extract all "question" values
questions = list(data.values())
# Print first few questions
# for q in questions[:5]:
#     print(q)


download_folder = r'C:\Users\Altar\uni_assingments\Embeddings Demo Project\work-with-OTT-QA\all_gold_tables'
def download_all_json_files(base_url, files, download_folder):
    for file in files:
        url = base_url + file +".json"
        response = requests.get(url)
        if response.status_code == 200:
            filepath = os.path.join(download_folder, file)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {file}")
        else:
            print(f"Failed to download {file}")


download_all_json_files(my_url, questions, download_folder)
