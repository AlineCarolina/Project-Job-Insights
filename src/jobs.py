import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        dict_list = []
        for row in reader:
            dict_list.append(row)
    return dict_list
