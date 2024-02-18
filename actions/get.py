from actions.base_handler import get_instance as get
from validation import validate_delete_get


def get_instance(values, entity_type):
    if err := validate_delete_get(values, entity_type):
        return {"error": err, "data": None}
    ID = values.get('ID')
    instance = get(entity_type, ID)
    return {"error": None, "data": instance}

def get_fields(entity):
    return [('ID', 'IntegerField')]
