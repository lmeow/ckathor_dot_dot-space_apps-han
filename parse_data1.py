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


i = io.open('./datasets.txt', 'r', encoding='utf-8').read()

new_i = i.strip('"')
# json.dump(query.strip('"'), o, ensure_ascii=False)

p = io.open('./datasets1.txt', 'a', encoding='utf-8')
p.write(new_i)


# print(i.json())
# json.dump(i.strip('"'), p, ensure_ascii=False)
