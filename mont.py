import json

from pydantic import BaseModel



MATH = 1
HISTORY = 2
GEOMETRY = 3
GEOGRAPHY = 4
LANGUAGE = 5
BIOLOGY = 6
ART = 7
MUSIC = 8
THEORY = 9


class ValidationRequest(BaseModel):
    selectedRole: str
    textEmail: str

# Allow requests from your remote frontend domain(s)
origins = [
    "https://redhairedlion.com",
    "http://127.0.0.1:8080",  # For local testing
    "http://localhost:8080",  # For local testing
]




class Report:

    _registry = []

    def __init__(self, report_id=None, lesson_id=None, student_id=None, grade=None):
        self.report_id = report_id
        self.lesson_id = lesson_id
        self.student_id = student_id
        self.grade = grade

    # Register this instance
        Report._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()


    def __del__(self):
        print("Report object destroyed")

class Poster:

    _registry = []

    def __init__(self, poster_id=None, lesson_id=None, title=None, description=None):
        self.poster_id = poster_id
        self.lesson_id = lesson_id
        self.title = title
        self.description = description

    # Register this instance
        Poster._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()


    def __del__(self):
        print("Poster object destroyed")

class Curriculum:

    _registry = []

    def __init__(self, curriculum_id=None, subject_id=None, title=None, description=None):
        self.curriculum_id = curriculum_id
        self.subject_id = subject_id
        self.title = title
        self.description = description

    # Register this instance
        Curriculum._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()

    def __del__(self):
        print("Curriculum object destroyed")

class Subject:

    _registry = []

    def __init__(self, subject_id=None, name=None, description=None):
        self.subject_id = subject_id
        self.name = name
        self.description = description
        self.object_id = 1

    # Register this instance
        Subject._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    def __del__(self):
        print("Subject object destroyed")

class Material:

    _registry = []

    def __init__(self, material_id=None, name=None, description=None):
        self.material_id = material_id
        self.name = name
        self.description = description

    # Register this instance
        Material._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    def __del__(self):
        print("Material object destroyed")

class Page:

    _registry = []

    def __init__(self, page_id=None, prerequisite_id=None, material_id=None, title=None, content=None):
        self.page_id = page_id
        self.prerequisite_id = prerequisite_id
        self.material_id = material_id
        self.title = title
        self.content = content

    # Register this instance
        Page._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    def __del__(self):
        print("Page object destroyed")
class Prerequisite:

    _registry = []

    def __init__(self, prerequisite_id=None, page_id=None, page_id_list=None):
        self.prerequisite_id = prerequisite_id
        self.page_id = page_id
        self.page_id_list = page_id_list

    # Register this instance
        Prerequisite._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    def __del__(self):
        print("Prerequisite object destroyed")
        
class Student:

    _registry = []

    def __init__(self, student_id=None, first_name=None, last_name=None, email=None, 
                 phone_number=None, 
                 math_lesson_id_list=None, biology_lesson_id_list=None, music_lesson_id_list=None,
                 Language_lesson_id_list=None, art_lesson_id_list=None, history_lesson_id_list=None, 
                 geometry_lesson_id_list=None, theory_lesson_id_list=None, geography_lesson_id_list=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.math_lesson_id_list = []
        self.biology_lesson_id_list = []
        self.music_lesson_id_list = []
        self.Language_lesson_id_list = []
        self.art_lesson_id_list = []
        self.history_lesson_id_list = []
        self.geometry_lesson_id_list = []
        self.theory_lesson_id_list = []
        self.geography_lesson_id_list = []
        

    # Register this instance
        Student._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry


    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()


    def __del__(self):
        print(f"Student object destroyed for {self.first_name}")



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






def load_students_from_json(filename="Student.JSON"):
  students = []
  Student.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for student_data in data:
        # **student_data unpacks dictionary keys into the __init__ arguments
        student = Student(**student_data)
        students.append(student)

    return students

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []






def save_students_to_json(students, filename="Student.JSON"):
  """Saves a single Student object or a list of Student objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(students, Student):
    students = [students]

  # Convert each Student object into a dictionary of its attributes
  students_data = [vars(student) for student in students]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(students_data, file, indent=4)
    print(
        f"Successfully saved {len(students)} student record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")
