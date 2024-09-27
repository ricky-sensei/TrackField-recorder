import openpyxl


def data_input(school_record, path):
    wb = openpyxl.load_workbook(path)
    ws = wb["Sheet1"]
    wb.remove(ws)
    wb.create_sheet(title="Sheet1")
    ws = wb["Sheet1"]
    for row in school_record:
        ws.append(row)
    wb.save(path)
