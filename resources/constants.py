import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


DISTANCE_LIMIT_KM = 100
EARTH_RADIUS = 6371
INTERCOM_DUBLIN_LATITUDE = 53.339428
INTERCOM_DUBLIN_LONGITUDE = -6.257664
CUSTOMERS_DATA_PATH = os.path.join(dir_path, "customers.txt")

CUSTOMERS_DATA_TEST_PATH = os.path.join(dir_path, "test_input.txt")