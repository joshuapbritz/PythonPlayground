from openpyxl import Workbook
wb = Workbook()

ws = wb.active

ws['A1'] = 42

ws.append([1, 2, 3, 4])

wb.save('my_book.xlsx')