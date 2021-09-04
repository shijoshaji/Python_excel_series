# DataFrame Creation

import pandas as pd

# NOTE: Reading the files we need
excel_file = 'sampleData.xlsx'
csv_file = 'sampleData.csv'

#  NOTE: creating a dataframe
df = pd.read_excel(excel_file)
df_csv = pd.read_csv(csv_file)

print(df)
print("-"*30)
print(df_csv)


'''
OUTPUT:
  id Author  Title  Cost
0   1  Shijo  Book1   3.0
1   2   Jojo  Book3   5.0
2   3    Joe  Book2   4.5
------------------------------
   id      fruit  quantity_in_kg  Price  Total
0   1      Apple               2    3.0    6.0
1   2     Orange               5    2.0   10.0
2   3  Pineapple               3    2.5    7.5
3   4     Banana               2    5.0   10.0
4   5      Mango               1   30.0   30.0

'''
