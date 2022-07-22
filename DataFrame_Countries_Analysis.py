"""
Author: Mike Zhang

Using dataframe in pandas on data entry of countries
"""

#%%
"""
Create a new Dataframe 
Expected output:
        country    capital    area  population
0        Brazil   Brasilia   8.516      200.40
1        Russia     Moscow  17.100      143.50
2         India  New Dehli   3.286     1252.00
3         China    Beijing   9.597     1357.00
4  South Africa   Pretoria   1.221       52.98
"""

import pandas as pd
import numpy as np

popInfo = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

df = pd.DataFrame(popInfo)

#%%
"insert a new row to the dataframe with index 4, that contains 'Singapore' as both Country and capital, but nil value for the rest of the information"

new_row = {"country":"Singapore", "capital":"Singapore", "area":np.NaN, "population":np.NaN}
df = df.append(new_row, ignore_index=True)
print(df)

#%%
"check for the numeber of nil records in the dataframe"

print(df.isnull())
print(df.isnull().sum())

#%%
"update Singapore population as 5.704 and area 0.0007283"

df.loc[df["country"]=="Singapore","area"] = 0.0007283
df.loc[df["country"]=="Singapore","population"] = 5.704
print(df.isnull().sum())
print(df)

#%%
"duplicate row with index 1 for rows with index 6,7,8,9,10"
'''
expected output:
         country    capital       area  population
0         Brazil   Brasilia   8.516000    200.4000
1         Russia     Moscow  17.100000    143.5000
2          India  New Dehli   3.286000   1252.0000
3          China    Beijing   9.597000   1357.0000
4   South Africa   Pretoria   1.221000     52.9800
5      Singapore  Sinagpore   0.000728      0.5704
6         Russia     Moscow  17.100000    143.5000
7         Russia     Moscow  17.100000    143.5000
8         Russia     Moscow  17.100000    143.5000
9         Russia     Moscow  17.100000    143.5000
10        Russia     Moscow  17.100000    143.5000
'''

russia_row = {"country":"Russia", "capital":"Moscow", "area":17.1, "population":143.5}
for counter in range(5):
    df = df.append(russia_row, ignore_index=True)

print(df)

#%%
"update population at row 7 as 18, 8 as 19, 9 as 20, 10 as 19"

for counter in range(7,10):
    df.loc[counter,"population"] = counter+11

df.loc[10,"population"] = 19

print(df)

#%%
"use DataFrame.drop_duplicates to remove duplicates based on country, using 'first' for keep parameter, removal does not alter the original dataframe"
print(df.drop_duplicates(subset = "country", keep="first", inplace = False))

"use DataFrame.drop_duplicates to remove duplicates based on country, using False for keep parameter, removal does not alter the original dataframe"
print(df.drop_duplicates(subset='country',keep=False, inplace = False))

"use DataFrame.drop_duplicates to remove duplicates based on country, using 'last' for keep  parameter removal does not alter the original dataframe"
print(df.drop_duplicates(subset="country", keep="first", inplace = False))

#%%
"sort the dataframe permenantly in the order of country, population, then area"
df.sort_values(["country", "population", "area"], inplace = True)
print(df)

#%%
"sort the dataframe permenantly in the order of area in descending order then country, population (both ascending)"
df.sort_values(["area","country","population"], ascending=[False, True, True], inplace = True)
print(df)

#%%
"Find the average area, including duplicates"
print('average area, including duplicates:', df["area"].mean())

#%%
"Find the averages for Russia only"
print(df[df["country"]=="Russia"].mean())

#%%
"Find which country has the max and min population"
print(df.loc[df.population == df.population.max(), ["country", "population"]])
print(df.loc[df.population == df.population.min(), ["country", "population"]])

#%%
"Task 19 :Find the records whose capital is Beijing"
print(df.loc[df.capital == "Beijing"])

#%%
"Find the records whose capital begins with 'B'"
for each in df.capital:
    if each[0] == "B":
        print(df.loc[df.capital == each])

