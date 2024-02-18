from actions.base_handler import get_instance, field_model
from actions.base_handler import get_fields as fields
from validation import validate_updating

def proccess_fields(values, entity_type):
    instance_values = {}
    for field, _ in fields(entity_type):
        if not values.get(field):
            continue
        value = values.get(field)
        if field := field_model.get(field):
            if field in ["birth_year", "value"]:
                value = int(value)
            instance_values[field] = value

    if teacher_id := values.get('Teacher ID'):
        instance_values['teacher'] = get_instance("teacher", teacher_id)
    if subject_id := values.get('Subject ID') and entity_type != "teacher":
        instance_values['subject'] = get_instance("subject", subject_id)
    if class_id := values.get('Class ID'):
        instance_values['study_class'] = get_instance("class", class_id)
    if student_id := values.get('Student ID'):
        instance_values['student'] = get_instance("student", student_id)

    return instance_values

def update_entity(values, entity_type):
    if err := validate_updating(values, entity_type):
        return {"error": err, "data": None}

    entity = get_instance(entity_type, values.get('ID'))
    instance_values = proccess_fields(values, entity_type)

    for attr_name, value in instance_values.items():
        setattr(entity, attr_name, value)

    entity.save()
    if subject_id := values.get('Subject ID') and entity_type == "teacher":
        subject = get_instance("subject", subject_id)
        subject.teacher_set.add(entity)

    return {"error": None, "data": None}

def get_fields(entity):
    return fields(entity, True)
