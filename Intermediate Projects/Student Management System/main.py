import json
import os

class Student:
    def __init__(self, name, roll, sub_mid_marks, sub_end_marks, sub_other_marks, assignment_marks, atten_percentage,attedn_marks,total_marks):
        self.name = name
        self.roll = roll
        self.mid_marks = sub_mid_marks
        self.end_marks = sub_end_marks
        self.other_marks = sub_other_marks
        self.ass_marks = assignment_marks
        self.atd_percentage = atten_percentage
        self.attend_marks= attedn_marks
        self.total_marks= total_marks

    def display(self):
        print("\n")
        print("Name: ", self.name)
        print("Roll No.: ", self.roll)
        print("\n")
        print("Marks Scored in Mid Sem:")
        for subject, marks in self.mid_marks.items():
            print(subject, ":", marks)
        print("\n")
        print("Marks Scored in End Sem:")
        for subject, marks in self.end_marks.items():
            print(subject, ":", marks)
        print("\n")
        print("Marks Scored in Case study and Quiz:")
        for subject, marks in self.other_marks.items():
            print(subject, ":", marks)
        print("\n")
        print("Marks for assignment:")
        for subject, marks in self.ass_marks.items():
            print(subject, ":", marks)
        print("\n")
        print("Attendance Percentage in Following Subjects:")
        for subject, att in self.atd_percentage.items():
            print(subject, ":", att, "%")
        print("\n")
        print("Total Marks Scored Out of 100 :")
        for subject, marks in self.total_marks.items():
            print(subject, ":", marks)
        print("\n")

class Teacher:
    def __init__(self, name, ID):
        self.name = name
        self.id = ID

def add_student():
    name = input("Enter the student's name: ")
    roll = int(input("Enter the Roll Number of the student: "))
    subject_mid_mar = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_end_mar = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_other_mar = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_addent_percen = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_ass_marks = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_att_marks = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}
    subject_total_marks = {"DAA": None, "DCCN": None, "DMGT": None, "UHV": None, "GCHEM": None}

    print("Mid Sem Marks Entry: \n")
    print("Enter out of 20 ")
    for subject in subject_mid_mar.keys():
        mark = int(input(f"Enter marks for {subject}:"))
        subject_mid_mar[subject] = mark
    print("\n")

    print("End Sem Marks Entry: \n")
    print("Enter out of 100 ")
    for subject in subject_end_mar.keys():
        mark = int(input(f"Enter marks for {subject}:"))
        subject_end_mar[subject] = mark
    print("\n")

    print("Case Study and Quiz Marks Entry: \n")
    print("Enter out of 20 ")
    for subject in subject_other_mar.keys():
        mark = int(input(f"Enter marks for {subject}:"))
        subject_other_mar[subject] = mark
    print("\n")

    print("Attendance Percentage: \n")
    print("Enter out of 100 ")
    for subject in subject_addent_percen.keys():
        atp= int(input(f"Enter percentage of classes attended for {subject}:"))
        if atp>=95 and atp<=100:
            subject_att_marks[subject]=10
        elif atp>=85 and atp<95:
            subject_att_marks[subject]=9
        elif atp>=75 and atp<85:
            subject_att_marks[subject]=8
        elif atp<75:
            subject_att_marks[subject]=7

        subject_addent_percen[subject] = atp
    print("\n")

    print("Assignments Marks: \n")
    print("Enter out of 10 ")
    for subject in subject_ass_marks.keys():
        mark = int(input(f"Enter marks for {subject}:"))
        subject_ass_marks[subject] = mark
    
    for subject in subject_total_marks:
        total_mark=subject_mid_mar[subject]+subject_other_mar[subject]+(subject_end_mar[subject]/100)*40+subject_att_marks[subject]+subject_ass_marks[subject]
        subject_total_marks[subject]=total_mark

    a = Student(name, roll, subject_mid_mar, subject_end_mar, subject_other_mar, subject_ass_marks, subject_addent_percen,subject_att_marks,subject_total_marks)
    return a

def save_students_data(students):
    student_data = []
    for student in students:
        student_data.append({
            'Name': student.name,
            'Roll No.': student.roll,
            'Mid Sem Marks': student.mid_marks,
            'End Sem Marks': student.end_marks,
            'Quiz+Case Study Marks': student.other_marks,
            'Assignment Marks': student.ass_marks,
            'Attendence Percentage': student.atd_percentage,
            'Attendence Marks': student.attend_marks,
            'Total Marks': student.total_marks
        })
    with open('s1.json', 'w') as file:
        json.dump(student_data, file, indent=4)

