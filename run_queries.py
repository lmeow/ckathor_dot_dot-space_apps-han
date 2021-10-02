import requests
import codecs
from neo4j import GraphDatabase
from dotenv import dotenv_values

config = dotenv_values(".env")
uri = config.get('NEO4J_URI')
user = config.get('NEO4J_USER')
password = config.get('NEO4J_PASSWORD')
driver = GraphDatabase.driver(uri, auth=(user, password))
outfile = codecs.open('datasets.json', 'r', encoding='utf-8')


# def run_queries(tx):
#     outfile = codecs.open('seed.txt', 'r', encoding='utf-8')
#     for line in outfile.readlines()[:7000]:
#         print(line)
#         tx.run(line)
#     outfile.close()


def run_queries(tx):
    outfile = codecs.open('datasets1.json', 'r', encoding='utf-8')
    for line in outfile.readlines()[:1]:
        print(line)
    # tx.run('CREATE (:CAT)')

    outfile.close()


with driver.session() as session:
    session.write_transaction(run_queries)

driver.close()
