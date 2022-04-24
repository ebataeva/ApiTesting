import pytest


def test_url_status(base_url, session, expected_status_code):  
    r = session.get(base_url)
    
    assert str(r.status_code) == expected_status_code 

