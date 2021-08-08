# %%
# Download data
import requests

download_file = requests.get("https://my.data.warehouse/data.csv")

# Save data to file
with open("data.csv", "w+") as writer:
    writer.write(download_file.content.decode("utf-8"))

# %%
# Clean data
import pandas as pd

df = pd.read_csv("data.csv")
df = df.fillna(0)

# Split X and Y
x_train = df[[col for col in df.columns if col != "target"]].values.astype("float32")
y_train = df["target"].values.astype("float32")
