import pandas as pd
import os

def load_enriched_data(tracking_path, roster_path):
    """
    Ingests raw tracking CSVs and joins them with roster data to provide player names.
    """
    df = pd.read_csv(tracking_path)
    roster = pd.read_csv(roster_path)
    
    # Map team names to home/away labels for roster alignment
    team_map = {
        'USA': 'home', 'Canada': 'away', 
        'Finland': 'home', 'ROC': 'away', 
        'Switzerland': 'away'
    }
    df['roster_team_label'] = df['team_name'].map(team_map)
    
    # Merge datasets on jersey number and team label
    enriched = df.merge(
        roster, 
        left_on=['jersey_number', 'roster_team_label'], 
        right_on=['jn', 'team'], 
        how='left'
    )
    
    # Assign identifiable label to the puck object
    enriched.loc[enriched['jersey_number'] == 100, 'player'] = 'PUCK'
    
    return enriched