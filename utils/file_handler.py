import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def save_csv(data, file_path):

    data.to_csv(file_path, index=False) 