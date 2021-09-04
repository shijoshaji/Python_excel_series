#  Excel Sheet to Dict, CSV and JSON
import pandas as pd

# NOTE: Reading the files we need
excel_file = 'sampleData.xlsx'
csv_file = 'sampleData.csv'

#  NOTE: creating a dataframe
df = pd.read_excel(excel_file)
df_csv = pd.read_csv(csv_file)

# NOTE: converting excel data intp Dict, JSON & CSV

dict_data = df.to_dict()
csv_data = df.to_csv(index=False)
json_data = df.to_json()

print("-"*30 + "DICTIONATY DATA" + "-"*30)
print(dict_data)
print("-"*30 + "CSV DATA" + "-"*30)
print(csv_data)
print("-"*30 + "JSON DATA" + "-"*30)
print(json_data)

# NOTE: You can write the logic to convert the csv file similar to abouve code
'''
OUTPUT:

------------------------------DICTIONATY DATA------------------------------
{'id': {0: 1, 1: 2, 2: 3}, 'Author': {0: 'Shijo', 1: 'Jojo', 2: 'Joe'}, 'Title': {0: 'Book1', 1: 'Book3', 2: 'Book2'}, 'Cost': {0: 3.0, 1:
5.0, 2: 4.5}}
------------------------------CSV DATA------------------------------
id,Author,Title,Cost
1,Shijo,Book1,3.0
2,Jojo,Book3,5.0
3,Joe,Book2,4.5

------------------------------JSON DATA------------------------------
{"id":{"0":1,"1":2,"2":3},"Author":{"0":"Shijo","1":"Jojo","2":"Joe"},"Title":{"0":"Book1","1":"Book3","2":"Book2"},"Cost":{"0":3.0,"1":5.0,"2":4.5}}
'''
