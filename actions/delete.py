from actions.base_handler import get_instance
from validation import validate_delete_get


def delete_instance(values, entity_type):
    if err := validate_delete_get(values, entity_type):
        return {"error": err, "data": None}
    ID = values.get('ID')
    instance = get_instance(entity_type, ID)
    instance.delete()
    return {"error": None, "data": None}

def get_fields(entity):
    return [('ID', 'IntegerField')]
