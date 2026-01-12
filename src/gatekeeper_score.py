import pandas as pd

def generate_index(results_df):
    """Aggregates entry data to rank defenders by their average gap control."""
    # Filter out entries where no defender was identified (NaNs)
    clean_df = results_df.dropna(subset=['defender_name'])
    
    # Group by defender and calculate metrics
    stats = clean_df.groupby('defender_name').agg(
        entries_faced=('frame_id', 'count'),
        avg_gap=('gap_distance', 'mean'),
        min_gap=('gap_distance', 'min')
    ).reset_index()
    
    # Sort by avg_gap (Lower is better for a defender!)
    stats = stats.sort_values('avg_gap', ascending=True)
    
    return stats