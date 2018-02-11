#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import unicode_literals
import scrapy
import xlwt
from datetime import datetime


wb = xlwt.Workbook()
ws = wb.add_sheet('ChileAutos')

# HEADER
#year = unicode('AnO','UTF-8')
#year = unicode("AnO", 'utf-8') 
ws.write(0, 0, 'MARCA') 
ws.write(0, 1, 'MODELO')
ws.write(0, 2, 'AnO')
ws.write(0, 3, 'PRECIO')
ws.write(0, 4, 'VENDEDOR')
ws.write(0, 5, 'CIUDAD')
ws.write(0, 6, 'LINK')

class ScrapingWeb(scrapy.Spider):

    name = "chileautos"
    allowed_domains = ["www.chileautos.cl"]
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.chileautos.cl/cemagic.asp?region=0&ciudad=0&tipo=Todos&carroceria=&maresp=0&modelo=&combustible=0&kilom=&c_otros=&cili=0&cilf=0&vendedor=0&ai=1920&af=2016&pi=0&pf=1000000000&fecha_ini=&fecha_fin=&disp=1&dea=100&pag=1"
    ]

    def parse(self, response):
        print(' \n Creado por: David Valenzuela Urrutia \n')

        #for sel in response.xpath('//table[@class="tbl_Principal"]/td'):

        i = 0
        for sel in response.xpath('//tr'):
            i = i+1
            if i>101:
                break

            #title = sel.xpath('a/text()').extract()
            marca_modelo = sel.xpath('td/a/text()').extract()
            link = sel.xpath('td/a/@href').extract()
            data = sel.xpath('td/text()').extract()

            print(' \n ______________________________________________\n')
            print "Numero fila : {} \n".format(i)
            print(' \n marca_modelo: \n')
            print marca_modelo            
            print(' \n data: \n')
            print data
            print(' \n link: \n')
            print link
            print(' \n')
            #GG = 'hola'
            #return GG

			#ws.write(sel+1, 0, marca_modelo) 
			#ws.write(sel+1, 1, marca_modelo)
			#ws.write(sel+1, 2, data)
			#ws.write(sel+1, 3, data)
			#ws.write(sel+1, 4, data)
			#ws.write(sel+1, 5, data)
			#ws.write(sel+1, 6, link)

#A = ScrapingWeb
#B = A.parse(scrapy.Spider)
wb.save('chile_autos.xls')    


# TODO 1: GUARDAR DATOS EN ARCHIVO XML (excel) |MARCA | MODELO | AnO | PRECIO | VENDEDOR | CIUDAD | LINK
# TODO 2: Separar String marca_modelo en MARCA y modelo (ojo: ver manejo de strings en python)
# TODO 3: Separar data en AnO , PRECIO , VENDEDOR y CIUDAD 
# TODO 4: Hacer lo mismo para TODAS las paginas de CHILEAUTOS 