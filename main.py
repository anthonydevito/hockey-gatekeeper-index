import os
import pandas as pd
from src.loader import load_enriched_data
from src.entry_detector import detect_zone_entries
from src.gap_analyzer import calculate_gap
from src.gatekeeper_score import generate_index

def run_gatekeeper_pipeline():
    """
    Main orchestrator for the Gatekeeper Index.
    Processes tracking segments in batch to quantify defensive gap control at the blue line.
    """
    # Define directory for game segments and roster metadata
    game_dir = "data/tracking/2022-02-08 Canada at USA"
    roster_file = os.path.join(game_dir, "2022-02-08 Canada at USA roster.csv")

    if not os.path.exists(roster_file):
        print(f"Error: Required roster file not found at {roster_file}")
        return

    print(f"--- INITIALIZING BATCH GATEKEEPER PIPELINE ---")
    
    all_results = []

    # Iterate through tracking files to build a comprehensive game dataset
    for filename in os.listdir(game_dir):
        # Identify tracking CSVs while excluding roster or metadata files
        if filename.endswith(".csv") and "roster" not in filename:
            tracking_path = os.path.join(game_dir, filename)
            print(f"Processing Segment: {filename}...")
            
            try:
                # 1. Load data and synchronize with roster
                df = load_enriched_data(tracking_path, roster_file)
                
                # 2. Extract zone entry events
                entry_df = detect_zone_entries(df)
                
                # 3. Calculate spatial metrics (Gap Distance) for each entry
                for _, entry in entry_df.iterrows():
                    gap_info = calculate_gap(df, entry['frame_id'], entry['zone'])
                    if gap_info:
                        all_results.append({**entry, **gap_info})
                        
            except Exception as e:
                # Log non-tracking files or corrupted segments without breaking the loop
                print(f"Bypassing {filename}: {e}")

    # Finalize results and generate leaderboard
    if all_results:
        results_df = pd.DataFrame(all_results)
        
        print("\n[GLOBAL ENTRY ANALYSIS]")
        print(f"Total Entries Analyzed: {len(results_df)}")

        print("\n[GATEKEEPER INDEX - LEADERBOARD]")
        leaderboard = generate_index(results_df)
        print(leaderboard)
    else:
        print("Pipeline execution resulted in zero detected entries.")

    print(f"\n--- BATCH EXECUTION COMPLETE ---")

if __name__ == "__main__":
    run_gatekeeper_pipeline()