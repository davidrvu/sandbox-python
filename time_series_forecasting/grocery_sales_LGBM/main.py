# DAVIDRVU 2018

# Corporación Favorita Grocery Sales Forecasting - Can you accurately predict sales for a large grocery chain?
# SOURCE: https://www.kaggle.com/c/favorita-grocery-sales-forecasting/kernels

# LGBM Starter 
# SOURCE: https://www.kaggle.com/ceshine/lgbm-starter/code

# Microsoft/LightGBM: A fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms, used for ranking, classification and many other machine learning tasks. It is under the umbrella of the DMTK(http://github.com/microsoft/dmtk) project of Microsoft. SOURCE: https://github.com/Microsoft/LightGBM

# DOWNLOAD DATA: https://www.kaggle.com/c/favorita-grocery-sales-forecasting/data

from datetime import date, timedelta
from sklearn.metrics import mean_squared_error
import argparse
import lightgbm as lgb
import numpy as np
import pandas as pd
import sys
import time

def get_timespan(df, dt, minus, periods):
    return df[pd.date_range(dt - timedelta(days=minus), periods=periods)]

def prepare_dataset(df_2017, promo_2017, t2017, is_train=True):
    X = pd.DataFrame({
        "mean_3_2017": get_timespan(df_2017, t2017, 3, 3).mean(axis=1).values,
        "mean_7_2017": get_timespan(df_2017, t2017, 7, 7).mean(axis=1).values,
        "mean_14_2017": get_timespan(df_2017, t2017, 14, 14).mean(axis=1).values,
        "promo_14_2017": get_timespan(promo_2017, t2017, 14, 14).sum(axis=1).values
    })
    for i in range(16):
        X["promo_{}".format(i)] = promo_2017[t2017 + timedelta(days=i)].values.astype(np.uint8)
    if is_train:
        y = df_2017[pd.date_range(t2017, periods=16)].values
        return X, y
    return X

