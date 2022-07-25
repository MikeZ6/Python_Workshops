"""
Author: Mike Zhang

View csv data and apply simple wrangling techniques
"""

import pandas as pd

#Overview of data
df = pd.read_csv("OnlineRetail.csv", index_col = 0)
print(df.shape)
print(df.info())
print(df.describe())

#%%
#Data wrangling of stockcode and description columns
data = df[["StockCode","Description"]]
print(data.shape)
data = data.sort_values(["StockCode"])
print(data)

data = data.drop_duplicates(keep='first', subset ='StockCode')
data.to_csv("Stocks.csv", index = False)
print(data.shape)
print(data)


#%%
#Sorting based on InvoinceNo
df=pd.read_csv("OnlineRetail.csv")
df.info()
data = df[["InvoiceNo","InvoiceDate","CustomerID"]]
print(data.shape)
data = data.sort_values(["InvoiceNo"])
print(data)


#%%
#Sorting based on CustomerID
df=pd.read_csv("OnlineRetail.csv")
df.info()
data = df[["CustomerID","Country"]]
print(data.shape)
data = data.sort_values(["CustomerID"])
print(data)

