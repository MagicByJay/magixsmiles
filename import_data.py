import xmltodict, json

with open('test.xml') as inFh:
    with open('sample.json','w') as outFh:
        json.dump(xmltodict.parse(inFh.read()), outFh)