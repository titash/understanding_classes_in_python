import xml.etree.ElementTree as ET
import json

# Parse the XML document
xml_data = """
<organization>
    <department name="HR" state="active">
        <employee id="1">
            <name>John Smith</name>
            <position>Manager</position>
        </employee>
        <employee id="2">
            <name>Alice Johnson</name>
            <position>HR Specialist</position>
        </employee>
    </department>
    <department name="IT" state="NULL">
        <employee id="3">
            <name>David Brown</name>
            <position>Director</position>
        </employee>
        <employee id="4">
            <name>Sarah Davis</name>
            <position>Software Engineer</position>
        </employee>
    </department>
</organization>
"""

root = ET.fromstring(xml_data)

# Convert the XML to a Python dictionary using a recursive function
def xml_to_dict(element):
    result = {}
    # Include attributes in the dictionary
    if element.attrib:
        result["@attributes"] = element.attrib
    for child in element:
        child_data = xml_to_dict(child)
        if child_data:
            if child.tag in result:
                if type(result[child.tag]) is not list:
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_data)
            else:
                result[child.tag] = child_data
        else:
            result[child.tag] = child.text
    return result


xml_dict = xml_to_dict(root)

# Convert the Python dictionary to JSON
json_data = json.dumps(xml_dict, indent=4)

print(json_data)
