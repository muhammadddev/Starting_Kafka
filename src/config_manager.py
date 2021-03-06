import yaml


class ConfigManager:
    @classmethod
    def from_yaml(cls, file_address):
        txt = None
        with open(file_address) as inpfile:
            txt = inpfile.read()
        return cls.from_string(txt)

    @classmethod
    def from_string(cls, txt):
        raw_obj = yaml.load(txt, Loader=yaml.FullLoader)
        ConfigManager.is_yaml_config_valid(raw_obj)
        prj_name = raw_obj["project_name"]
        header = raw_obj["event"]["header"]
        columns = raw_obj["event"]["columns"]
        baked_obj = ConfigManager(prj_name, columns, header)
        return baked_obj

    @classmethod
    def is_yaml_config_valid(cls, raw_obj):
        assert "project_name" in raw_obj
        assert "event" in raw_obj
        event_obj = raw_obj["event"]
        assert "header" in event_obj
        assert "columns" in event_obj
        assert isinstance(event_obj["columns"], list)
        col_obj = event_obj["columns"]
        for column in col_obj:
            assert "name" in column
            assert "type" in column

    def __init__(self, project_name, parsed_obj, header, hdel=","):
        self.project_name = project_name
        self.header_del = hdel
        self.header = header
        self.length_header = None
        self.parsed_obj = parsed_obj
        self.header_map = self.generate_column_map()

    def generate_column_map(self):
        header_index = dict()
        raw = self.header.split(self.header_del)
        self.length_header = len(raw)
        for col in self.parsed_obj:
            h = col["name"]
            if h not in raw:
                print(f"Column {h} was defined in config file but not in header")
            index = raw.index(h)
            header_index[col["name"]] = index
        return header_index

    def get_column_index(self, col):
        if col in self.header_map:
            return self.header_map[col]
        return -1

    def get_header_length(self):
        assert self.length_header is not None
        return self.length_header

    def get_project_name(self):
        return self.project_name

    def get_column_list(self):
        return self.parsed_obj

    def get_value_shape(self):
        value_shape = dict()
        for col in self.parsed_obj:
            value_shape["{}".format(col["name"])] = None
        return value_shape

    def get_key_shape(self):
        key_shape = dict()
        for col in self.parsed_obj:
            if col["role"] == "user_id":
                key_shape["{}".format(col["name"])] = None
        return key_shape
