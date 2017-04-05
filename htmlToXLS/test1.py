# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

import sys
from html_table_to_excel import html_table_to_excel
from export_to_xls import export_to_xls

def main():
    print " Testing html_table_to_excel and export_to_xls"

    archivoInput  = "html_example.txt"
    #archivoInput  = "html_example2.txt"
    archivoOutput = "output/output.xls"
    titleOutput   = "Sheet1"

    try:
        fileIn = open(archivoInput, "r") 
    except IOError:
        print "\nERROR: El archivo " + archivoInput + " NO existe."
        sys.exit()

    tablaTest = fileIn.read() 
    print tablaTest


    dataTest = html_table_to_excel(tablaTest)
    print " Se escribe archivo xls: " + archivoOutput
    export_to_xls(dataTest, title=titleOutput, filename=archivoOutput)
    print " DONE!"

if __name__ == "__main__":
    main()