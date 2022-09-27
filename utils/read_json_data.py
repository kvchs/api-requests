import os
import json


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReadJsonFileData:
    @staticmethod
    def load_json(file_path):
        try:
            data_file_path = os.path.join(root_path, "data", "json", file_path)
            with open(data_file_path, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        else:
            return data


json_data = ReadJsonFileData()