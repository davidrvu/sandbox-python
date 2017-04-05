# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

# pip install xlwt
import xlwt

def export_to_xls(data, title='Sheet1', filename='export.xls'):

    """ export_to_xls(data, title, filename): Exports data to an Excel Spreadsheet.
    Data should be a dictionary with rows as keys; the values of which should be a dictionary with columns as keys; the value should be the value at the x, y coordinate.
    """

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(title)

    for x in sorted(data.iterkeys()):
        for y in sorted(data[x].iterkeys()):
            try:
                if float(data[x][y]).is_integer():
                    worksheet.write(x, y, int(float(data[x][y])))
                else:
                    worksheet.write(x, y, float(data[x][y]))
            except ValueError:
                worksheet.write(x, y, data[x][y])

    workbook.save(filename)

    return