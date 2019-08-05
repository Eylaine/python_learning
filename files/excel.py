from openpyxl import load_workbook

work_book = load_workbook("123.xlsx")
work_sheet = work_book.active

data = [['a', 2, '3', 4], [2, '3', 4], [3, 4, "aaa"]]

for each in data:
    work_sheet.append(each)

work_book.save("123.xlsx")
