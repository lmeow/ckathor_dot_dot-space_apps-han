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

r = requests.get('https://techport.nasa.gov/api/taxonomies/8816')
r_tax = r.json()['taxonomy']['children']

# print(r_tax)


def send_to_db(query):

    def run_queries(tx):
        print(query)
        tx.run(query)

    with driver.session() as session:
        session.write_transaction(run_queries)


def rec_search(child_c):
    if child_c['hasChildren']:
        # print('true', child_c['code'])
        child_c_node = "(:TechPort:Taxonomy {"
        for dict_attr, dict_value in child_c.items():
            t = type(dict_value)
            if t == str or t == int:
                dict_value = str(dict_value)
                dict_attr = dict_attr.replace('-', '_')
                child_c_node += dict_attr+":'" + \
                    dict_value.replace('\"', '\\"').replace(
                        "'", "\\'")+"', "
        query = "MERGE " + child_c_node[:-2]+"})"
        send_to_db(query)

        r = requests.get(
            'https://techport.nasa.gov/api/taxonomies/nodes/'+str(child_c['taxonomyNodeId']))
        for child in r.json()['children']:
            rec_search(child['content'])
    else:
        # print('false', child_c['code'])
        child_c_node = "(:TechPort:Taxonomy {"
        for dict_attr, dict_value in child_c.items():
            t = type(dict_value)
            if t == str or t == int:
                dict_value = str(dict_value)
                dict_attr = dict_attr.replace('-', '_')
                child_c_node += dict_attr+":'" + \
                    dict_value.replace('\"', '\\"').replace(
                        "'", "\\'")+"', "
        query = "MERGE " + child_c_node[:-2]+"})"
        send_to_db(query)


for a_child in r_tax:
    rec_search(a_child['content'])

# for child in r_tax:
#     if child['hasChildren']:
#         print('true')
#         for child1 in child['children']:
#             if child1['hasChildren']:
#                 if child['hasChildren']:
#                     print('true')
#                 else:
#                     print('false')
#     else:
#         print('false')
# if 'destinations' in project:
#     for destination in project['destinations']:
#         dest_nodes += " MERGE (p"+count_obj + \
#             ":TechPort:Destination {"
# for dict_attr, dict_value in destination.items():
#     t = type(dict_value)
#     if t == str or t == int:
#         dict_value = str(dict_value)
#         dict_attr = dict_attr.replace('-', '_')
#         dest_nodes += dict_attr+":'" + \
#             dict_value.replace('\"', '\\"').replace(
#                 "'", "\\'")+"', "
# dest_nodes = dest_nodes[:-2] + \
#     "}) MERGE (p"+count_obj + \
#     ")<-[:HAS_DESTINATION]-(n)"
