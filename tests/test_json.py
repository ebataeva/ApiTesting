import pytest

from support import assert_api_json_schema


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_json_url(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
    assert r.status_code == 200


@pytest.mark.run_these_please
@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_all_resource(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
    assert r.status_code == 200



def test_get_all_resourc_once(base_url_json, session):
    r = session.get(f'{base_url_json}/posts/')
    assert r.status_code == 200


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_json_url(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
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
    assert_api_json_schema(r, schema)

# def test_post(base_url_breweries, session):
#     pass
