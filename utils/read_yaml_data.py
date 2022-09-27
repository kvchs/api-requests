import os
import yaml


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReadYamlFileData:
    @staticmethod
    def load_yaml(file_path):
        try:
            data_file_path = os.path.join(root_path, "data", "yml", file_path)
            with open(data_file_path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print(e)
        else:
            return data


yaml_data = ReadYamlFileData()