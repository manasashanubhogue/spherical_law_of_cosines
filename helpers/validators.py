import os, json, logging
from src.model import Customer

logger = logging.getLogger(__name__)

class Validators:

    def validate_fields(input_dict, required_fields):
        """
        input_dict: a customer json data
        required_fields: fields that are mandatory in the input
        """
        has_error = False
        error_message = ''
        if set(required_fields) != set(input_dict.keys()):
            has_error = True
            error_message = 'Missing mandatory fields in the file, please check'
        # check if any of the field's value is empty
        if '' in input_dict.values():
            has_error = True
            error_message = 'Value is Empty for one/more keys in the input file, please correct'
        return has_error, error_message

    def validate_customer_data(file_path):
        """ validate file and contents """
        required_fields = ['user_id', 'name', 'latitude', 'longitude']
        all_customers = list()
        if os.path.exists(file_path):
            try:
                with open(file_path) as file:
                    for line in file:
                        # data validation and then append
                        json_line = json.loads(line)
                        has_error, error_message = Validators.validate_fields(json_line, required_fields)
                        # check values of lat and long
                        has_error, error_message = Validators.verify_latitute_longitude(float(json_line['latitude']), float(json_line['longitude']))
                        if has_error:
                            logger.error(error_message)
                            raise ValueError(error_message)
                        all_customers.append(Customer(json_line['user_id'], json_line['name'],
                            (float(json_line['latitude']),float(json_line['longitude'])) ))
            except OSError:
                logger.error("Could not open/read file: {}", file_path)
            logger.debug("File parsed successfully")
            return all_customers

    
    def verify_latitute_longitude(lat, lng):
        """ Validate values of lat and long """
        has_error = False
        error_message = ''
        if lat > 90 or lat < -90:
            has_error = True
            error_message = 'Latitude must have value between -90 to +90'
        if lng > 180 or lng < -180:
            has_error = True
            error_message = 'Longitude must have value between -180 to +180'
        return has_error, error_message
