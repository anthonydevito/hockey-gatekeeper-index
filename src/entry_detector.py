import pandas as pd

def detect_zone_entries(df, cooldown_frames=60):
    """Detects frames where the puck crosses from Neutral to Offensive with a cooldown."""
    puck_df = df[df['jersey_number'] == 100].sort_values('frame_id').copy()
    
    entries = []
    puck_df['prev_x'] = puck_df['x_ft'].shift(1)
    
    last_entry_frame = -cooldown_frames
    
    for i, row in puck_df.iterrows():
        if pd.isnull(row['prev_x']): continue
        
        is_entry = False
        zone = None
        
        # ENTRY RIGHT: Crossing 125 from left-to-right
        if row['prev_x'] < 125 and row['x_ft'] >= 125:
            is_entry = True
            zone = 'right'
            
        # ENTRY LEFT: Crossing 75 from right-to-left
        elif row['prev_x'] > 75 and row['x_ft'] <= 75:
            is_entry = True
            zone = 'left'
            
        # Only record if we are outside the cooldown period
        if is_entry and (row['frame_id'] - last_entry_frame > cooldown_frames):
            entries.append({'frame_id': row['frame_id'], 'zone': zone, 'x': row['x_ft']})
            last_entry_frame = row['frame_id']
            
    return pd.DataFrame(entries)