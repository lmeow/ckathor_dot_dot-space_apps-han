import json
from types import new_class
import re
from neo4j import GraphDatabase
from dotenv import dotenv_values

config = dotenv_values(".env")
uri = config.get('NEO4J_URI')
user = config.get('NEO4J_USER')
password = config.get('NEO4J_PASSWORD')
driver = GraphDatabase.driver(uri, auth=(user, password))

with open("techport_projects.txt", "r", encoding="utf-8") as f:
    for newline in f.readlines():
        project = eval(newline)['project']
        project_id = ""
        project_title = ""
        project_description = ""
        project_startyear = ""
        project_endYear = ""
        tax_nodes = ""
        dest_nodes = ""
        count_obj = '0'

        if 'projectId' in project:
            project_id = str(project['projectId'])
        if 'title' in project:
            project_title = str(project['title']).replace('\"', '\\"').replace(
                "'", "\\'")
        if 'description' in project:
            project_description = str(project['description']).replace('\"', '\\"').replace(
                "'", "\\'")
        if 'startYear' in project:
            project_startyear = str(project['startYear'])
        if 'endYear' in project:
            project_endYear = str(project['endYear'])

        project_node = "(n:TechPort:Project {tile: '"+project_title+"', projectId: '" + project_id+"', description: '" + \
            project_description + "', startYear: '" + project_startyear + \
            "', endYear: '" + project_endYear + "'})"

        project_node_query = "MERGE " + project_node

        def run_project_queries(tx):
            global project_node_query
            print(project_node_query)
            tx.run(project_node_query)

        if len(project_node_query) > 0:
            with driver.session() as session:
                session.write_transaction(run_project_queries)

        if 'primaryTaxonomyNodes' in project:
            for tax in project['primaryTaxonomyNodes']:
                tax_nodes += " MERGE (o"+count_obj + \
                    ":TechPort:Taxonomy {"
                for dict_attr, dict_value in tax.items():
                    t = type(dict_value)
                    if t == str or t == int:
                        dict_value = str(dict_value)
                        dict_attr = dict_attr.replace('-', '_')
                        tax_nodes += dict_attr+":'" + \
                            dict_value.replace('\"', '\\"').replace(
                                "'", "\\'")+"', "
                tax_nodes = tax_nodes[:-2] + \
                    "}) MERGE (o"+count_obj + \
                    ")<-[:HAS_TAXONOMY]-(n)"
                tax_nodes = "MATCH " + project_node + tax_nodes

                count_obj = str(int(count_obj) + 1)

        # print(tax_nodes)

                def run_tax_queries(tx):
                    global tax_nodes
                    print(tax_nodes)
                    tx.run(tax_nodes)
                if len(tax_nodes) > 0:
                    with driver.session() as session:
                        session.write_transaction(run_tax_queries)

        if 'destinations' in project:
            for destination in project['destinations']:
                dest_nodes += " MERGE (p"+count_obj + \
                    ":TechPort:Destination {"
                for dict_attr, dict_value in destination.items():
                    t = type(dict_value)
                    if t == str or t == int:
                        dict_value = str(dict_value)
                        dict_attr = dict_attr.replace('-', '_')
                        dest_nodes += dict_attr+":'" + \
                            dict_value.replace('\"', '\\"').replace(
                                "'", "\\'")+"', "
                dest_nodes = dest_nodes[:-2] + \
                    "}) MERGE (p"+count_obj + \
                    ")<-[:HAS_DESTINATION]-(n)"

                count_obj = str(int(count_obj) + 1)
                dest_nodes = "MATCH " + project_node + dest_nodes

                def run_destination_queries(tx):
                    global dest_nodes
                    print(dest_nodes)
                    tx.run(dest_nodes)

                if len(dest_nodes) > 0:

                    with driver.session() as session:
                        session.write_transaction(run_destination_queries)
