#%%
import requests
download_file = requests.get("https://my.data.warehouse.com/data_1.csv")

with open("data_1.csv", "wb") as writer:
    writer.write(download_file.content)

#%%
import pandas as pd
df = pd.read_csv("data_1.csv")
df = df.fillna(0)

x_train = df[[col for col in df.columns if col != "target"]].values.astype("float32")
y_train = df["target"].values.astype("float32")
