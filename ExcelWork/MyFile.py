import openpyxl
workbook = openpyxl.load_workbook("excel_sheet.xlsx")
sheets = workbook.sheetnames



print("My Minimum value of searching result :")
sheet1= workbook['MySheet']
value = sheet1['D3'].value
print(value,'\n')

print("My Maximum value of searching result :")
sheet1= workbook['MySheet']
value = sheet1['E3'].value
print(value)

print("........ next keword.........")

print("My Minimum value of searching result :")
sheet1= workbook['MySheet']
value = sheet1['D4'].value
print(value,'\n')

print("My Maximum value of searching result :")
sheet1= workbook['MySheet']
value = sheet1['E4'].value
print(value)

