class Student:
    def __init__(self, name , age ,rollNumber ,class_name , section: str = "", marks_dict: dict[str, int] ={}, ):
        self.name = name 
        self.age = age 
        self.rollNumber = rollNumber
        self.class_name = class_name
        self.section = section
        self.marks_dict = marks_dict

    def calculate_total_marks(self):
        marks_list = self.marks_dict.values()
        total_marks = sum(marks_list)
        print(f"Total Marks: {total_marks}")
        return total_marks
    
    def calculate_average_marks(self):
        total_marks = self.calculate_total_marks()
        print(f"Total Markshfb: {total_marks}")
        print(f"{len(self.marks_dict)}")
        average_marks = (total_marks) / len(self.marks_dict)
        print(f"Average Marks: {average_marks}")
        return average_marks
    
    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.rollNumber}")        
    
    def calculate_percentage(self):
        total_marks = self.calculate_total_marks()
        
        total_possible_marks = len(self.marks_dict) * 100
        print(f"Percentage: {total_marks / total_possible_marks * 100}")
        return total_marks / total_possible_marks * 100
    
    def display_grade(self):
        percentage = self.calculate_percentage()
        
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"Grade: {grade}")    



student1 = Student ("John Doe", 16, 23, '10Th', 'A', marks_dict={
    'physics':20,
    'chemistry':30,
    'maths':    90
})
    
student1.display_student_info()
student1.calculate_total_marks()
student1.calculate_average_marks()
student1.calculate_percentage()
student1.display_grade()        

