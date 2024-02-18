from actions.base_handler import get_instance, type_model, field_model
from actions.base_handler import get_fields as fields
from actions.validation import validate_creating


def entity(values, entity_type):
    if err := validate_creating(values, entity_type):
        return {"error": err, "data": None}

    model = type_model.get(entity_type)
    instance_values = {}

    for field, _ in fields(entity_type):
        value = values.get(field)
        if field := field_model.get(field):
            instance_values[field] = int(value) if field == "birth_year" else value

    if entity_type in ["schedule", "class"]:
        teacher = get_instance("teacher", values.get("Teacher ID"))
        instance_values['teacher'] = teacher
    if entity_type in ["grade", "schedule"]:
        subject = get_instance("subject", values.get('Subject ID'))
        instance_values['subject'] = subject
    if entity_type in ["schedule", "student"]:
        study_class = get_instance("class", values.get('Class ID'))
        instance_values['study_class'] = study_class
    if entity_type == "grade":
        student = get_instance("student", values.get('Student ID'))
        instance_values['student'] = student
    
    instance = model(**instance_values)
    instance.save()

    if entity_type == "teacher":
        subject = get_instance("subject", values.get("Subject ID"))
        subject.teacher_set.add(instance)

    return {"error": None, "data": None}

def get_fields(entity_type):
    return fields(entity_type)