

class Report:
    def __init__(self, report_id=None, lesson_id=None, student_id=None, grade=None):
        self.report_id = report_id
        self.lesson_id = lesson_id
        self.student_id = student_id
        self.grade = grade

    def __del__(self):
        print("Report object destroyed")

class Poster:
    def __init__(self, poster_id=None, lesson_id=None, title=None, description=None):
        self.poster_id = poster_id
        self.lesson_id = lesson_id
        self.title = title
        self.description = description

    def __del__(self):
        print("Poster object destroyed")

class Curriculum:
    def __init__(self, curriculum_id=None, subject_id=None, title=None, description=None):
        self.curriculum_id = curriculum_id
        self.subject_id = subject_id
        self.title = title
        self.description = description

    def __del__(self):
        print("Curriculum object destroyed")

class Subject:
    def __init__(self, subject_id=None, name=None, description=None):
        self.subject_id = subject_id
        self.name = name
        self.description = description

    def __del__(self):
        print("Subject object destroyed")

class Material:
    def __init__(self, material_id=None, name=None, description=None):
        self.material_id = material_id
        self.name = name
        self.description = description

    def __del__(self):
        print("Material object destroyed")

class Page:
    def __init__(self, page_id=None, prerequisite_id=None, material_id=None, title=None, content=None):
        self.page_id = page_id
        self.prerequisite_id = prerequisite_id
        self.material_id = material_id
        self.title = title
        self.content = content

    def __del__(self):
        print("Page object destroyed")

class Lesson:
    def __init__(self, lesson_id=None, page_id=None, student_id_list=None, title=None, description=None, date=None, time=None):
        self.lesson_id = lesson_id
        self.page_id = page_id
        self.student_id_list = student_id_list
        self.title = title
        self.description = description
        self.date = date
        self.time = time

    def __del__(self):
        print("Lesson object destroyed")

class Prerequisite:
    def __init__(self, prerequisite_id=None, page_id=None, page_id_list=None):
        self.prerequisite_id = prerequisite_id
        self.page_id = page_id
        self.page_id_list = page_id_list

    def __del__(self):
        print("Prerequisite object destroyed")

class Administrator:
    def __init__(self, admin_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __del__(self):
        print("Administrator object destroyed")

class Teacher:
    def __init__(self, teacher_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __del__(self):
        print("Teacher object destroyed")

class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.lesson_id_list = []
        


    def __del__(self):
        print("Student object destroyed")


# Directed Graph Representation
prerequisites = {
    "Math 101": set(),                         # No prerequisites
    "Math 102": {"Math 101"},                  # Requires Math 101
    "Physics 101": {"Math 101"},               # Requires Math 101
    "Quantum Mechanics": {"Math 102", "Physics 101"} # Requires both
}




def get_eligible_lessons(completed_lessons: set[str], course_prereqs: dict[str, set[str]]) -> list[str]:
    eligible = []
    for course, reqs in course_prereqs.items():
        if course not in completed_lessons and reqs.issubset(completed_lessons):
            eligible.append(course)
    return eligible



# Example Usage
completed = {"Math 101"}
print(get_eligible_lessons(completed, prerequisites))

# Output: ['Math 102', 'Physics 101']
