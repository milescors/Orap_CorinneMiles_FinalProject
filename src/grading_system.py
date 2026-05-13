import json
import os

class GradeSystem:
    def __init__(self, filepath='data/grades.json'):
        self.filepath = filepath
        self.students = self.load_data()

    def load_data(self):
        """Loads student records from the JSON file."""
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Saves student records to the JSON file, creates folder if missing."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, s_id, name, grades_str):
        """Logic for processing grades and saving a student."""
        try:
           
            clean_grades = [float(g.strip()) for g in grades_str.split(',')]
            
            self.students[s_id] = {
                "name": name,
                "grades": clean_grades,
                "average": round(sum(clean_grades)/len(clean_grades), 2) if clean_grades else 0
            }
            self.save_data()
            print(f"\n[SUCCESS] Record for {name} has been saved!")
        except ValueError:
            print("\n[ERROR] Invalid grade format. Please use numbers separated by commas (e.g. 85, 90).")