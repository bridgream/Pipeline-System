import pandas as pd


def clean_data(
        file_path: str
) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df = df.dropna()
    return df


cleaned_data = clean_data("data.csv")
