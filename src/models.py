class Student:
    def __init__(self, student_id, name, math, science, english):
        self.student_id = student_id
        self.name = name
        self.math = float(math)
        self.science = float(science)
        self.english = float(english)
        self.average = (self.math + self.science + self.english) / 3

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "math": self.math,
            "science": self.science,
            "english": self.english,
            "average": round(self.average, 2)
        }