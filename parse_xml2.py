from lxml import etree
import os
concept_tag = "{http://www.w3.org/2004/02/skos/core#}Concept"
directory = './SKOS/'

for filename in os.listdir(directory):
    filename_label = filename.replace('.skos', '')

    xslt_root = etree.parse('./SKOS/'+filename)

    preflabel = ''
    altLabel = ''

    for concept in xslt_root.findall(concept_tag):
        concept_children = concept.findall(".//")
        for child in concept_children:
            tags = child.tag.split('}')[1]
            print(tags, child.text)
