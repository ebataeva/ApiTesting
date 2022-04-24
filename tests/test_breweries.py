import pytest


@pytest.mark.parametrize('city', ['Alameda', 'Miami', 'Sylvania'])
def test_list_parameters_by_city(base_url_breweries, session, city):
    parameter = {'by_city': city}
    r = session.get(base_url_breweries, params=parameter)

    for city_name in r.json():
        assert str(city).lower() in city_name['city'].lower()


@pytest.mark.parametrize('parameter, value', [('city', 'Alameda'), ('by_type', 'regional')])
@pytest.mark.parametrize('second_parameter, second_value', [('by_state', 'California'), ('postal_code', '94501-5047')])
def test_list_pairwaising(base_url_breweries, session, parameter, value, second_parameter, second_value):
    parameter = {f'by_{parameter}': value,
                 f'by_{second_parameter}': second_value}
    r = session.get(base_url_breweries, params=parameter)

    print(r.json())
    assert r.status_code == 200
