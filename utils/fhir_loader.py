import json

def load_fhir_resource(path):
    with open(path, 'r') as file:
        return json.load(file)