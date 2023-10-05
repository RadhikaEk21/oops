class Student:
    def __init__(self, name, math_score, science_score, english_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.english_score = english_score

    def calculate_average_score(self):
        total_score = self.math_score + self.science_score + self.english_score
        average_score = total_score / 3
        return average_score

    def calculate_grade(self):
        average_score = self.calculate_average_score()
        if average_score >= 90:
            return 'A'
        elif 80 <= average_score < 90:
            return 'B'
        elif 70 <= average_score < 80:
            return 'C'
        elif 60 <= average_score < 70:
            return 'D'
        else:
            return 'F'
student1 = Student("ammu", 85, 92, 78)
average_score = student1.calculate_average_score()
grade = student1.calculate_grade()

print(f"Student: {student1.name}")
print(f"Average Score: {average_score}")
print(f"Grade: {grade}")