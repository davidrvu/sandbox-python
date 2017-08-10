import pandas as pd
import numpy as np

def eprintDeb(stringIn, debug):
    if debug == 1:
        print(stringIn)

def main():
    ######################################################
    ## PARAMETROS
    ######################################################
    fileIx   = "dataInNaN.csv"
    delimIX  = ","
    xyzColIx = "1,2,3"
    debug    = 1 
    ######################################################

    try:
        dataIx = pd.read_csv(fileIx, delimiter = delimIX, keep_default_na = False, dtype=str)
    except IOError:
        eprint("\nERROR: El archivo: " + fileIx + " NO existe ")
        sys.exit()

    if xyzColIx is None:
        eprint("\nERROR: xyzColIx es None")
        sys.exit()

    try:
        xyzColIxList = xyzColIx.split(",")
        XcolIx = int(xyzColIxList[0])
        YcolIx = int(xyzColIxList[1])
        ZcolIx = int(xyzColIxList[2])
    except:
        eprint("\nERROR: xyzColIx: " + xyzColIx + " NO es valido ")
        sys.exit()

    headersIx = list(dataIx.columns.values)
    eprintDeb("headersIx = ", debug)
    eprintDeb(headersIx, debug)

    try:
        dataIx[headersIx[XcolIx]] = pd.to_numeric(dataIx[headersIx[XcolIx]])
        dataIx[headersIx[YcolIx]] = pd.to_numeric(dataIx[headersIx[YcolIx]])
        dataIx[headersIx[ZcolIx]] = pd.to_numeric(dataIx[headersIx[ZcolIx]])
    except Exception:
        eprint ("\nERROR: Las coordenadas de archivo de entrada " + fileIx + " deben tener valores numericos")
        sys.exit()


    print(dataIx)

    ######################################################
    ## ELIMINA FILAS NaN en columnas xyzColIx
    ######################################################
    dataIx = dataIx[np.isfinite(dataIx[headersIx[XcolIx]])]
    dataIx = dataIx[np.isfinite(dataIx[headersIx[YcolIx]])]
    dataIx = dataIx[np.isfinite(dataIx[headersIx[ZcolIx]])]
    dataIx = dataIx.reset_index(drop=True) # Se resetea el indice

    print("______________________________________________________")
    print("DATAFRAME POST FILTRO NaN para coordenadas XYZ")
    print("______________________________________________________")
    print(dataIx)




    print("DONE!")



if __name__ == "__main__":
    main()