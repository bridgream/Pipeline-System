import pandas as pd

from common import PathLike


def clean_data(
        input_path: PathLike,
        output_path: PathLike
):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df.to_csv(output_path)


clean_data(
    input_path="data.csv",
    output_path="clean_data.csv"
)
