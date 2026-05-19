import json
from pathlib import Path

# Path to JSON file
DATA_FILE = Path("data/players.json")

# Structure for when no exists
DEFAULT_DATA = {
    "players": {}
}

def load_data():
    """
    1. Read players.json
    2. If missing or corrupted
    3. Return default data
    """
    if not DATA_FILE.exists():
        return DEFAULT_DATA
    
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)

    except json.JSONDecodeError:
        return DEFAULT_DATA
    
def save_data(data):
    """
    Write data to file
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def create_player(name):
    """
    1. Validation
    2. Create new player
    3. Set default stats
    4. Save to file
    """
    name = name.strip().upper()

    if not name:
        raise ValueError("Name cannot be empty")
    if len(name) > 4:
        raise ValueError("Max 4 characters")
    if not name.isalnum():
        raise ValueError("Letters only & numbers only")

    current_data = load_data()
    new_player = {
        "best_attempts": 0,
        "best_time": 0,
        "games_played": 0,
        "total_guesses": 0,
        "is_test": False    
    }
    current_data["players"][name] = new_player
    save_data(current_data)
    return new_player

def get_player(name):
    """
    1. Fetch data
    2. Look into data
    3. Search with Format
    4. Retrieve result 
    """
    current_data = load_data()
    for player_key in current_data["players"]:
        if player_key.upper() == name.upper():
            return current_data["players"][player_key].copy()
                
    return None

def update_stats(name, attempts, time_elapsed):
    """
    1. Load data
    2. Verify player data
    3. Load data if empty
    """
    current_data = load_data()
    
    found_name = None
    for player_key in current_data["players"]:
        if player_key.upper() == name.upper():
            found_name = player_key
            break
    
    if found_name is None:
        raise KeyError(f"Player {name} not found")
    
    player = current_data["players"][found_name]

    player["games_played"] += 1
    player["total_guesses"] += attempts

    if player["best_attempts"] == 0 or attempts < player["best_attempts"]:
        player["best_attempts"] = attempts
        
    if player["best_time"] == 0 or time_elapsed < player["best_time"]:
        player["best_time"] = time_elapsed

    save_data(current_data)
    
def get_leaderboard(category, limit=5):
    """
    1. Defining Map
    2. Get key    
    3. Load Data
    4. Create leaderboard list
    5. Filter data and add to list
    6. Define sorting behaviour
    7. Sort list
    """
    stat_map = {
        "speed": "best_time",
        "logic": "best_attempts",
        "junkie": "games_played"
    }

    target_key = stat_map[category]
    
    current_data = load_data()

    leaderboard_list = []

    for name, stats in current_data["players"].items():
        if stats["is_test"] == False:
            player_score = stats[target_key]
            player_tuple = (name, player_score)
            leaderboard_list.append(player_tuple)

    if category == "junkie":
        sort_highest_first = True
    else:
        sort_highest_first = False

    final_sorted_list = sorted(leaderboard_list, key=lambda x: x[1], reverse=sort_highest_first)
    return final_sorted_list[:limit]
