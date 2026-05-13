import json
import os

class Storage:
    FILE_PATH = "data/grades.json"

    @staticmethod
    def load_data():
        if not os.path.exists(Storage.FILE_PATH):
            return []
        with open(Storage.FILE_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        # Siguraduhin na may folder na 'data'
        if not os.path.exists("data"):
            os.makedirs("data")
        with open(Storage.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)