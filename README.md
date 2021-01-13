Using Spherical Law of Cosines to find distance between points and fetch customers within a given distance range

Input:
- Given a text file with customer data having name,id,lat,long as json (one user/line)
- office location (lat-long)

Result:
- To Get sorted list of customers who are located within 100km from office using first formula in https://en.wikipedia.org/wiki/Great-circle_distance 

Requirements:
```Python 3x```

Installation:
Dependencies - ``` pip install requirements.txt ```

Execution:
```python main.py ```

File Structure:
- main.py : Main Function that's invoked
- helpers -> 
    utils.py - Utility generic functions
    validators - Validation functions
- resources ->
    constants.py - Constants used across project
    customer.txt - Input file
- src ->
    model.py - Model for customer data
- tests - pytest
- output.txt - Output file
- requirements.txt - Requirements for the project
- Readme.nd - Readme file

