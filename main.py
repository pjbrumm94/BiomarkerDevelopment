import preprocessing
import feature_engineering
import model

DATA_PATH = "data/digital_biomarkers.csv"  # Adjust path as needed
FEATURE_COLUMNS = ['sensor_1', 'sensor_2']  # Update based on dataset
TARGET_COLUMN = 'diagnosis'  # Update with the actual column name

def main():
    print("Loading and Preprocessing Data...")
    df = preprocessing.preprocess(DATA_PATH, FEATURE_COLUMNS)

    print("Extracting Features...")
    df = feature_engineering.extract_features(df)

    print("Training Model...")
    trained_model = model.train_model(df, TARGET_COLUMN)

if __name__ == "__main__":
    main()
