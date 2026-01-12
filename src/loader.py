import pandas as pd
import os

def load_enriched_data(tracking_path, roster_path):
    """Loads tracking data and merges with roster for player names."""
    df = pd.read_csv(tracking_path)
    roster = pd.read_csv(roster_path)
    
    # Simple team mapping
    team_map = {'USA': 'home', 'Canada': 'away', 'Finland': 'home', 'ROC': 'away', 'Switzerland': 'away'}
    df['roster_team_label'] = df['team_name'].map(team_map)
    
    # Merge
    enriched = df.merge(
        roster, 
        left_on=['jersey_number', 'roster_team_label'], 
        right_on=['jn', 'team'], 
        how='left'
    )
    
    # Handle the puck (Jersey 100)
    enriched.loc[enriched['jersey_number'] == 100, 'player'] = 'PUCK'
    
    return enriched