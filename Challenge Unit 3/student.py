class Student:

   def _init_(self, name, roll_number,  cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list, 
                           key=lambda 
                           student: 
                           student.cgpa, 
                           reverse=True)
  return sorted_students

students = [
  Student("Raja", "A123", 7.8),
  Student("Srikanth", "A125", 8.7),
  Student("Sowmya", "A125", 9.7),
  Student("Mukesh", "A126", 9.9),
]
sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))