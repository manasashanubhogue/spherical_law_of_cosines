import json, pytest
from helpers.utils import is_customer_within_range
from helpers.validators import Validators
from resources.constants import (
    CUSTOMERS_DATA_TEST_PATH,
    DISTANCE_LIMIT_KM,
    INTERCOM_DUBLIN_LATITUDE,
    INTERCOM_DUBLIN_LONGITUDE,
)
from src.model import Customer

@pytest.fixture
def customer_data_list():
    return [{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"},
            {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}]

@pytest.fixture
def customer_detail_instance():
    return {
        'name': 'xyz',
        'user_id': 1,
        'location': (52.98, -6.043701)
    }

@pytest.fixture
def customer_invalid_instance():
    return {
        'name': 'Alice',
        'user_id': 2,
        'location': (51.92, -10.043701)
    }

def test_read_input_file(customer_data_list):
    """ Read and compare input file """
    with open(CUSTOMERS_DATA_TEST_PATH) as file:
        for line, exp_line in zip(file, customer_data_list):
            assert json.loads(line) == exp_line


def test_customer_data_struct(customer_detail_instance):
    """ data model verifications """
    customer = Customer(**customer_detail_instance)
    assert customer.name == 'xyz'
    with pytest.raises(TypeError):
        Customer(**{'user_id': 1})
    with pytest.raises(AttributeError):
        customer.latitude

@pytest.mark.parametrize("test_lat, test_lng, expected", 
    [(180, 8, (True, 'Latitude must have value between -90 to +90')), (-8, -90, (False, '')), (-90, 360, (True, 'Longitude must have value between -180 to +180'))])
def test_lat_long_values(test_lat, test_lng, expected):
    """ Verify lat and long values and compare output from function used """
    assert expected == Validators.verify_latitute_longitude(test_lat, test_lng)


def test_valid_distance_range(customer_detail_instance):
    customer = Customer(**customer_detail_instance)
    office_location = (INTERCOM_DUBLIN_LATITUDE, INTERCOM_DUBLIN_LONGITUDE)
    assert True == is_customer_within_range(customer.location, office_location, DISTANCE_LIMIT_KM)

def test_invalid_distance_range(customer_invalid_instance):
    customer = Customer(**customer_invalid_instance)
    office_location = (INTERCOM_DUBLIN_LATITUDE, INTERCOM_DUBLIN_LONGITUDE)
    assert False == is_customer_within_range(customer.location, office_location, DISTANCE_LIMIT_KM)