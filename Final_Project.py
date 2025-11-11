#function to add a new student
def add_student():
    info = []
    while True:
        userInput = input("Enter Student ID: ")
        if len(userInput) == 8 and userInput.isdigit():
            info.append(userInput)
            break
        else:
            print("Error: Invalid format")
    while True:
        userInput = input("Enter Student Name: ")
        if any(i.isdigit() for i in userInput):
            print("Error: No numbers allowed")
            continue
        info.append(userInput)
        break
    while True:
        userInput = input("Enter Student Email: ")
        if not userInput.endswith("@imail.sunway.edu.my") or userInput[0] == '@':
            print("Error: must end with @imail.sunway.edu.my")
            continue
        info.append(userInput)
        break
    studentLine = ",".join(info)
    with open("students.txt", "a") as a:
        a.write(studentLine)
        a.write('\n')
    print("\nAction successful!\n--------------------")

#function to add a new course
def add_course():
    info = []
    while True:
        userInput = input("Enter Course ID: ")
        if len(userInput) == 7 and userInput[0:2].isalpha() and userInput[3:6].isdigit():
            info.append(userInput.upper())
            break
        else:
            print("Error: Invalid format")
    while True:
        userInput = input("Enter Course Name: ")
        if any(i.isdigit() for i in userInput):
            print("Error: No numbers allowed")
            continue
        info.append(userInput)
        break
    courseLine = ",".join(info)
    with open("courses.txt", "a") as a:
        a.write(courseLine)
        a.write('\n')
    print("\nAction successful!\n--------------------")

# funciton to return recorded students in dict form
def load_students():
    students = {}
    with open("students.txt", "r") as s:
        for line in s:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                # make sure the line has at east 3 parts (prevent empty lines or incomplete record) 
                # only then assign id,name accordingly
                student_id = parts[0]
                name = parts[1]
                students[student_id] = name
    return students


#function to return recorded courses in dict form
def load_courses():
    courses = {}
    with open("courses.txt","r") as c:
        for line in c:
            parts = line.strip().split(",")
            if len(parts) >=2:
                course_id = parts[0]
                course_name = parts[1]
                courses[course_id] =course_name
    return courses


#function to record the results
def record():
    info = []
    students = load_students()
    if not students:
        # if there is no recorded student, stop function early
        print("Error: No student found. Please add a student first.")
        return
    print("Available students:")
    for student_id, name in students.items():
        print(f"{student_id} - {name}")
    while True:
        userInput = input("Enter Student ID: ")
        if userInput in students:
            print(f"Student found: {students[userInput]}")
            info.append(userInput)
            break
        else:
            print("Error: Student not found")
            continue
    courses = load_courses()
    if not courses:
        # if there is no recorded course, stop function early
        print("Error: No course found. Please add a course first.")
        return
    print("Available courses:")
    for course_id, course_name in courses.items():
        print(f"{course_id} - {course_name}")
    while True:
        userInput = input("Enter Course ID: ")
        if userInput in courses:
            print(f"Courses found: {courses[userInput]}")
            info.append(courses[userInput])
            break
        else:
            print("Error: Course not found")
            continue
    while True:
        try:
            userInput=float(input("Enter marks(%): "))
            if userInput<0 or userInput>100:
                print("Error: Invalid range")
                continue
            info.append(str(f"{userInput:.2f}%"))
            if userInput >= 80:
                grade='A+'
            elif userInput >= 75:
                grade='A'
            elif userInput >= 70:
                grade='A-'
            elif userInput >= 65:
                grade='B+'
            elif userInput >= 60:
                grade='B'
            elif userInput >= 55:
                grade='B-'
            elif userInput >= 50:
                grade='C'
            elif userInput >= 45:
                grade='C-'
            elif userInput >= 40:
                grade='D'
            else:
                grade='F'
            info.append(grade)
            break
        except:
            print("Error: Only numbers allowed")
    gradeLine = ",".join(info)
    with open("grades.txt", "a") as a:
        a.write(gradeLine)
        a.write('\n')
    print("\nAction successful!\n--------------------")


#function to show the options
def print_option():
        print("> 1 Add a new student")
        print("> 2 Add a new course")
        print("> 3 Record student marks")
        print("> 4 Display individual student performance")
        print("> 5 Display course performance summary")
        print("> 6 Export performance report")
        print("> 0 Exit")


#function to check if the files exist
def parse_files():
    try:
        with open("students.txt") as a:
            pass
        with open("grades.txt") as b:
            pass
        with open("courses.txt") as c:
            pass

    except FileNotFoundError:
        print("Error: Unable to open files")
        exit()

def main():
    print("Welcome to the Ultimate Python-Powered Student Grading System!")
    parse_files()
    while True:
        print_option()
        userInput = input("Please select an action: ")
        match userInput:
            case '1':
                add_student()
            case '2':
                add_course()
            case '3':
                record()
            case '4':
                print("4")
            case '5':
                print("5")
            case '6':
                print("6")
            case '0':
                print("Exiting program...")
                break
            case _ :
                print("Invalid option!")


if __name__ == "__main__":
    main()