def LGBM_starter(debug, train_file, test_file, items_file, output_file):
    print("\n----> START " + str(sys._getframe().f_code.co_name) )

    print("Reading train_file ...")
    df_train = pd.read_csv(
        train_file, usecols=[1, 2, 3, 4, 5],
        dtype={'onpromotion': bool},
        converters={'unit_sales': lambda u: np.log1p(float(u)) if float(u) > 0 else 0},
        parse_dates=["date"],
        skiprows=range(1, 66458909)  # 2016-01-01
    )

    print("Reading test_file ...")
    df_test = pd.read_csv(
        test_file, usecols=[0, 1, 2, 3, 4],
        dtype={'onpromotion': bool},
        parse_dates=["date"]  # , date_parser=parser
    ).set_index(['store_nbr', 'item_nbr', 'date'])

    print("Reading items_file ...")
    items = pd.read_csv(items_file).set_index("item_nbr")

    print("Setting dataframes ...")

    df_2017 = df_train[df_train.date.isin(pd.date_range("2017-05-31", periods=7 * 11))].copy()
    del df_train

    promo_2017_train         = df_2017.set_index(["store_nbr", "item_nbr", "date"])[["onpromotion"]].unstack(level=-1).fillna(False)
    promo_2017_train.columns = promo_2017_train.columns.get_level_values(1)
    promo_2017_test          = df_test[["onpromotion"]].unstack(level=-1).fillna(False)
    promo_2017_test.columns  = promo_2017_test.columns.get_level_values(1)
    promo_2017_test          = promo_2017_test.reindex(promo_2017_train.index).fillna(False)
    promo_2017               = pd.concat([promo_2017_train, promo_2017_test], axis=1)
    del promo_2017_test, promo_2017_train

    df_2017 = df_2017.set_index(["store_nbr", "item_nbr", "date"])[["unit_sales"]].unstack(level=-1).fillna(0)
    df_2017.columns = df_2017.columns.get_level_values(1)

    items = items.reindex(df_2017.index.get_level_values(1))
 
    print("Preparing dataset...")
    t2017 = date(2017, 6, 21)
    X_l, y_l = [], []
    for i in range(4):
        delta = timedelta(days=7 * i)
        X_tmp, y_tmp = prepare_dataset(df_2017, promo_2017, t2017 + delta)
        X_l.append(X_tmp)
        y_l.append(y_tmp)
    X_train = pd.concat(X_l, axis=0)
    y_train = np.concatenate(y_l, axis=0)
    del X_l, y_l
    X_val, y_val = prepare_dataset(df_2017, promo_2017, date(2017, 7, 26))
    X_test = prepare_dataset(df_2017, promo_2017, date(2017, 8, 16), is_train=False)

    print("Training and predicting models...")
    params = {
        'num_leaves': 2**5 - 1,
        'objective': 'regression_l2',
        'max_depth': 8,
        'min_data_in_leaf': 50,
        'learning_rate': 0.05,
        'feature_fraction': 0.75,
        'bagging_fraction': 0.75,
        'bagging_freq': 1,
        'metric': 'l2',
        'num_threads': 4
    }

    MAX_ROUNDS = 1000
    val_pred = []
    test_pred = []
    cate_vars = []
    for i in range(16):
        print("=" * 50)
        print("Step %d" % (i+1))
        print("=" * 50)
        dtrain = lgb.Dataset(
            X_train, label=y_train[:, i],
            categorical_feature=cate_vars,
            weight=pd.concat([items["perishable"]] * 4) * 0.25 + 1
        )
        dval = lgb.Dataset(
            X_val, label=y_val[:, i], reference=dtrain,
            weight=items["perishable"] * 0.25 + 1,
            categorical_feature=cate_vars)
        bst = lgb.train(
            params, dtrain, num_boost_round=MAX_ROUNDS,
            valid_sets=[dtrain, dval], early_stopping_rounds=50, verbose_eval=50
        )
        print("\n".join(("%s: %.2f" % x) for x in sorted(
            zip(X_train.columns, bst.feature_importance("gain")),
            key=lambda x: x[1], reverse=True
        )))
        val_pred.append(bst.predict(X_val, num_iteration=bst.best_iteration or MAX_ROUNDS))
        test_pred.append(bst.predict(X_test, num_iteration=bst.best_iteration or MAX_ROUNDS))

    print("Validation mse:", mean_squared_error(y_val, np.array(val_pred).transpose()))

    print("Making submission...")
    y_test = np.array(test_pred).transpose()
    df_preds = pd.DataFrame(y_test, index=df_2017.index, columns=pd.date_range("2017-08-16", periods=16)).stack().to_frame("unit_sales")
    df_preds.index.set_names(["store_nbr", "item_nbr", "date"], inplace=True)

    submission = df_test[["id"]].join(df_preds, how="left").fillna(0)
    submission["unit_sales"] = np.clip(np.expm1(submission["unit_sales"]), 0, 1000)
    submission.to_csv(output_file, float_format='%.4f', index=None)

    print("----> END " + str(sys._getframe().f_code.co_name) + "\n")

def main():
    print("_________________________________________________________")
    print("_____________  MAIN LGBM STARTER  _______________________")

    # TODOTODO: GRAFICOS PLOTLY

    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--debug',       type=int,  default=0,     help='Debug')
    parser.add_argument('--train_file',  type=str,  default=None,  help='Archivo train')
    parser.add_argument('--test_file',   type=str,  default=None,  help='Archivo test')
    parser.add_argument('--items_file',  type=str,  default=None,  help='Archivo items')
    parser.add_argument('--output_file', type=str,  default=None,  help='Archivo output')

    args = parser.parse_args()
    debug       = args.debug
    train_file  = args.train_file
    test_file   = args.test_file
    items_file  = args.items_file
    output_file = args.output_file

    print("_________________________________________________________")
    print("_________________ARGUMENTS_______________________________")
    print("debug       = " + str(debug))
    print("train_file  = " + str(train_file))
    print("test_file   = " + str(test_file))
    print("items_file  = " + str(items_file))
    print("output_file = " + str(output_file))

    start_time = time.time()
    LGBM_starter(debug, train_file, test_file, items_file, output_file)
    end_time   = time.time()

    total_time = end_time - start_time
    print("total_time = " + str(round(total_time,4)) + "[s].")

    print("DONE!")

if __name__ == "__main__":
    main()