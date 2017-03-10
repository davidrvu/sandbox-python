# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from downloadFile import downloadFile
import json

def main():
    
    urlIni  = "http://www.fakewebtest.com/mercado/Paginas/Resumen-de-Instrumento.aspx?RequestHistorico=1&NEMO="
    strExt  = "csv"

    jsonAll = json.loads(open('codigos.json').read())
    listaInstrumentos    = jsonAll["ListaInstrumentos"]
    listaInstrumentosLen = len(listaInstrumentos)

    strNames = []
    for i in range(0,listaInstrumentosLen):
        strNames.append(str(listaInstrumentos[i]["Nemo"]))

    for i in range(0, listaInstrumentosLen):
        porcent    = i*100.0/float(listaInstrumentosLen)
        porcentStr = str.format('{0:.3f}', porcent)
        print "i = " + str(i) + " de " + str(listaInstrumentosLen-1) + " ( " + porcentStr + " % )"
        downloadFile(urlIni, strNames[i], strExt)

if __name__ == "__main__":
    main()