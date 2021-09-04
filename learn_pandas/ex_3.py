# DataFrame Creation with specified condition

import pandas as pd

# NOTE: Reading the files we need
excel_file = 'sampleData.xlsx'
csv_file = 'sampleData.csv'

#  NOTE: creating a dataframe with user specified sheeet
df_sheet = pd.read_excel(excel_file, sheet_name="Sheet2")
df_sheet_with_index = pd.read_excel(excel_file, sheet_name=[1])
df_cols = pd.read_excel(excel_file, usecols=['Author', 'Title'])
df = pd.read_csv(csv_file)


print("-"*30 + "DATA with Sheet Specified" + "-"*30)
print(df_sheet)
print("-"*30 + "DATA with cols Specified" + "-"*30)
print(df_cols)
print("-"*30 + "DATA with limits Specified" + "-"*30)
# NOTE: Reading first 2 rows
print(df_sheet.head(2))
print("-"*30)
# NOTE: Reading last 2 rows
print(df_sheet.tail(2))
print("-"*30 + "Inspecting data" + "-"*30)
print(df_cols.index)
print(df_sheet.columns)
print(df.dtypes)


'''
OUTPUT:
------------------------------DATA with Sheet Specified------------------------------
   id      fruit  quantity_in_kg  Price  Total
0   1      Apple               2    3.0    6.0
1   2     Orange               5    2.0   10.0
2   3  Pineapple               3    2.5    7.5
3   4     Banana               2    5.0   10.0
4   5      Mango               1   30.0   30.0
------------------------------DATA with cols Specified------------------------------
  Author  Title
0  Shijo  Book1
1   Jojo  Book3
2    Joe  Book2
------------------------------DATA with limits Specified------------------------------
   id   fruit  quantity_in_kg  Price  Total
0   1   Apple               2    3.0    6.0
1   2  Orange               5    2.0   10.0
------------------------------
   id   fruit  quantity_in_kg  Price  Total
3   4  Banana               2    5.0   10.0
4   5   Mango               1   30.0   30.0
------------------------------Inspecting data------------------------------
RangeIndex(start=0, stop=3, step=1)
Index(['id', 'fruit', 'quantity_in_kg', 'Price', 'Total'], dtype='object')
id                  int64
fruit              object
quantity_in_kg      int64
Price             float64
Total             float64
dtype: object
 
'''
