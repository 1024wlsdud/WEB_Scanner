import json

def read_setting(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        for key in data.keys():
            print(key,data[key])
        return data
