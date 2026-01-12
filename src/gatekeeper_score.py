import pandas as pd

def generate_index(results_df):
    """
    Aggregates transition data to rank defenders based on spatial suppression metrics.
    Produces a leaderboard where a lower average gap indicates superior gap control.
    """
    # Remove observations where defender identification was unsuccessful
    clean_df = results_df.dropna(subset=['defender_name'])
    
    # Calculate aggregate performance metrics per player
    stats = clean_df.groupby('defender_name').agg(
        entries_faced=('frame_id', 'count'),
        avg_gap=('gap_distance', 'mean'),
        min_gap=('gap_distance', 'min')
    ).reset_index()
    
    # Sort by average gap; lower values represent tighter defensive coverage
    stats = stats.sort_values('avg_gap', ascending=True)
    
    return stats