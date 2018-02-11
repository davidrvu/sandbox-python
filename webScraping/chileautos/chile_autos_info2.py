#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from lxml import html
import requests
import xlwt
from datetime import datetime

print '=================================================================================='
print '=============      WEB SCRAPING BY DAVID VALENZUELA URRUTIA 2016     ============='
print '=================================================================================='
wb = xlwt.Workbook()
ws = wb.add_sheet('ChileAutos')

# HEADER
ws.write(0, 0, 'MARCA') 
ws.write(0, 1, 'MODELO')
ws.write(0, 2, 'AnO')
ws.write(0, 3, 'PRECIO')
ws.write(0, 4, 'VENDEDOR')
ws.write(0, 5, 'CIUDAD')
ws.write(0, 6, 'LINK')

# maximo 645
for num_pagina in xrange(1 , 645):

    num_pagina_str = str(num_pagina)
    print "num_pagina = " + num_pagina_str
    direccion_web = 'http://www.chileautos.cl/cemagic.asp?region=0&ciudad=0&tipo=Todos&carroceria=&maresp=0&modelo=&combustible=0&kilom=&c_otros=&cili=0&cilf=0&vendedor=0&ai=1920&af=2016&pi=0&pf=1000000000&fecha_ini=&fecha_fin=&disp=1&dea=100&pag=' + num_pagina_str
    page     = requests.get(direccion_web)
    response = html.fromstring(page.content)
    i = 0
    for sel in response.xpath('//tr'):
        i = i+1
        if i>101:
            break

        marca_modelo = sel.xpath('td/a/text()')
        marca_modelo_str   = str(marca_modelo)
        marca_modelo_str = marca_modelo_str.replace("[", "")
        marca_modelo_str = marca_modelo_str.replace("]", "")
        marca_modelo_str = marca_modelo_str.replace("'", "")
        marca_modelo_split = marca_modelo_str.split(' ')
        marca              = marca_modelo_split[0]
        del marca_modelo_split[0]
        modelo             = " ".join(marca_modelo_split)

        link     = sel.xpath('td/a/@href')
        link_str   = str(link)
        link_str   = link_str.replace("//", "")
        link_str   = link_str.replace("[", "")
        link_str   = link_str.replace("]", "")
        link_str   = link_str.replace("'", "")

        data     = sel.xpath('td/text()')
        data_str = str(data)
        data_str = data_str.replace("[", "")
        data_str = data_str.replace("]", "")   
        data_str = data_str.replace("'", "")
        data_split = data_str.split(', ')
        
        ano      = data_split[0]
        del data_split[0]
        data_split = ", ".join(data_split)
        data_split = data_split.split(', ')

        precio    = data_split[0]
        del data_split[0]
        data_split = ", ".join(data_split)
        data_split = data_split.split(', ')

        vendedor  = data_split[0]
        del data_split[0]
        data_split = ", ".join(data_split)
        data_split = data_split.split(', ')

        ciudad   = data_split[0]

        #print(' \n ______________________________________________\n')
        #print "Numero fila : {} \n".format(i)
        #print(' \n marca: ')
        #print marca
        #print(' \n modelo: ')
        #print modelo
        #print(' \n ano: ')
        #print ano
        #print(' \n precio: ')
        #print precio
        #print(' \n vendedor: ')
        #print vendedor
        #print(' \n ciudad: ')
        #print ciudad   
        #print(' \n link: ')
        #print link_str
        #print(' \n')

        if i >= 2:
            if num_pagina == 1:
                fila_excel = i-1
                ws.write( fila_excel, 0, marca) 
                ws.write( fila_excel, 1, modelo)
                ws.write( fila_excel, 2, ano)
                ws.write( fila_excel, 3, precio)
                ws.write( fila_excel, 4, vendedor)
                ws.write( fila_excel, 5, ciudad)
                ws.write( fila_excel, 6, link_str)
            else:
                fila_excel = (100*(num_pagina-1)) + i
                ws.write( fila_excel, 0, marca) 
                ws.write( fila_excel, 1, modelo)
                ws.write( fila_excel, 2, ano)
                ws.write( fila_excel, 3, precio)
                ws.write( fila_excel, 4, vendedor)
                ws.write( fila_excel, 5, ciudad)
                ws.write( fila_excel, 6, link_str)

    print "fila_excel = " + str(fila_excel)


print 'Guardando archivo ... Por favor espere'
wb.save('chile_autos.xls')
print 'LISTO!'

# TODO 4: Hacer lo mismo para TODAS las paginas de CHILEAUTOS 