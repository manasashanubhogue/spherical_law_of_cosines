import logging
from pprint import pprint
from helpers.validators import Validators
from resources.constants import (
    CUSTOMERS_DATA_PATH,
    DISTANCE_LIMIT_KM,
    INTERCOM_DUBLIN_LATITUDE,
    INTERCOM_DUBLIN_LONGITUDE,
)
from helpers.utils import is_customer_within_range

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def fetch_valid_customers():
    """
    Validate the input file
    And fetch required data
    """
    logger.debug("Function to validate and fetch customer input")
    # validate contents of the file
    all_customers = Validators.validate_customer_data(CUSTOMERS_DATA_PATH)
    office_location = (INTERCOM_DUBLIN_LATITUDE, INTERCOM_DUBLIN_LONGITUDE)
    find_customers_within_distance_range(all_customers, office_location, DISTANCE_LIMIT_KM)


def find_customers_within_distance_range(all_customers, office_location, distance_limit ):
    """ 
    For given list of customers, filter the result to staisy distance limitation
    all_customers: list of customer detail json
    office location: lat-long data
    distance_limit: max distance range allowed
    """
    resultant = dict()
    for customer in all_customers:
        if is_customer_within_range(customer.location, office_location, distance_limit):
            # dict with name and id of customer is stored
            resultant[customer.user_id] = customer.name
    # sort dict based on customer id
    logger.info("Following customers can be invited:\n")
    logger.info(pprint(resultant, sort_dicts=True))
    return resultant

def main():
    fetch_valid_customers()


if __name__ == '__main__':
    main()