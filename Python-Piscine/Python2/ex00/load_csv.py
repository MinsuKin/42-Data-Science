import pandas as pd


def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    print(f"Loading dataset of dimensions ({data.shape[0]}, {data.shape[1]})")
    return data


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
