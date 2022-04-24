import json
from support import assert_valid_schema, HOUND, BULLDOGS
import pytest


def test_get_list_all(base_url_dogs, session):
    r =session.get(f'{base_url_dogs}breeds/list/all')
    
    assert r.status_code == 200
    assert_valid_schema(r.json(), 'schema.json')


@pytest.mark.parametrize('breed_name', ['newfoundland', 'papillon', 'pug'])
def test_breed_list(base_url_dogs, session, breed_name):
    r = session.get(f'{base_url_dogs}breed/{breed_name}/images/random')
    
    assert r.status_code == 200
    assert r.json()['status'] == 'success'


@pytest.mark.parametrize('breed_name', ['asian', 'transoformer', 'pig'])
def test_breed_list_negative(base_url_dogs, session, breed_name):
    r = session.get(f'{base_url_dogs}breed/{breed_name}/images/random')

    assert r.status_code == 404
    assert r.json()['status'] == 'error'


def test_random_image(base_url_dogs, session):
    r = session.get(f'{base_url_dogs}breeds/image/random')

    image_link = r.json()['message']
    
    assert r.status_code == 200
    
    r2 = session.get(f'{base_url_dogs}breeds/image/random')
    
    assert r2.status_code == 200
    assert r2.json()['message'] != image_link


@pytest.mark.parametrize('breed, breeders', [(HOUND, 'hound'), (BULLDOGS, "bulldog")])
def test_sub_breed(base_url_dogs, session, breed, breeders):
    r = session.get(f'{base_url_dogs}breed/{breeders}/list')

    assert r.status_code == 200
    assert r.json()['message'] == breed
