import json

def read(file):
    with open('../db/'+ file +'.py') as json_file:  
        results = json.load(json_file)
        



    # for p in data['people']:
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print(''s)