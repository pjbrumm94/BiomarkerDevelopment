import numpy as np

def extract_features(df):
    """Extracts digital biomarkers from raw data."""
    df['mean_activity'] = df[['sensor_1', 'sensor_2']].mean(axis=1)
    df['std_activity'] = df[['sensor_1', 'sensor_2']].std(axis=1)
    df['movement_variability'] = df['sensor_1'].diff().abs().mean()
    
    return df
