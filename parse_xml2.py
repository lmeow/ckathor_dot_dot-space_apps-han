from bs4 import BeautifulSoup
from lxml import etree

xslt_root = etree.parse('./SKOS/competencies.xml')

concept_tag = "{http://www.w3.org/2004/02/skos/core#}Concept"
preflabel_tag = "{http://www.w3.org/2004/02/skos/core#}prefLabel"
altLabel_tag = "{http://www.w3.org/2004/02/skos/core#}altLabel"

preflabel = ''
altLabel = ''

for concept in xslt_root.findall(concept_tag):
    concept_children = concept.findall(".//")
    for child in concept_children:
        if child.tag == preflabel_tag:
            preflabel = child.text
            print('preflabel:', preflabel)
        if child.tag == altLabel_tag:
            altLabel = child.text
            print('altLabel:', altLabel)

        # print(preflabel, altLabel)
        # print(xslt_root)
