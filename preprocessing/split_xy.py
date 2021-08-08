import pandas as pd

from preprocessing.common import PathLike


def split_xy(
        input_path: PathLike,
        output_x_path: PathLike,
        output_y_path: PathLike,
        y_column_name: str,
        dtype: str = None,

):
    df = pd.read_csv(input_path)
    x_train = df.drop(y_column_name, axis=1)
    y_train = df[y_column_name]

    if dtype is not None:
        x_train = x_train.astype(dtype)
        y_train = y_train.astype(dtype)

    x_train.to_csv(output_x_path)
    y_train.to_csv(output_y_path)
