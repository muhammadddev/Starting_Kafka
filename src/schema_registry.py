import json


class SchemaRegistry:
    def __init__(self, prj_name, parsed_obj):
        self.prj_name = prj_name
        self.parsed_obj = parsed_obj

    def key_fields(self):
        fields = list()
        for col in self.parsed_obj:
            if col["role"] == "user_id":
                field = dict()
                field["name"] = col["name"]
                field["type"] = col["type"]
                fields.append(field)
        return fields

    def value_fields(self):
        fields = list()
        for col in self.parsed_obj:
            if col["role"] != "action_weight":
                field = dict()
                field["name"] = col["name"]
                field["type"] = col["type"]
                fields.append(field)
        return fields

    def key_schema(self):
        key_schema = dict()
        key_schema["namespace"] = "{}.events".format(self.prj_name)
        key_schema["name"] = "{}_user_events_key".format(self.prj_name)
        key_schema["type"] = "record"
        key_schema["fields"] = self.key_fields()
        return json.dumps(key_schema)

    def value_schema(self):
        value_schema = dict()
        value_schema["namespace"] = "{}.events".format(self.prj_name)
        value_schema["name"] = "{}_user_events_value".format(self.prj_name)
        value_schema["type"] = "record"
        value_schema["fields"] = self.value_fields()
        return json.dumps(value_schema)
