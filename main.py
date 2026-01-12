import os
import pandas as pd
from src.loader import load_enriched_data
from src.entry_detector import detect_zone_entries
from src.gap_analyzer import calculate_gap
from src.gatekeeper_score import generate_index

def run_gatekeeper_pipeline():
    """
    Main execution script for the Gatekeeper Index. 
    Orchestrates data loading, transition detection, spatial analysis, and leaderboard generation.
    """
    # Configuration: Define paths for tracking and roster data
    game_dir = "data/tracking/2022-02-08 Canada at USA"
    tracking_file = os.path.join(game_dir, "2022-02-08 Canada at USA P1 PP2.csv")
    roster_file = os.path.join(game_dir, "2022-02-08 Canada at USA roster.csv")

    print(f"--- INITIALIZING GATEKEEPER PIPELINE ---")
    
    # 1. Data Ingestion
    if not os.path.exists(tracking_file):
        print(f"Error: Missing data file at {tracking_file}")
        return

    df = load_enriched_data(tracking_file, roster_file)
    print(f"Loaded {len(df)} tracking rows.")

    # 2. Transition Detection
    entry_df = detect_zone_entries(df)
    print(f"\n[TRANSITION ANALYSIS]")
    print(f"Blue Line Crossings Detected: {len(entry_df)}")
    
    # 3. Spatial Gap Analysis
    if not entry_df.empty:
        results = []
        for _, entry in entry_df.iterrows():
            gap_info = calculate_gap(df, entry['frame_id'], entry['zone'])
            if gap_info:
                # Merge transition event data with spatial gap metrics
                results.append({**entry, **gap_info})
        
        results_df = pd.DataFrame(results)
        
        # Display granular entry results
        print("\n[ENTRY LOG - SAMPLE]")
        print(results_df[['frame_id', 'zone', 'defender_name', 'gap_distance']].head())

        # 4. Aggregation and Ranking
        print("\n[GATEKEEPER INDEX - LEADERBOARD]")
        leaderboard = generate_index(results_df)
        print(leaderboard)

    print(f"\n--- EXECUTION COMPLETE ---")

if __name__ == "__main__":
    run_gatekeeper_pipeline()