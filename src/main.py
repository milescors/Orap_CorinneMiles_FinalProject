"""
Module Name: Student Grading System
Description: A CLI application for managing student records and grades.
Author: Orap, Corinne Miles
"""

import json
import os

class Student:
   
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else []

    def calculate_average(self):
        """Algorithm: Calculates the GPA of the student."""
        return sum(self.grades) / len(self.grades) if self.grades else 0

class GradeSystem:
   
    def __init__(self, filepath='data/grades.json'):
        self.filepath = filepath
        self.students = self.load_data()

    def load_data(self):
        
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
      
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, s_id, name, grades_str):
       
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
            print("\n[ERROR] Invalid grade format. Please use numbers separated by commas.")

def main():
    
    system = GradeSystem()
    
    while True:
        print("\n===== STUDENT GRADING SYSTEM =====")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            s_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grades = input("Enter Grades (e.g., 85, 90, 88): ")
            system.add_student(s_id, name, grades)
            
        elif choice == '2':
            if not system.students:
                print("\nNo records found.")
            else:
                print("\n--- REGISTERED STUDENTS ---")
                print(f"{'ID':<15} | {'NAME':<20} | {'GPA':<10}")
                print("-" * 50)
                for s_id, info in system.students.items():
                    print(f"{s_id:<15} | {info['name']:<20} | {info['average']:<10.2f}")
                    
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()