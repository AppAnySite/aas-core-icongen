import json

class ConfigLoader:
    @staticmethod
    def load_config(file_path: str):
        with open(file_path, 'r') as f:
            return json.load(f)
