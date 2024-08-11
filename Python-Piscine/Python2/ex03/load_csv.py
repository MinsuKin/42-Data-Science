import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Takes a path to a csv file and returns a pandas DataFrame."""
    data = pd.read_csv(path)
    return data
