import pandas as pd

pd_file = pd.read_csv("Data_09-11-22.csv")


df = pd.DataFrame(pd_file)

print(df.tail())
