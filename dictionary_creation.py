from lxml import etree 
def write_to_dict(climate_term, title):
    dictionary_element = etree.Element("dictionary")
    dictionary_element.attrib['title'] = title
    for term in climate_term:
        entry_element = etree.SubElement(dictionary_element, "entry")
        entry_element.attrib['term'] = term
    xml_dict = etree.tostring(dictionary_element, pretty_print=True).decode('utf-8')

    with open(f'{title}.xml', mode='w', encoding='utf-8') as f:
        f.write(xml_dict)


example_terms = ["migration", "displacement", "urbanisation", "relocation", "resettlement", "vulnerability", "health", "disease", "zoonoses", "food availability", "nutrition"
]

write_to_dict(example_terms, "migration")