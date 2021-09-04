# Select multiple Sheets
import pandas as pd

excel_file = 'sampleData.xlsx'
# NOTE Selected multiple sheets and getting 2 rows of data from each sheet
df = pd.read_excel(excel_file, sheet_name=[0, 1], nrows=2)
print(df)

'''
OUTPUT:
{0:    id Author  Title  Cost
0   1  Shijo  Book1     3
1   2   Jojo  Book3     5, 1:    id   fruit  quantity_in_kg  Price  Total
0   1   Apple               2      3      6
1   2  Orange               5      2     10}
'''
