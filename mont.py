import json
from pydantic import BaseModel


class MyState:
    thisAccount: str
    isLoggedIn: bool

    _registry = []

    def __init__(self, thisAccount='', isLoggedIn=False):
        
        self.thisAccount = thisAccount
        self.isLoggedIn = isLoggedIn

    # Register this instance
        MyState._registry.append(self)

    @classmethod  
    def __del__(self):
        return


state = MyState('',False)


MATH = 1
HISTORY = 2
GEOMETRY = 3
GEOGRAPHY = 4
LANGUAGE = 5
BIOLOGY = 6
ART = 7
MUSIC = 8
THEORY = 9


class HttpRequest(BaseModel):
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
        return

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
        return


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
        return

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
 
    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()
   
    def __del__(self):
        return

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

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()

    def __del__(self):
        return

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

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()

    def __del__(self):
        return


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

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()

    def __del__(self):
        return
        


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




def load_curriculum_from_json(HttpRequest, filename="Curriculum.JSON"):
  curriculums = []
  Curriculum.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for curriculum_data in data:
        # **curriculum_data unpacks dictionary keys into the __init__ arguments
        curriculum = Curriculum(**curriculum_data)
        curriculums.append(curriculum)

      curriculum_data = [vars(curr) for curr in Curriculum._registry]

    return curriculum_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []




def load_page_from_json(HttpRequest, filename="Page.JSON"):
  pages = []
  Page.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for page_data in data:
        # **page_data unpacks dictionary keys into the __init__ arguments
        page = Page(**page_data)
        pages.append(page)

      page_data = [vars(pg) for pg in Page._registry]

    return page_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []



def load_prerequisite_from_json(HttpRequest, filename="Prerequisite.JSON"):
  prerequisites = []
  Prerequisite.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for prerequisite_data in data:
        # **curriculum_data unpacks dictionary keys into the __init__ arguments
        prerequisite = Prerequisite(**prerequisite_data)
        prerequisites.append(prerequisite)

      prerequisite_data = [vars(prereq) for prereq in Prerequisite._registry]

    return prerequisite_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []




def load_subject_from_json(HttpRequest, filename="Subject.JSON"):
  subjects = []
  Subject.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for subject_data in data:
        # **subject_data unpacks dictionary keys into the __init__ arguments
        subject = Subject(**subject_data)
        subjects.append(subject)

      subject_data = [vars(subj) for subj in Subject._registry]

    return subject_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []


def load_poster_from_json(HttpRequest, filename="Poster.JSON"):
  posters = []
  Poster.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for poster_data in data:
        # **subject_data unpacks dictionary keys into the __init__ arguments
        poster = Poster(**poster_data)
        posters.append(poster)

      poster_data = [vars(post) for post in Poster._registry]

    return poster_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []


def load_material_from_json(HttpRequest, filename="Material.JSON"):
  materials = []
  Material.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for material_data in data:
        # **subject_data unpacks dictionary keys into the __init__ arguments
        material = Material(**material_data)
        materials.append(material)

      material_data = [vars(mat) for mat in Material._registry]

    return material_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []


def load_report_from_json(HttpRequest, filename="Report.JSON"):
  reports = []
  Report.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for report_data in data:
        # **subject_data unpacks dictionary keys into the __init__ arguments
        report = Report(**report_data)
        reports.append(report)

      report_data = [vars(rept) for rept in Report._registry]

    return report_data

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []

