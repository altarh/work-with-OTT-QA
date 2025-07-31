import os

# List of file paths with issues
invalid_files = [
    "2000_random_tables/List_of_The_Avengers:_Earth's_Mightiest_Heroes_characters_2.json",
    "2000_random_tables/List_of_closed_railway_stations_in_Ireland:_C_0.json",
    "2000_random_tables/Looney_Tunes_Golden_Collection:_Volume_1_2.json",
    "2000_random_tables/Looney_Tunes_Golden_Collection:_Volume_3_1.json",
    "2000_random_tables/Looney_Tunes_Golden_Collection:_Volume_6_0.json",
    "2000_random_tables/Magic:_The_Gathering_Hall_of_Fame_0.json",
    "2000_random_tables/Michael_\"Ffish\"_Hemschoot_0.json",
    "2000_random_tables/The_Real_World:_Los_Angeles_0.json",
    "2000_random_tables/The_Real_World:_New_Orleans_(2010)_0.json",
    "2000_random_tables/The_Real_World:_San_Diego_0.json",
    "2000_random_tables/The_Real_World:_Sydney_0.json"
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
