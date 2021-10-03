from bs4 import BeautifulSoup
from lxml import etree

BS_data = []
with open("./SKOS/competencies.xml", "r", encoding='ISO-8859-1') as f:
    aString = f.read()
    parser = etree.XMLParser(recover=True)
    tree = etree.fromstring(aString, parser)
    print(tree.xpath('//Concept'))
    # print(aString)
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


# for tuples in datalist:
    # print(tuples)

# print(f.read().xpath('//Concept'))


# data = open('./SKOS/competencies.xml', 'rb')
xslt_root = etree.parse('./SKOS/competencies.xml')
print(xslt_root)
# aString = f.read()
# parser = etree.XMLParser(recover=True)
# tree = etree.fromstring(aString, parser)
# print(tree.xpath('//Concept'))
