##
import xlrd

class Excel():
    def __init__(self, path):
        self.sheet = ""
        self.path = path

    def readData(self):
        #Open workbook
        wb = xlrd.open_workbook(self.path)
        #Get First Sheet
        self.sheet = wb.sheet_by_index(0)
        return self.sheet

    def checkValues(self):
        return



"""
# Give the location of the file
loc = ("test.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print("XLRD: ", sheet.cell_value(0, 0))
print(sheet.col_values(1))
print([float(item) for item in sheet.col_values(1)])
"""


'''
import pyexcel
import pyexcel_xls as xls
import pyexcel_xlsx as xlsx
import json

excel = Excel("test.xlsx")
data = json.dumps(excel.readData())
data2 = excel.readData()
print(data)
print(data2)

for value in data2.keys():
    print(value)

print(list(data))
print("First Sheet: ",list(data2)[:1]) #first item in ordered dictionary
print("First Data in sheet name:", data2['Sheet1'][0][0]) #on given sheet first item first value

maxVal = max(data2, key= lambda x : data2[x])
print(maxVal)

for key, value in data2.items(): #shows items and and key in ordered dict
    print("Data, Key: " ,key, " Value: ", value)



print(type(data))
print(type(data2))
'''