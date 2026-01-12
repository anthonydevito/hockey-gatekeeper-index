import numpy as np

def calculate_gap(df, entry_frame, attacking_zone):
    """Finds the distance to the closest defender at the moment of entry."""
    # 1. Get all players at that specific frame
    frame_data = df[df['frame_id'] == entry_frame].copy()
    
    puck_pos = frame_data[frame_data['jersey_number'] == 100]
    if puck_pos.empty: return None
    
    puck_x, puck_y = puck_pos.iloc[0]['x_ft'], puck_pos.iloc[0]['y_ft']
    
    # 2. Identify the defending team
    # If attacking right (x > 125), defenders are players with x > 125 (usually)
    # But a better way is to look at the team_name of the player closest to puck
    # For now, let's find the closest player who is NOT on the team that just entered
    
    # Let's find the puck carrier first (closest to puck)
    players = frame_data[frame_data['jersey_number'] != 100].copy()
    players['dist'] = np.sqrt((players['x_ft'] - puck_x)**2 + (players['y_ft'] - puck_y)**2)
    
    if players.empty: return None
    
    carrier = players.loc[players['dist'].idxmin()]
    attacking_team = carrier['team_name']
    
    # 3. Find the closest opponent (the Defender)
    defenders = players[players['team_name'] != attacking_team]
    if defenders.empty: return None
    
    closest_defender = defenders.loc[defenders['dist'].idxmin()]
    
    return {
        'defender_name': closest_defender['player'],
        'defender_jn': closest_defender['jersey_number'],
        'gap_distance': closest_defender['dist'],
        'attacking_team': attacking_team
    }