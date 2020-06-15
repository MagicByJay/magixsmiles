import xmltodict, json, glob

path = 'import_data/'

files = [f for f in glob.glob(path + '*.xml',recursive=True)]

for f in files:
    with open(f) as inFh:
        fname = f.split('.')
        with open('hold_data/' + fname[0].split('/')[1] + '.json','w') as outFh:
            json.dump(xmltodict.parse(inFh.read()), outFh)