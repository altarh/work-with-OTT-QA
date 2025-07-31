import os

# List of file paths with issues
invalid_files = [
    "2000_random_tables/\"Weird_Al\"_Yankovic_2.json",
    "2000_random_tables/Ben_Rubin_(Magic:_The_Gathering_player)_0.json",
    "2000_random_tables/Bugs_&_Daffy:_The_Wartime_Cartoons_0.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_11.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_14.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_17.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_18.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_4.json",
    "2000_random_tables/Ebertfest:_Roger_Ebert's_Film_Festival_9.json",
    "2000_random_tables/List_of_Important_Cultural_Properties_of_Japan_(Heian_period:_structures)_1.json"
]

# Delete each file if it exists
for file_path in invalid_files:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
