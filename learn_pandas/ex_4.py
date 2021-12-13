#  Selecting Data

import pandas as pd

# NOTE: Reading the files we need
excel_file = 'sampleData.xlsx'
csv_file = 'sampleData.csv'


df_csv = pd.read_csv(csv_file)
df_xl = pd.read_excel(excel_file)

# NOTE:  accessing data
# same concepts can be applied to df_xl
print("-"*30 + "DATA with specified headers" + "-"*30)
print(df_csv[['fruit', 'Price']])  # NOTE: passed column value to be printed
print("-"*30 + "DATA with Specified Row" + "-"*30)
print(df_csv.at[3, 'fruit'])  # NOTE: passed row & column value to be printed
print("-"*30 + "DATA with Specified Range" + "-"*30)
# NOTE: passed range of value to be printed with all columns
print(df_csv.loc[:2])
print("-"*30)
# NOTE: passed range of value to be printed with range of columns
print(df_csv.loc[0:2, 'fruit':'Price'])


'''
OUTPUT:
------------------------------DATA with specified headers------------------------------
       fruit  Price
0      Apple    3.0
1     Orange    2.0
2  Pineapple    2.5
3     Banana    5.0
4      Mango   30.0
------------------------------DATA with Specified Row------------------------------
Banana
------------------------------DATA with Specified Range------------------------------
   id      fruit  quantity_in_kg  Price  Total
0   1      Apple               2    3.0    6.0
1   2     Orange               5    2.0   10.0
2   3  Pineapple               3    2.5    7.5
------------------------------
       fruit  quantity_in_kg  Price
0      Apple               2    3.0
1     Orange               5    2.0
2  Pineapple               3    2.5

'''
