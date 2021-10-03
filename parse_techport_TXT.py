import json
from types import new_class
import re


with open("techport_projects.txt", "r", encoding="utf-8") as f:
    for newline in f.readlines():
        
        # print(line)
        # newline = line[:-2]
        
        newline = newline.replace("'", "!BAJS!")
        newline = newline.replace('"', "'")
        # newlime = re.sub("!BAJS!", '"', newline)
        newline = newline.replace("!BAJS!", '"')
        newline = json.dumps(newline, indent=4)
        print(newline)
        # json_proj = json.loads(json.dumps(newline))
        # outdata = eval(json_proj)

        # print(type(json_proj))
        # json_proj = json.loads(newline)
        # print(type(json_proj))
        # print(newline)

        # skrivut = json.loads(newline)
        # print(type(newline))