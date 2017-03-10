import urllib
import sys

def downloadFile(urlIni, strName, strExt):
    urlGlobal = urlIni + strName
    pathFile  = "downloadedData/" + strName + "." + strExt
    print "Downloading " + strName + " to " + pathFile
    try:
    	urllib.urlretrieve (urlGlobal, pathFile)
    except IOError:
    	print "    ERROR: urlGlobal = " + urlGlobal + " NO ES VALIDA.\n"