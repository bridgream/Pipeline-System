import os
import typing

import requests

PathLike = typing.Union[str, bytes, os.PathLike]


def download_text(
        uri: str,
        save_to: PathLike
):
    download_file = requests.get(uri)

    with open(save_to, "w+") as writer:
        writer.write(download_file.content.decode("utf-8"))


download_text(
    uri="https://my.data.warehouse/data.csv",
    save_to="data.csv"
)
