class BaseHandler:
    @staticmethod
    def _get_instance(model, id):
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            return None

    @staticmethod
    def _validate_and_get_instance(model, id):
        if id is None:
            return None, None
        instance = BaseHandler._get_instance(model, id)
        if instance:
            return None, instance
        return f"{model.__name__} ID not found.", None

    @staticmethod
    def get_fields(entity, include_id=False):
        fields = []
        if include_id:
            fields.append(('ID', 'IntegerField'))

        if entity == 'Subject':
            fields.extend([
                ('Title', 'CharField'),
                ('Description', 'TextField')
            ])
        elif entity == 'Teacher':
            fields.extend([
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Position', 'CharField'),
                ('Subject ID', 'IntegerField')
            ])
        elif entity == 'Class':
            fields.extend([
                ('Title', 'CharField'),
                ('Teacher ID', 'IntegerField')
            ])
        elif entity == 'Student':
            fields.extend([
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Class ID', 'IntegerField')
            ])
        elif entity == "Grade":
            fields.extend([
                ('Value', 'TextField'),
                ('Date', 'DateField'),
                ('Student ID', 'IntegerField'),
                ('Subject ID', 'IntegerField')
            ])
        elif entity == "Schedule":
            fields.extend([
                ('Week day', 'TextField'),
                ('Start time', 'TimeField'),
                ('Subject ID', 'IntegerField'),
                ('Class ID', 'IntegerField'),
                ('Teacher ID', 'IntegerField')
            ])
        return fields
