import pandas as pd
import numpy as np
import matplotlib.pyplot as py

df = pd.read_csv("D:\Private\DEQ3\Project\SQL-data-challenges-master-Shared\orders.csv")

for col in df['invoice_id', 'product_id', 'customer_id', 'country_id']:
    df[col] = df[col].astype(str)

print(df.info())