# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

def html_table_to_excel(table):

    """ html_table_to_excel(table): Takes an HTML table of data and formats it so that it can be inserted into an Excel Spreadsheet.
    """

    data = {}

    table = table[table.index('<tr'):table.index('</table>')]

    rows = table.strip('\n').split('</tr>')[:-1]
    for (x, row) in enumerate(rows):   
        columns = row.strip('\n').split('</td>')[:-1] 
        data[x] = {}
        for (y, col) in enumerate(columns):
            data[x][y] = col.replace('<tr>', '').replace('<td>', '').strip()

    return data