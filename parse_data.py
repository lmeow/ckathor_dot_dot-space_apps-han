import requests
import io
from defusedxml.ElementTree import fromstring
import os
import json
import uuid
import pickle

# p_file = 'words_pickle.p'

r = requests.get('https://data.nasa.gov/data.json')

r_datasets = r.json()['dataset']

o = io.open('./datasets.json', 'a', encoding='utf-8')


# for dataset in r_datasets:

#     # Open file with BFS (that is not modified with guids)
# m = io.open('./bfs/'+bfs['id']+'.json', 'r', encoding='utf-8').read()
# # Dump all data from BFS file as string, then loads as json object
# n = json.loads(json.dumps(m))
# # Delete existing modified BFS file to create a new one
# os.remove('./bfs_br.ai/'+bfs['id']+'.json')
# # Open new file with "append"
# # Convert json objects to python dictionary
# outfile = eval(n)

# First parameters in first object before loop
# print(r_datasets)
json.dump(r_datasets, o)


# print(r.json()['userId'])
# print(r.json()['conformsTo'])
# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# r.json()
