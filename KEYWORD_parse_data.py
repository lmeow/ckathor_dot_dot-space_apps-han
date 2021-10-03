import requests
import io
from defusedxml.ElementTree import fromstring
import os
import json
import uuid
import pickle
import codecs
from neo4j import GraphDatabase
from dotenv import dotenv_values

config = dotenv_values(".env")
uri = config.get('NEO4J_URI')
user = config.get('NEO4J_USER')
password = config.get('NEO4J_PASSWORD')

driver = GraphDatabase.driver(uri, auth=(user, password))


def check_if_at(attr):
    '''replacing symbol since neo4j doesnt accept @-symbools as property name'''

    if attr[0] == '@':
        attr = 'at_'+attr[1:]
    return attr


def get_relationship(name):
    return name

# p_file = 'words_pickle.p'


r = requests.get('https://data.nasa.gov/data.json')
r_datasets = r.json()['dataset'][18452:]
o = io.open('./datasets.json', 'a', encoding='utf-8')


# for dataset in r_datasets:


# json.dump(r_datasets, o)

# Open file with BFS (that is not modified with guids)
# m = io.open('./datasets.json', 'r', encoding='utf-8').read()
# Dump all data from BFS file as string, then loads as json object
# n = json.loads(m)
for dataset in r_datasets:
    dataset_node = "MERGE (a:Dataset {"

    new_node_list_str = ""
    count_l_str = "0"
    new_node_list_obj = ""
    count_l_obj = "0"
    new_node_object = ""
    count_obj = "0"

    # iterating key-value pairs
    for attr, value in dataset.items():
        attr = check_if_at(attr).replace('-', '_')

        # if property value is a string, add as property in Dataset node
        if type(value) == str:
            dataset_node += attr+":'" + \
                value.replace('\"', '\\"').replace("'", "\\'")+"',"
        attr_label = attr[0].upper()+attr[1:]

        # if property value is a list, and the elements are a string, then create new nodes for
        # each of the elements with the property name as label
        if type(value) == list:
            if type(value[0]) == str:
                # new_node_list_str = ""
                for str_element in value:
                    new_node_list_str += " MERGE (n"+count_l_str+":" + attr_label + \
                        " {title:'"+str_element.replace('\"', '\\"').replace("'", "\\'")+"'}) MERGE (n"+count_l_str + \
                        ")<-[:HAS_"+attr_label.upper() + "]-(a)"
                    count_l_str = str(int(count_l_str) + 1)

            # if the elements in list are objects, then create new nodes for
            # each of the elements with the key-value pairs as properties and the property name as Label
            if type(value[0]) == dict:
                # new_node_list_obj = ""
                for dict_element in value:
                    new_node_list_obj += " MERGE (m" + \
                        count_l_obj+":" + attr_label + " {"
                    for dict_attr, dict_value in dict_element.items():
                        dict_attr = check_if_at(dict_attr).replace('-', '_')
                        new_node_list_obj += dict_attr+":'" + \
                            dict_value.replace('\"', '\\"').replace(
                                "'", "\\'")+"', "
                    new_node_list_obj = new_node_list_obj[:-2] + \
                        "}) MERGE (m"+count_l_obj + \
                        ")<-[:HAS_"+attr_label.upper() + "]-(a)"
                    count_l_obj = str(int(count_l_obj) + 1)

        if type(value) == dict:
            # new_node_object = ""

            new_node_object += " MERGE (o"+count_obj+":" + attr_label + " {"
            for dict_attr, dict_value in value.items():
                dict_attr = check_if_at(dict_attr).replace('-', '_')
                new_node_object += dict_attr+":'" + \
                    dict_value.replace('\"', '\\"').replace("'", "\\'")+"', "
            new_node_object = new_node_object[:-2] + \
                "}) MERGE (o"+count_obj + \
                ")<-[:HAS_"+attr_label.upper() + "]-(a)"

            count_obj = str(int(count_obj) + 1)

    dataset_node = dataset_node[:-1]+"})"
    query = dataset_node + new_node_list_str + \
        new_node_list_obj + new_node_object+";"

    # print()

    def run_queries(tx):
        global query
        print(query)
        tx.run(query)

    with driver.session() as session:
        session.write_transaction(run_queries)

    print()
driver.close()

#     json.dump(query.strip('"'), o, ensure_ascii=False)
# i = io.open('./datasets.json', 'r', encoding='utf-8')
# p = io.open('./datasets1.json', 'a', encoding='utf-8')

# json.dump(i.strip('"'), p, ensure_ascii=False)
