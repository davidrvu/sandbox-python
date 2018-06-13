:: DAVIDRVU 2018
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo  RUN main LGBM_starter
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CALL timecmd python main.py --train_file="C:/datasets/favorita_grocery_sales/train.csv" --test_file="C:/datasets/favorita_grocery_sales/test.csv" --items_file="C:/datasets/favorita_grocery_sales/items.csv" --output_file="C:/datasets/favorita_grocery_sales/output_lgb.csv"