def edit_marks():
    
    if not studentobj:
        print("No students added yet.")
    else:
        student_checkname = input("Enter the name of The Student: ")
        student_checkroll = int(input("Enter the roll no. of The Student: "))
        student_found = False
        for i in studentobj:
            if i.name == student_checkname and i.roll==student_checkroll:
                student_sub=input("Enter the subject for editing:")
                choice=int(input("Enter Your Choice:\n1.Mid sem\n2.End Sem\n3.Case Study and Quiz\n4.Assignment\n5.Attendence Marks\n"))

                if choice==1:
                    mark=int(input("Enter the New Mid Sem Mark: "))
                    temp=i.mid_marks[student_sub]
                    i.mid_marks[student_sub]=mark
                    total=i.total_marks[student_sub]
                    i.total_marks[student_sub]=(total-temp)+mark
                    print("Mid Sem Marks Updated for ",student_sub," of ",student_checkname,"!")

                elif choice==2: 
                    mark=int(input("Enter the New End Sem Mark: "))
                    temp=i.end_marks[student_sub]
                    i.end_marks[student_sub]=mark
                    total=i.total_marks[student_sub]
                    i.total_marks[student_sub]=(total-temp)+mark
                    print("End Sem Marks Updated for ",student_sub," of ",student_checkname,"!")
                
                elif choice==3:
                    mark=int(input("Enter the New Case Study and Quiz Mark: "))
                    temp=i.other_marks[student_sub]
                    i.other_marks[student_sub]=mark
                    total=i.total_marks[student_sub]
                    i.total_marks[student_sub]=(total-temp)+mark
                    print("Case Study and Quiz Marks Updated for ",student_sub," of ",student_checkname,"!")
                
                elif choice==4:
                    mark=int(input("Enter the New Assignment Mark: "))
                    temp=i.ass_marks[student_sub]
                    i.ass_marks[student_sub]=mark
                    total=i.total_marks[student_sub]
                    i.total_marks[student_sub]=(total-temp)+mark
                    print("Assignment Marks Updated for ",student_sub," of ",student_checkname,"!")
                
                elif choice==5:
                    mark=int(input("Enter the New Attendence Mark: "))
                    temp=i.attend_marks[student_sub]
                    i.attend_marks[student_sub]=mark
                    total=i.total_marks[student_sub]
                    i.total_marks[student_sub]=(total-temp)+mark
                    print("Attendence Marks Updated for ",student_sub," of ",student_checkname,"!")

                student_found = True
                break
        if not student_found:
            print("No such student exists\n")

def calculate_sgpa(self):
        total_credits = 4
        total_points = 0

        for subject in self.mid_marks.keys():
           
            mid_weighted = (self.mid_marks[subject] / 20) * 0.2 
            end_weighted = (self.end_marks[subject] / 100) * 0.6  
            quiz_weighted = (self.quiz_marks[subject] / 20) * 0.1  
            case_study_weighted = (self.case_study_marks[subject] / 20) * 0.1
            assign_weighted = (self.ass_marks[subject] / 10) * 0.1  
            attend_weighted = (self.attend_marks[subject] / 10) * 0.1  

            
            subject_points = mid_weighted + end_weighted + quiz_weighted + assign_weighted + attend_weighted
            total_points += subject_points
            

        sgpa = total_points / total_credits
        return round(sgpa * 10, 2)  # Scaling SGPA to 10-point grading scale
def load_from_student_data():
    students = []

    if not os.path.exists('s1.json'):
        print("No Students data found. Starting fresh.")
        return students    

    try:
        with open('s1.json', 'r') as file:
            student_data = json.load(file)
            for sdata in student_data:
                student = Student(
                    sdata['Name'], 
                    sdata['Roll No.'], 
                    sdata['Mid Sem Marks'], 
                    sdata['End Sem Marks'],
                    sdata['Quiz+Case Study Marks'],
                    sdata['Assignment Marks'],
                    sdata['Attendence Percentage'],
                    sdata['Attendence Marks'],
                    sdata['Total Marks']
                )
                students.append(student)
    except FileNotFoundError:
        print("No Students data found")
    return students 

studentobj = load_from_student_data()
teacherobj = [Teacher("Rupesh", 123), Teacher("Mamta", 321)]
while True:

    print("\n\nLogin As : ")
    print("\n1. Teacher \n2. Student \n3. Exit")
    login = int(input("Enter Choice: "))

    if login == 1:
        tname = input("Enter Your Name : ")
        tId = int(input("Enter Your ID : "))
        teacher_found = False
        for i in teacherobj:
            if tname.strip().lower() == i.name.strip().lower() and tId == i.id:
                teacher_found = True
                print("Welcome ", tname, " !!")
                while True:
                    print("\n1. Add a Student")
                    print("2. Check Marks")
                    print("3. Edit Marks")
                    print("4. Exit\n")

                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        a = add_student()
                        studentobj.append(a)
                        print(a.name, " Added Successfully")
                        save_students_data(studentobj)
                    elif choice == 2:
                        if not studentobj:
                            print("No students added yet.")
                        else:
                            student_checkname = input("Enter the name of The Student: ").strip().lower()
                            student_found = False
                            for i in studentobj:
                                if student_checkname == i.name.strip().lower():
                                    i.display()
                                    student_found = True
                                    break
                            if not student_found:
                                print("No such student exists\n")    
                    elif choice == 3:
                        edit_marks()
                    elif choice == 4:
                        print("Exiting the program...")
                        break 
                    else:
                        print("Invalid choice. Please try again.")
                    user_input = input("Want to continue (Y/N): ")
                    if user_input.lower() == 'n':
                        print("Thank you!!")
                        break
        if not teacher_found:
            print("Invalid Credentials")

    elif login == 2:
        sname = input("Enter Your Name : ")
        sId = int(input("Enter Your Roll No : "))
        student_found1 = False
        for i in studentobj:
            if sname.strip().lower() == i.name.strip().lower() and sId == i.roll:
                student_found1 = True
                print("Welcome ", sname, " !!")
                while True:
                    print("1. Show Results")
                    print("2. Show CGPA")
                    print("3. Exit")

                    choice2 = int(input("Enter your choice: "))

                    if choice2 == 1:
                        i.display()
                    elif choice2 == 2:
                        print("CGPA not available yet.")
                    elif choice2 == 3:
                        print("Exiting the program...")
                        break 
                    else:
                        print("Invalid choice. Please try again.")
                    user_input = input("Want to continue (Y/N): ")
                    if user_input.lower() == 'n':
                        print("Thank you!!")
                        break
        if not student_found1:
            print("Invalid Credentials")

    elif login == 3:
        print("Thankew!")
        break
    else:
        print("Wrong Choice!")
