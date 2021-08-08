from better_dropna import clean_data
from download import download_text
from split_xy import split_xy

download_text(
    uri="https://my.data.warehouse/data.csv",
    save_to="data.csv"
)

clean_data(
    input_path="data.csv",
    output_path="clean_data.csv"
)

split_xy(
    input_path="clean_data.csv",
    output_x_path="x_train.csv",
    output_y_path="y_train.csv",
    y_column_name="target",
    dtype="float32"
)
