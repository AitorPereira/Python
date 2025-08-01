import pandas as pd

file_excel = pd.ExcelFile('/Users/aitor/Downloads/excelfile.xlsx')

my_data = file_excel.parse('Sheet1')
print (my_data)