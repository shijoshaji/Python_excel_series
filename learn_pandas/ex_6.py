#  Apply concepts what we learnt
import pandas as pd

# NOTE: Reading the files we need
excel_file = 'sampleData.xlsx'
df = pd.read_excel(excel_file, sheet_name=None)

#  NOTE: Replica of Sheet 2 but the total here is not calculated properly
# TODO: Print fruit name where the total cost from excel is not matching with price & Qty
sheet = df["Sheet3"]
print("-"*30 + "DATA in Excel" + "-"*30)
print(sheet)
print("-"*30 + "Incorrect total cost in Excel" + "-"*30)
for item in sheet.index:
    fruit = sheet['fruit'][item]
    price = sheet['Price'][item]
    qty = sheet['quantity_in_kg'][item]
    total_cost = sheet['Total'][item]
    if (price * qty) != total_cost:
        print(
            f" {fruit} expected cost is {price * qty}, but actual cost in excel is {total_cost}")


'''
OUTPUT:
------------------------------DATA in Excel------------------------------
   id      fruit  quantity_in_kg  Price  Total
0   1      Apple               2    3.0    6.0
1   2     Orange               5    2.0    5.0
2   3  Pineapple               3    2.5    7.5
3   4     Banana               2    5.0   10.0
4   5      Mango               1   30.0   29.0
------------------------------Incorrect total cost in Excel------------------------------
 Orange expected cost is 10.0, but actual cost in excel is 5.0
 Mango expected cost is 30.0, but actual cost in excel is 29.0

'''
