import os
import pandas as pd
from src.loader import load_enriched_data
from src.entry_detector import detect_zone_entries
from src.gap_analyzer import calculate_gap
from src.gatekeeper_score import generate_index

def test_pipeline():
    # 1. Configuration - Using the first Canada vs USA power play
    game_dir = "data/tracking/2022-02-08 Canada at USA"
    tracking_file = os.path.join(game_dir, "2022-02-08 Canada at USA P1 PP2.csv")
    roster_file = os.path.join(game_dir, "2022-02-08 Canada at USA roster.csv")

    print(f"--- INITIALIZING GATEKEEPER PIPELINE ---")
    
    # 2. Load Data
    if not os.path.exists(tracking_file):
        print(f"Error: Could not find {tracking_file}")
        return

    df = load_enriched_data(tracking_file, roster_file)
    puck_only = df[df['jersey_number'] == 100]
    print(f"Puck X Range: Min={puck_only['x_ft'].min()}, Max={puck_only['x_ft'].max()}")
    print(f"Successfully loaded {len(df)} tracking rows.")

    # 3. Detect Entries
    entry_df = detect_zone_entries(df)
    
    print(f"\n[TRANSITION ANALYSIS]")
    print(f"Total Blue Line Crossings Detected: {len(entry_df)}")
    
    if not entry_df.empty:
        results = []
        for _, entry in entry_df.iterrows():
            gap_info = calculate_gap(df, entry['frame_id'], entry['zone'])
            if gap_info:
                results.append({**entry, **gap_info})
        
        results_df = pd.DataFrame(results)
        print("\n[GAP ANALYSIS RESULTS]")
        print(results_df[['frame_id', 'zone', 'defender_name', 'gap_distance']])

        print("\n[GATEKEEPER INDEX - LEADERBOARD]")
        leaderboard = generate_index(results_df)
        print(leaderboard)

    print(f"\n--- TEST COMPLETE ---")

if __name__ == "__main__":
    test_pipeline()