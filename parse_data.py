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
    dataset_node = "MERGE (:Dataset {"

    # iterating key-value pairs
    for attr, value in dataset.items():
        if attr[0] == '@':

            # replacing symbol since neo4j doesnt accept @-symbools as property name
            attr = 'at_'+attr[1:]

        # if property value is a string, add as property in Dataset node
        if type(value) == str:
            dataset_node += attr+":'"+value+"',"

        # if property value is a list, and the elements are a string, then create new nodes for
        # each of the elements with the property name as label
        # if the lements are an object, then create new nodes for
        # each of the elements with the key-value pairs as properties an the property name as Label
        if type(value) == list:
            attr_label = attr[0].upper()+attr[1:]
            if type(value[0]) == str:
                new_node = ""
                for str_element in value:
                    # print(str_element)
                    new_node += " MERGE (n:" + attr_label + \
                        " {title:'"+str_element+"'})"
                # print(new_node)

            if type(value[0]) == dict:
                new_node = ""
                attr_label = attr[0].upper()+attr[1:]

                for dict_element in value:
                    new_node += " MERGE (n:" + attr_label + " {"
                    for dict_attr, dict_value in dict_element.items():
                        if dict_attr[0] == '@':
                            dict_attr = 'at_'+dict_attr[1:]

                        new_node += dict_attr+":'"+dict_value+"', "
                    new_node = new_node[:-2]+"})"
                # print(new_node)

        if type(value) == dict:
            attr_label = attr[0].upper()+attr[1:]
            new_node_object = ""
            new_node_object += " MERGE (n:" + attr_label + " {"
            for dict_attr, dict_value in value.items():
                dict_attr = 'at_'+dict_attr[1:]

                new_node_object += dict_attr+":'"+dict_value+"', "
            new_node_object = new_node_object[:-2]+"})"

            print(new_node_object)
            # for element in value:
            # if type(element) == string:

            # new_node += ""

    dataset_node = dataset_node[:-1]+"})"

    # print(attr, value)
    # dataset_node += "})"

    # print(dataset_node)
