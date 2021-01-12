from math import acos, cos, radians, sin
from resources.constants import EARTH_RADIUS

def get_distance_between_points_on_sphere(customer_location, office_location):
    """
    Convert given locations into radians and based on spherical law of cosines, distance from customer
    location and office location is calculated
    customer_location: lat-long data of customer
    office location: lat-long data of office
    """
    dlon = radians(customer_location[1] - office_location[1])
    lat1 = radians(office_location[0])
    lat2 = radians(customer_location[0])

    a = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = acos(a)
    customers_distance = EARTH_RADIUS * c
    return customers_distance

def is_customer_within_range(customer_location, office_location, distance_limit):
    """
    Returns True/false based on whether location is less than limit
    customer_location: lat-long data of customer
    office location: lat-long data of office
    distance_limit: max distance range allowed
    """
    customer_distance = get_distance_between_points_on_sphere(customer_location, office_location)
    return customer_distance < distance_limit
