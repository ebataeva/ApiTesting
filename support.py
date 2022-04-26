from jsonschema import validate
import os
import json

script = ' .\apitesting\venv\Scripts\activate'

DIRPATH = os.path.abspath(os.path.dirname(__file__))
HOUND = [
    "afghan",
    "basset",
    "blood",
    "english",
    "ibizan",
    "plott",
    "walker"
]
BULLDOGS = [
    "boston",
    "english",
    "french"
]


def assert_valid_schema(data, schema_file):
    with open(DIRPATH + '/' + schema_file, encoding='utf-8') as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def assert_api_json_schema(request, schema):
    return validate(instance=request.json(), schema=schema)
