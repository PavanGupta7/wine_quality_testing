import pandas as pd 
import os
import yaml
import argparse


def read_params(config_path):
    with open(config_path , 'r') as yaml_file:  # Change 'rb' to 'r' for reading text
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path)
    return df


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    
    parsed_args = arg.parse_args()
    config_file = os.path.join(os.getcwd(), parsed_args.config)  # Get full path to config file
    df = get_data(config_path=config_file)
    print(df.head())
