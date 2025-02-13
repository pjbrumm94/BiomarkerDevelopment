import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Loads dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Cleans dataset by handling missing values and duplicates."""
    df = df.drop_duplicates()
    df = df.fillna(df.median())  # Filling missing values with median
    return df

def scale_features(df, columns):
    """Scales selected features using StandardScaler."""
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def preprocess(file_path, feature_columns):
    """Complete preprocessing pipeline."""
    df = load_data(file_path)
    df = clean_data(df)
    df = scale_features(df, feature_columns)
    return df
