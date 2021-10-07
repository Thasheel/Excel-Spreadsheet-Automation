import openpyxl as xl

def process_workbook(filename):
    wb = xl.load_workbook(filename)  # importing file,use Tab for crcting
    sheet = wb["Sheet1"]  # sheet name
    cell = sheet["a1"]  # index number
    cell = sheet.cell(1, 1)  # rows and colums
    # print(sheet.max_row)  # for finding how many rows
    # print(cell.value)