"""
Author: Mike Zhang

Workshop on using dataframe in pandas
"""

"create a dataframe df1 from single list salesList [1254,2654,2514,1425] to represent sales of first quarter in current year"
import pandas as pd
sales = [1254,2654,2514,1425]
s = pd.DataFrame(sales)

#%%
"inspect sales index 2 by using loc"
print(s.loc[2])

#%%
"insert a index column for df1"
index = ["Jan", "Feb", "Mar", "Apr"]
s = pd.DataFrame(sales, index)

#%%
"get the sales from 'Feb' using loc"
mth = 'Feb'
print(f'sales for {mth} is {s.loc[mth][0]}')

#%%
"change the column name to 'sales'"
s = pd.DataFrame(sales, index, columns = ["Sales"])
print(s)

#%%
"add in a new column to df1 with number of transactions [30,52,50,28]"
nos = [30,52,50,28]
s['nos']=nos
print(s)

#%%
"derive a new column 'avg' that represent the average sales per transaction" 
avg = [a/b for a,b in zip(sales, nos)]
s['avg']=avg
print(s)

#%%
"extract any month's sales with average more than 50"
print(s.loc[s.avg > 50])

#%%
"reassign the dataframe index and columns to mList(month), sList(sales), nList(nos) and aList(avg) "
mList=list(s.index)
sList = list(s["sales"])
nList = list(s["nos"])
aList = list(s["avg"])

print(mList)
print(sList)
print(nList)
print(aList)

#%%
"rearange back to dataframe"
df = pd.DataFrame({"mth":mList, "sales":sList, "nos":nList, "avg":aList})
print(df)

