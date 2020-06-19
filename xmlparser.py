import xml.etree.ElementTree as ET

# Store data in memory from disk

tree = ET.parse('test.xml')
root = tree.getroot()

print(root.tag)

print(root.attrib)


for child in root:
    print(child.tag, child.attrib)


#Opc server

