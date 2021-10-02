from bs4 import BeautifulSoup
from lxml import etree

BS_data = []
with open("competencies.xml", "r") as f:
    xmlfile = etree.parse(f)
    # XMLdata = f.read()
    # XMLdata = f.readlines()
    # XMLdata = "".join(XMLdata)

code_URI = r"{http://nasataxonomy.jpl.nasa.gov/cvFields#}code"
Concept_URI = r"{http://www.w3.org/2004/02/skos/core#}Concept"
prefLabel_URI = r"{http://www.w3.org/2004/02/skos/core#}prefLabel"
altLabel_URI = r"{http://www.w3.org/2004/02/skos/core#}altLabel"
broader_URI = r"{http://www.w3.org/2004/02/skos/core#}broader"
scopeNote_URI = r"{http://www.w3.org/2004/02/skos/core#}scopeNote"
status_URI = r"{http://nasataxonomy.jpl.nasa.gov/cvFields#}status"
type_URI = r"{http://nasataxonomy.jpl.nasa.gov/cvFields#}type"
inputdate_URI = r"{http://nasataxonomy.jpl.nasa.gov/cvFields#}inputdate"
modified_URI = r"{http://purl.org/dc/terms/}modified"

datalist = []
preflabel_exist = False
altlabel_exist = False
preflabel = ""
altlabel = ""
for element in xmlfile.iter():
    if element.tag == prefLabel_URI:
        preflabel = element.text
        preflabel_exist = True
    if element.tag == altLabel_URI:
        altlabel = element.text
        altlabel_exist = True
    if altlabel_exist and preflabel_exist:
        datalist.append((preflabel, altlabel))
        preflabel_exist = False
        altlabel_exist = False

for tuples in datalist:
    print(tuples)


# print(dir(xmlfile))
# testml = xmlfile.getpath(xmlfile.findall(prefLabel_URI))
# mydict = {}
# print(testml)
# for e in xmlfile.findall(Concept_URI):
#     if e.tag == Concept_URI:
#             print(e.text)
#     if e.tag == prefLabel_URI:
#         print(e.text)
    # for e in element:
        # print(e.tag)
        # if e.tag == Concept_URI:
        #     print(e.text)
        # if e.tag == prefLabel_URI:
        #     print(e.text)

# for element in xmlfile.iter():
    # if element.tag == Concept_URI:
        # print(element.text)


# xmlfile2 = etree.getroot(xmlfile)
# test = xmlfile.find("prefLabel")
# print(test)

# root = etree.XML(XMLdata)
# print(root.tag)

# data = etree.Element()

# BS_data = []
# with open("competencies.xml", "r") as f:
#     XMLdata = f.readlines()
#     XMLdata = "".join(XMLdata)
    
# BS_data = BeautifulSoup(XMLdata, "xml")
# print(XMLdata)


# print(BS_data)

# b_test = BS_data.find_all("skos:prefLabel")

# print(b_test)