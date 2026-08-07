import json


class Student:

  _registry = []

  def __init__(
      self,
      student_id=None,
      first_name=None,
      last_name=None,
      email=None,
      phone_number=None,
      admin_id=None,
      math_lesson_id_list=None,
      biology_lesson_id_list=None,
      music_lesson_id_list=None,
      Language_lesson_id_list=None,
      art_lesson_id_list=None,
      history_lesson_id_list=None,
      geometry_lesson_id_list=None,
      theory_lesson_id_list=None,
      geography_lesson_id_list=None,
  ):
    self.student_id = student_id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone_number = phone_number
    self.admin_id = admin_id
    # Ensure defaults fallback to lists if None is passed
    self.math_lesson_id_list = (
        math_lesson_id_list if math_lesson_id_list is not None else []
    )
    self.biology_lesson_id_list = (
        biology_lesson_id_list if biology_lesson_id_list is not None else []
    )
    self.music_lesson_id_list = (
        music_lesson_id_list if music_lesson_id_list is not None else []
    )
    self.Language_lesson_id_list = (
        Language_lesson_id_list if Language_lesson_id_list is not None else []
    )
    self.art_lesson_id_list = (
        art_lesson_id_list if art_lesson_id_list is not None else []
    )
    self.history_lesson_id_list = (
        history_lesson_id_list if history_lesson_id_list is not None else []
    )
    self.geometry_lesson_id_list = (
        geometry_lesson_id_list if geometry_lesson_id_list is not None else []
    )
    self.theory_lesson_id_list = (
        theory_lesson_id_list if theory_lesson_id_list is not None else []
    )
    self.geography_lesson_id_list = (
        geography_lesson_id_list
        if geography_lesson_id_list is not None
        else []
    )


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
