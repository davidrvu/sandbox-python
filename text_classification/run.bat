::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: RUN FILE
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo RUN FILE
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo RUNNING main_all.py ...

::CALL timecmd python main_all.py --debug=1 --model_mode=0 --file_in="C://davidrvu//data_bases//dbpedia//dbpedia_all.csv" --train_perc=0.89 --header_features="content" --header_labels="class" --max_vocab_length=25 --fig_dir="C://davidrvu//data_bases//dbpedia//fig\"

::CALL timecmd python main_all.py --debug=1 --model_mode=0 --file_in="C://davidrvu//data_bases//dbpedia//dbpedia_all_small.csv" --train_perc=0.89 --header_features="content" --header_labels="class" --max_vocab_length=15 --fig_dir="C://davidrvu//data_bases//dbpedia//fig//"



:: EL MEJOR HASTA EL MOMENTO: model_mode=0 :: BAG OF WORDS
:: DBPEDIA
::CALL timecmd python main_all.py --debug=1 --model_mode=0 --file_in="C://davidrvu//data_bases//dbpedia//dbpedia_all_small.csv" --train_perc=0.89 --header_features="content" --header_labels="class" --max_vocab_length=25 --fig_dir="C://davidrvu//data_bases//dbpedia//fig//"

:: FAKE_DATA
::CALL timecmd python main_all.py --debug=1 --model_mode=0 --file_in="C://davidrvu//data_bases//fake_data//fake_3clases_10500samples.csv" --train_perc=0.8 --header_features="content" --header_labels="class" --max_vocab_length=25 --fig_dir="C://davidrvu//data_bases//fake_data//fig//" 


:: LATAM

CALL timecmd python main_all.py --debug=1 --model_mode=0 --file_in="C://davidrvu//Proyectos//LATAM//1_continuidad_negocios_drvu//data//KPIs Funcional Carga_2017W38_filtered_lang.csv" --train_perc=0.8 --header_features="words_filtered" --header_labels="Sistema" --max_vocab_length=25 --fig_dir="C://davidrvu//Proyectos//LATAM//1_continuidad_negocios_drvu//fig//BOW//"