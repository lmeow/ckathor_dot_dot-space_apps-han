import requests
import json
from dotenv import dotenv_values

config = dotenv_values(".env")
API_key = config.get('API_KEY')

projectID = ""

params = {
    "api_key": API_key,
}

with open("techport_project_IDs.json", "r") as f:
    IDs = json.load(f)

IDs = IDs["projects"]
ID_parsed = []
for item in IDs:
    ID_parsed.append(item["projectId"])

my_file = open("techport_projects.txt", "a", encoding="utf-8")
i = 0
for projID in ID_parsed:

    URL = f"https://api.nasa.gov/techport/api/projects/{projID}?api_key={API_key}"
    print(URL)
    r = requests.get(URL)
    r_json = str(r.json())
    # json_data = r.json()
    my_file.write(r_json + "\n")
    
    i += 1
    if i > 500:
        break

    # json.dump(r.json(), file, indent=4)


my_file.close()