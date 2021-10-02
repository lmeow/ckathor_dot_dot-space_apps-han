import requests
import io
from defusedxml.ElementTree import fromstring
import os
import json
import uuid
import pickle

# p_file = 'words_pickle.p'

# r = requests.get('https://data.nasa.gov/data.json')
# r_datasets = r.json()['dataset'][:100]
# o = io.open('./datasets.json', 'a', encoding='utf-8')


# for dataset in r_datasets:


# json.dump(r_datasets, o)

# Open file with BFS (that is not modified with guids)
m = io.open('./datasets.json', 'r', encoding='utf-8').read()
# Dump all data from BFS file as string, then loads as json object
n = json.loads(m)
print(n)
for dataset in n:
    # print(type(dataset))

    dataset_node = "MERGE (:Dataset {"
    for attr, value in dataset.items():
        if attr[0] == '@':
            attr.replace('@', 'at_')
        if type(value) == str:
            dataset_node += attr+":'"+value+"',"
        # print(attr, value)
    # dataset_node += "})"

    print(dataset_node)
