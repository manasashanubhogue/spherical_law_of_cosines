import os, json, logging
from src.customer import Customer

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
                        if has_error:
                            logger.error(error_message)
                            logging.raiseExceptions()
                        all_customers.append(Customer(json_line['user_id'], json_line['name'],
                            (float(json_line['latitude']),float(json_line['longitude'])) ))
            except OSError:
                logger.error("Could not open/read file: {}", file_path)
            logger.debug("File parsed successfully")
            return all_customers