import pytest
from support import test_api_json_schema


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_json_url(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
    assert r.status_code == 200


def test_valid_body_url(base_url_json, session):
    r = session.get(f'{base_url_json}/posts/1')
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "title": {
                "type": "string"
            },
            "body": {
                "type": "string"
            },
            "userId": {
                "type": "integer"
            }
        },
        "required": [
            "id",
            "title",
            "body",
            "userId"
        ]
    }
    assert r.status_code == 200
    test_api_json_schema(r.json(), schema)
