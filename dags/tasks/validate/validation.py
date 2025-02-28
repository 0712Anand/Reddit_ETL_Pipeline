import sys
import datetime

def validate_input(input_date):
    """provide validation of the input"""
    try:
        datetime.datetime.strptime(input_date,'%Y%m%d')
    except ValueError:
        raise ValueError("INput parameter should be %YYYY-%MM-%DD")
        sys.exit(1)