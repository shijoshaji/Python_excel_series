# loading workbook

from openpyxl import load_workbook

# NOTE: loading the excel we need
wb = load_workbook(filename='sampleData.xlsx')

print(wb)  # OUTPUT: <openpyxl.workbook.workbook.Workbook object at 0x0000026C6A25AD60>
