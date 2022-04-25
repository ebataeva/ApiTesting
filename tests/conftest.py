import pytest
import requests
import functools


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is the request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Expected status code"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")



@pytest.fixture
def base_url_dogs():
    return 'https://dog.ceo/api/'


@pytest.fixture
def base_url_breweries():
    return 'https://api.openbrewerydb.org/breweries'


@pytest.fixture
def base_url_json():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture(scope='module')
def session():
    s = requests.Session()
    s.request = functools.partial(s.request, timeout=30)
    return s
