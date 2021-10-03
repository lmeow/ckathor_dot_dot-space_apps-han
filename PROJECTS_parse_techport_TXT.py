import json
from types import new_class
import re


with open("techport_projects.txt", "r", encoding="utf-8") as f:
    for newline in f.readlines():
        project = eval(newline)['project']
        project_id = ""
        project_title = ""
        project_description = ""
        project_startyear = ""
        project_endYear = ""

        if 'projectId' in project:
            project_id = str(project['projectId'])
        if 'title' in project:
            project_title = str(project['title'])
        if'description' in project:
            project_description = str(project['description'])
        if'startYear' in project:
            project_startyear = str(project['startYear'])
        if'endYear' in project:
            project_endYear = str(project['endYear'])

        project_node_query = "MERGE (n:TechPort:Project {tile:'"+project_title+"', projectId: '" + project_id+"', description: '" + \
            project_description + "', startYear: '" + project_startyear + \
            "', endYear: '" + project_endYear + "'})"

        print(project_node_query)
