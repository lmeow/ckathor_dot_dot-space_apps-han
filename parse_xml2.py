from dotenv import dotenv_values
from neo4j import GraphDatabase
from lxml import etree
import os
concept_tag = "{http://www.w3.org/2004/02/skos/core#}Concept"
directory = './SKOS/'

config = dotenv_values(".env")
uri = config.get('NEO4J_URI')
user = config.get('NEO4J_USER')
password = config.get('NEO4J_PASSWORD')
driver = GraphDatabase.driver(uri, auth=(user, password))


for filename in os.listdir(directory):
    filename_label = filename.replace('.skos', '')
    # filename_label_query = "MERGE (n:SKOS:"+filename_label+" {title: "

    xslt_root = etree.parse(directory+filename)
    preflabel = ''
    altLabel = ''
    child_label_query = ''
    count = "0"

    for concept in xslt_root.findall(concept_tag):
        filename_label_query = "MERGE "
        filename_node = "(n:SKOS:"+filename_label+" {title: "

        concept_children = concept.findall(".//")
        child_label_query = ''
        for child in concept_children:
            if child.text:
                tags = child.tag.split('}')[1]
                if tags == 'prefLabel':
                    filename_node += "'" + \
                        child.text.replace('\"', '\\"').replace(
                            "'", "\\'")+"'})"
                    filename_label_query += filename_node

                    def run_label_queries(tx):
                        global filename_label_query
                        print(filename_label_query)
                        tx.run(filename_label_query)

                    with driver.session() as session:
                        session.write_transaction(run_label_queries)

                if tags == 'altLabel' or tags == 'prefLabel':
                    child_label_query = "MATCH " + filename_node+" MERGE (a"+count + \
                        ":SKOS:Keyword {title: '" + child.text.replace('\"', '\\"').replace("'", "\\'") + \
                        "'}) MERGE (a"+count + \
                        ")<-[:HAS_KEYWORD]-(n)"

                    def run_queries(tx):
                        global child_label_query
                        print(child_label_query)
                        tx.run(child_label_query)

                    with driver.session() as session:
                        session.write_transaction(run_queries)

                    count = str(int(count) + 1)

        # query = filename_label_query + child_label_query

    # query = filename_label_query + child_label_query
    # print(query)
    print()

    print()

driver.close()
