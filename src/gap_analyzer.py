import numpy as np

def calculate_gap(df, entry_frame, attacking_zone):
    """
    Calculates the Euclidean distance to the nearest opponent at the time of zone entry.
    Used to quantify defensive pressure and gap control at the blue line.
    """
    # Filter data for the specific frame of entry
    frame_data = df[df['frame_id'] == entry_frame].copy()
    
    # Locate puck coordinates
    puck_pos = frame_data[frame_data['jersey_number'] == 100]
    if puck_pos.empty: 
        return None
    
    puck_x, puck_y = puck_pos.iloc[0]['x_ft'], puck_pos.iloc[0]['y_ft']
    
    # Calculate player distances to the puck
    players = frame_data[frame_data['jersey_number'] != 100].copy()
    players['dist'] = np.sqrt((players['x_ft'] - puck_x)**2 + (players['y_ft'] - puck_y)**2)
    
    if players.empty: 
        return None
    
    # Identify the puck carrier and attacking team
    carrier = players.loc[players['dist'].idxmin()]
    attacking_team = carrier['team_name']
    
    # Identify the closest opponent (the primary defender)
    defenders = players[players['team_name'] != attacking_team]
    if defenders.empty: 
        return None
    
    closest_defender = defenders.loc[defenders['dist'].idxmin()]
    
    return {
        'defender_name': closest_defender['player'],
        'defender_jn': closest_defender['jersey_number'],
        'gap_distance': closest_defender['dist'],
        'attacking_team': attacking_team
    }