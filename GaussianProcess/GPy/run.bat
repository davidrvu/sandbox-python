::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: RUN GPy
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo RUN GPy
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo RUN tutorial1
CALL timecmd python tutorial1.py

::echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
::echo RUN func2
::echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
::CALL timecmd x64\Release\mainTemplateClass.exe -debug=1 -mode="func2" -coutMode=1 -outputCSV=1 -numFilas=800 -fileOut="data\\resultadofunc2.csv"
