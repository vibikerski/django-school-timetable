from actions.base_handler import type_model
from datetime import date, datetime


def is_valid_date_format(date_text):
    try:
        date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

def is_valid_time(time_text):
    try:
        datetime.strptime(time_text, "%H:%M")
        return True
    except ValueError:
        return False

def is_digit_and_positive(value):
    return value.isdigit() and int(value) >= 0

def is_not_too_long(value, max_length):
    return len(value) <= max_length

def validate_ID(value, entity_type): 
    if value is None:
        return False
    if not is_digit_and_positive(value):
        return False

    try:
        model = type_model.get(entity_type)
        model.objects.get(id=value)
        return True
    except model.DoesNotExist:
        return False

def contains(val1, val2):
    return val1 in val2

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

validations = {
     "subject": [
        ("Title", is_not_too_long, 100),
        ("Description", None)],
    "class": [
        ("Title", is_not_too_long, 100),
        ("Teacher ID", validate_ID, "teacher")],
    "teacher": [
        ("Birth Year", is_digit_and_positive),
        ("Name", is_not_too_long, 100),
        ("Surname", is_not_too_long, 100),
        ("Position", is_not_too_long, 150),
        ("Subject ID", validate_ID, "subject")
    ],
    "student": [
        ("Birth Year", is_digit_and_positive),
        ("Name", is_not_too_long, 100),
        ("Surname", is_not_too_long, 100),
        ("Class ID", validate_ID, "class")
    ],
    "grade": [
        ("Value", is_digit_and_positive),
        ("Date", is_valid_date_format),
        ("Student ID", validate_ID, "student"),
        ("Subject ID", validate_ID, "subject")
    ],
    "schedule": [
        ("Week day", contains, week_days),
        ("Start time", is_valid_time),
        ("Subject ID", validate_ID, "subject"),
        ("Class ID", validate_ID, "class"),
        ("Teacher ID", validate_ID, "teacher"),
    ],
}

def validate_creating(values, entity_type):
    for field, validator, *args in validations.get(entity_type, []):
        value = values.get(field)
        if value is None:
            return f"{field} is missing."
        if validator and not validator(value, *args):
            return f"{field} is unprocessable."

    return None

def validate_updating(values, entity_type):
    ID = values.get('ID')
    if not validate_ID(ID, entity_type):
        return "Entity does not exist."
    for field, validator, *args in validations.get(entity_type, []):
        if not values.get(field):
            continue
        
        value = values.get(field)
        if validator and not validator(value, *args):
            return f"{field} is unprocessable."
    
    return None

def validate_delete_get(values, entity_type):
    ID = values.get('ID')
    return None if validate_ID(ID, entity_type) else "Entity does not exist."