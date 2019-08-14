#!/usr/bin/python3
import configparser
import os


def get_config(path_file: str):
    config = configparser.ConfigParser()
    config.read(path_file)
    return config


path_config_file = os.environ.get('FOULE_FACTORY_CONFIG', r'.\config.ini')
config = get_config(path_config_file)
