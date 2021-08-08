import tempfile

import pandas as pd

from better_dropna import clean_data

with tempfile.NamedTemporaryFile() as file:
    input_path = "data.csv"
    output_path = file.name
    clean_data(input_path, output_path)

    cleaned: pd.DataFrame = pd.read_csv(output_path)
    assert cleaned.ndim == 2
    assert cleaned.isna().sum().sum() == 0
