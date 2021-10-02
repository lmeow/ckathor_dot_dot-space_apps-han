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
# print(n)
for dataset in n:
    # print(type(dataset))

    dataset_node = "MERGE (:Dataset {"
    for attr, value in dataset.items():
        if attr[0] == '@':
            # print(attr)
            attr = 'at_'+attr[1:]
        if type(value) == str:
            dataset_node += attr+":'"+value+"',"
        if type(value) == list:
            # print(value)
            attr_label = attr[0].upper()+attr[1:]
            if type(value[0]) == str:
                # print(value)
                new_node = ""
                for str_element in value:
                    # print(str_element)
                    new_node += " MERGE (n:" + attr_label + \
                        " {title:'"+str_element+"'})"
                print(new_node)
            # for element in value:
                # if type(element) == string:

                # new_node += ""

    dataset_node = dataset_node[:-1]+"})"

    # print(attr, value)
    # dataset_node += "})"

    # print(dataset_node)
