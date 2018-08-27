"""
Libraries used to store and retrieve data
Uses the json format for simplicity
"""
def store_list(filename,file):
    import json
    with open(filename, 'w') as filehandle:
        json.dump(file, filehandle)

def retreive_list(filename):
    import json
    with open(filename, 'r') as filehandle:
        return json.load(filehandle)
