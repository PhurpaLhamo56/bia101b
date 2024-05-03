class Person:
    # assigning attributes
    def __init__(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid

    # defining behaviours/ methods
    def walk(self):
        print(self.name, "is walking")

    def talk(self):
        print(self,name, "is talking")

    def sleep(self):
        print(self.name, "is sleeping")

    def eat(self):
        print(self.name, "is eating")    

class Teacher(Person):
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super(). __init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(self.name, "is teaching")

    def grade_student(self):
        print(self,name, "is grading")

    def attend_meeting(self):
        print(self.name, "is attend meeting")

class student (Person):
        #attributes
    def __init__(self, name, age, cid, std_id, course, year, gpa):
            super(). __init__(name, age, cid)      
            self.std_id = std_id
            self.course = course
            self.year = year
            self.gpa = gpa

    def study(self):
            print(self.name, "is studying")

    def attend_class(self):
            print(self,name, "is attending class")

    def write_exam(self):
            print(self.name, "is writing exam")

t1 = Teacher("Tashi", 30, 2003, "phy", 4500, "science", "assisstant")
t2 = Teacher("phurpa", 23, 2000, "bio", 2500, "science", "full teacher")

s1 = student("penjor", 30, 200333, 450000, "bbi", 1, 2)
s2 = student("sonam", 20, 200345, 55000, "bbi", 1, 3.5)

if s1.gpa > s2.gpa:
    print(s1.name, "is better than", s2.name)
    student_information = "year: " + str(s1.year) + " course: " + s1.course
    print(student_information)

else: 
    print(s2.name, "is better than", s1.name)
    student_information = "year: " + str(s2.year) + " course: " + s2.course
    print(student_information)

student_storage = [s1, s2] 

for std in student_storage:
    print(std.name)
    print(std.gpa)
    print(std.course)
    print('========')


    

