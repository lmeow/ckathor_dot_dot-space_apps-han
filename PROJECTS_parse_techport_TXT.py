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

        # project_title = str(project['title'])
        # project_description = str(project['description'])
        # project_startyear = str(project['startYear'])
        # project_endYear = str(project['endYear'])

        project_node_query = "MERGE (n:TechPort:Project {tile:'"+project_title+"', projectId: '" + project_id+"', description: '" + \
            project_description + "', startYear: '" + project_startyear + \
            "', endYear: '" + project_endYear + "'})"

        print(project_node_query)
        # print(line)
        # newline = line[:-2]

        # newline = newline.replace("'", "!BAJS!")
        # newline = newline.replace('"', "'")
        # # newlime = re.sub("!BAJS!", '"', newline)
        # newline = newline.replace("!BAJS!", '"')
        # newline = json.dumps(newline, indent=4)
        # print(newline)
        # json_proj = json.loads(json.dumps(newline))
        # outdata = eval(json_proj)

        # print(type(json_proj))
        # json_proj = json.loads(newline)
        # print(type(json_proj))
        # print(newline)

        # skrivut = json.loads(newline)
        # print(type(newline))
