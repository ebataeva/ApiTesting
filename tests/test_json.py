import pytest
from tests.support import assert_api_json_schema


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_json_url(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
    assert r.status_code == 200


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_all_resource(base_url_json, session, id):
    r = session.get(f'{base_url_json}/posts/{id}')
    assert r.status_code == 200


def test_get_all_resource_once(base_url_json, session):
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


def test_post(base_url_json, session):
    r = session.post(f'{base_url_json}/posts', data={
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    })
    id = r.json()['userId']
    r2 = session.get(f'{base_url_json}/posts/{id}')
    assert r2.json()['body'] == 'bar'
    assert r.status_code == 201

# def test_post(base_url_breweries, session):
#     pass
