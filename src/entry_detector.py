import pandas as pd

def detect_zone_entries(df, cooldown_frames=60):
    """
    Identifies frames where the puck crosses the blue line into the offensive zone.
    Includes a cooldown period to prevent duplicate triggers from 'line-dangling.'
    """
    # Isolate puck data and calculate movement vector
    puck_df = df[df['jersey_number'] == 100].sort_values('frame_id').copy()
    puck_df['prev_x'] = puck_df['x_ft'].shift(1)
    
    entries = []
    last_entry_frame = -cooldown_frames
    
    for i, row in puck_df.iterrows():
        if pd.isnull(row['prev_x']): 
            continue
        
        is_entry = False
        zone = None
        
        # Check for right-side entry (Puck crosses x=125)
        if row['prev_x'] < 125 and row['x_ft'] >= 125:
            is_entry = True
            zone = 'right'
            
        # Check for left-side entry (Puck crosses x=75)
        elif row['prev_x'] > 75 and row['x_ft'] <= 75:
            is_entry = True
            zone = 'left'
            
        # Log entry only if outside the defined cooldown window
        if is_entry and (row['frame_id'] - last_entry_frame > cooldown_frames):
            entries.append({
                'frame_id': row['frame_id'], 
                'zone': zone, 
                'x': row['x_ft']
            })
            last_entry_frame = row['frame_id']
            
    return pd.DataFrame(entries)