::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: RUN FILE
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo RUN FILE
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo RUNNING main_all.py ...

::CALL timecmd python main_all.py --debug=1 --mode=0 --file_in="C:\davidrvu\data_bases\dbpedia\dbpedia_all.csv"
CALL timecmd python main_all.py --debug=1 --mode=1 --file_in="C:\davidrvu\data_bases\dbpedia\dbpedia_all_small.csv"