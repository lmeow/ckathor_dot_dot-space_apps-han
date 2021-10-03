from lxml import etree
import os

directory = './SKOS/'

xslt_root = etree.parse('./SKOS/Access.skos')

for filename in os.listdir(directory):
    print(filename.replace('.skos', ''))

concept_tag = "{http://www.w3.org/2004/02/skos/core#}Concept"
preflabel_tag = "{http://www.w3.org/2004/02/skos/core#}prefLabel"
altLabel_tag = "{http://www.w3.org/2004/02/skos/core#}altLabel"

preflabel = ''
altLabel = ''

for concept in xslt_root.findall(concept_tag):
    concept_children = concept.findall(".//")
    # print(concept_children)
    for child in concept_children:
        tags = child.tag.split('}')[1]
        print(tags, child.text)
        # if child.tag == preflabel_tag:
        #     preflabel = child.text
        #     print('preflabel:', preflabel)
        # if child.tag == altLabel_tag:
        #     altLabel = child.text
        #     print('altLabel:', altLabel)

        # print(preflabel, altLabel)
        # print(xslt_root)
