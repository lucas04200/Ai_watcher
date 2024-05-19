import json
import os
from datetime import datetime


class DataManager:
    def __init__(self, video_name, results=None):
        self.video_name = video_name
        self.results = results

        base_path = os.path.join("data/output", self.video_name)
        self.frames_folder = os.path.join(base_path, "frames")
        self.results_folder = os.path.join(base_path, "results")

        os.makedirs(self.frames_folder, exist_ok=True)
        os.makedirs(self.results_folder, exist_ok=True)

    def save_data(self):
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
        file_path = os.path.join(self.results_folder, filename)

        with open(file_path, 'w') as file:
            json.dump(self.results, file, indent=4)

    def load_data(self, filename):
        file_path = os.path.join(self.results_folder, filename)

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.results = json.load(file)
                return self.results
        else:
            raise FileNotFoundError(f"Le fichier '{filename}' n'existe pas dans le dossier des résultats.")
