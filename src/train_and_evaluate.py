#model training and evaluation


import os
import argparse
import numpy as np
import pandas as pd
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import joblib
import json

 #metrics
def model_evaluation(y_test, prediction):
    mse = mean_squared_error(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    r2_scr = r2_score(y_test, prediction)
    rmse = np.sqrt(mse)

    rmse = np.sqrt(mse)
    return  mse, rmse, mae, r2_scr


#model training and model evaluation
def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config['split_data']['train_path']
    test_data_path = config['split_data']['test_path']

    random_state = config['base']['random_state']
    model_dir = config['model_dir']

    alpha  = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = config['estimators']['ElasticNet']['params']['l1_ratio']

    target = config['base']['target_col']

    train_df = pd.read_csv(train_data_path, sep= ",")
    test_df = pd.read_csv(test_data_path, sep=",") 

    train_y = train_df[target]
    test_y = test_df[target]

    train_x = train_df.drop(target, axis=1)
    test_x = test_df.drop(target, axis=1)

    lr = ElasticNet(
        alpha = alpha, 
        l1_ratio = l1_ratio, 
        random_state = random_state)
    lr.fit(train_x, train_y)
    y_pred = lr.predict(test_x)

    (_,rmse, mae, r2_scr) = model_evaluation(test_y, y_pred)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print(" Root Mean Squared Error: %s" % rmse)
    print('Mean Absolute Error: %s'% mae)
    print("R2 Score: %s"%r2_scr)

    scores_file = config['report']['scores']  #to save model  metrics scores
    params_file = config['report']['params']   #to save model parameters

    #saving model parameters
    with open(params_file, "w") as file:
        params  = {
            "alpha":alpha,
            "L1_Ratio":l1_ratio
        }
        json.dump(params,file, indent=4)
    
    #saving model metrics scores
    with open(scores_file, "w") as file:
        scores = {
            "RMSE": rmse,
            "MAE": mae,
            "R2 Score": r2_scr
        }
        json.dump(scores,file,indent = 4)

    #now saving model
    os.makedirs(model_dir, exist_ok = True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(lr, model_path)






if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path = parsed_args.config)

    
