import json
from typing import Any, Dict


class Helper:

    @staticmethod
    def get_config_value_by_name(config_file, param_name) -> Any:
        try:
            value = config_file
            for key in param_name:
                value = value[key]
            return value
        except (KeyError, TypeError):
            raise Exception(f"Parameter '{param_name}' not found in the configuration file.")

    @staticmethod
    def load_file(file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, "r") as config_file:
                config_data = json.load(config_file)
                return config_data

        except FileNotFoundError:
            raise Exception(f"Config file not found at {file_path}")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON format in the config file at {file_path}")
