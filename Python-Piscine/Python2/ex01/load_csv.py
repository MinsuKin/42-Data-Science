import pandas as pd


def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data
