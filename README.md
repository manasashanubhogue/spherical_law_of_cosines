Using Spherical Law of Cosines to find distance between points and fetch customers within a given distance range

Input:
- Given a text file with customer data having name,id,lat,long as json (one user/line)
- office location (lat-long)

Result:
- To Get sorted list of customers who are located within 100km from office using first formula in https://en.wikipedia.org/wiki/Great-circle_distance 

Requirements:
Python 3x, pip and virtualenv to be installed.

Install virtualenv globally using pip3 with pip3 install virtualenv.
Create a virtualenv named ".venv" with virtualenv .venv.
Activate the virtualenv with . .venv/bin/activate.
Install dependencies with pip3 install -r requirements.txt.

Installation:
1. Install virtualenv - ```pip install virutalenv```
2. Create virtualenv - ``` virtualenv .venv```
3. Activate - ``` source .venv/Scripts/activate ```
4. Install dependencies ``` pip install -r requirements.txt ```

Execution:
```python main.py ```

TestCases execution:
``` pytest ```

File Structure:
- main.py : Main Function
- helpers -> 
    utils.py - Utility generic functions
    validators - Validation functions
- resources ->
    constants.py - Constants used across project
    customer.txt - Input file
- src ->
    model.py - Model for customer data
- tests - Test cases for the project
- output.txt - Output file
- requirements.txt - Requirements for the project
- Readme.md - Readme file

