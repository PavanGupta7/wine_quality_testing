#splitting dataset train and test

#save it in data/processed directory

import os 
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_savedata(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep =",")
    train_df, test_df = train_test_split(
        df, 
        test_size = split_ratio, random_state = random_state)
    train_df.to_csv(train_data_path, sep=",", encoding = 'utf-8', index = False)
    test_df.to_csv(test_data_path, sep=",",encoding = 'utf-8',  index = False)



if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parse_args =  args.parse_args()
    split_and_savedata(config_path = parse_args.config)