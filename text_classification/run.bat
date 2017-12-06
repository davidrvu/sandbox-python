::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: RUN FILE
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo RUN FILE
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo RUNNING main_all.py ...

::CALL timecmd python main_all.py --debug=1 --model_mode=1 --file_in="C:\davidrvu\data_bases\dbpedia\dbpedia_all.csv" --train_perc=0.89 --max_vocab_length=25 --embedding_size=50

::CALL timecmd python main_all.py --debug=1 --model_mode=1 --file_in="C:\davidrvu\data_bases\dbpedia\dbpedia_all_small.csv" --train_perc=0.89 --max_vocab_length=15 --embedding_size=50

CALL timecmd python main_all.py --debug=1 --model_mode=1 --file_in="C:\davidrvu\data_bases\dbpedia\dbpedia_all_small.csv" --train_perc=0.89 --max_vocab_length=25 --embedding_size=50

::CALL timecmd python main_all.py --debug=1 --model_mode=1 --file_in="C:\davidrvu\data_bases\fake_data\fake_3clases_10500samples.csv" --train_perc=0.8 --max_vocab_length=25 --embedding_size=50