import json

def read(file):
    with open('./db/'+ file +'.json') as json_file:
        results = json.load(json_file)

    return results

def write (file, data):
    with open('./db/'+ file + '.json', 'w') as outfile:
        json.dump(data, outfile, indent = 2)

    return None