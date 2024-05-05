#read the data from the source 
#save it in data/raw  directory for further process4



import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in df.columns]
    
    #getting raw data file path 
    raw_file_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_file_path, sep=",", index = False, header = new_cols)
    print(df.head())



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parse_args =  args.parse_args()
    df = load_and_save(config_path = parse_args.config)