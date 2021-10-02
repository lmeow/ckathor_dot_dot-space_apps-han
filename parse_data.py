import requests
import io
from defusedxml.ElementTree import fromstring
import os
import json
import uuid
import pickle

p_file = 'words_pickle.p'

r = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(r.json()['userId'])
# print(r.json()['conformsTo'])
# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# r.json()
