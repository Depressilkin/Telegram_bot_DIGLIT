class Admin:
    id  = 0
    def __init__(self, token= None):
        self.token = token
        self.tutors = []
        self.students = []
        self.slots = []
    
    def creat_tutor(self, first_name, last_name, theme, token= None):
        id_tutor = f'#t{Admin.id}'
        Admin.id += 1
        tutor = Tutor(id_tutor, first_name, last_name, theme, token)
        return tutor
    
    def del_tutor(self,ID):
        for tutor in self.tutors:
            if tutor.id_tutor.lower() == ID.lower():
                index = self.tutors.index(tutor)
                self.tutors.pop(index)
                del tutor
        return self.tutors

    def creat_student(self,first_name, last_name, theme, token= None):
        id_student = f'#s{Admin.id}'
        Admin.id += 1
        student = Student(id_student, first_name, last_name, theme, token)
        return student
    
    def del_student(self,ID):
        for student in self.students:
            if student.id_student.lower() == ID.lower():
                index = self.students.index(student)
                self.students.pop(index)
                del student
        return self.students

    def add_slot(self,student,tutor, duration, day, time):
        slot = Slot(student,tutor, duration, day, time)
        return slot
        ##добавление в календарь ученика
        #for student in self.students:
        #    if student[0] == ID_student:
        #        student[1].calendary[ID_tutor] = [day,time]
        ##добавление в календарь преподавателя
        #for tutor in self.tutors:
        #    if tutor[1] == ID_tutor:
        #        tutor[2].calendary[ID_student] = [day,time]

    def desplay_calendary(self):
        return self.tutors
    #todo запись в БД учителей и учеников
      
class Tutor:
    def __init__(self, id_tutor, first_name, last_name, theme, token):
        self.id_tutor = id_tutor
        self.first_name = first_name
        self.last_name = last_name
        self.theme = theme
        self.token = token

class Student:
    def __init__(self, id_student, first_name, last_name, theme, token):
        self.id_student = id_student
        self.first_name = first_name
        self.last_name = last_name
        self.theme = []
        self.theme.append(theme)
        self.token = token

class Slot:
    def __init__(self, student, tutor, duration, day, time):
        self.student = student
        self.tutor = tutor
        self.duration = duration
        self.time = time
        self.day = day

with open('C:/Users/silki/Documents/Dev/env.txt','r') as env:
    token_admin = env.read()
admin = Admin(token_admin)