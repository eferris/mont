
import json


class Administrator:

    _registry = []

    def __init__(self, admin_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    # Register this instance
        Administrator._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()



    def __del__(self):
        print("Administrator object destroyed")

class Teacher:

    _registry = []

    def __init__(self, teacher_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    # Register this instance
        Teacher._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()

    def __del__(self):
        print("Teacher object destroyed")


def load_teachers_from_json(filename="Teacher.JSON"):
  teachers = []
  Teacher.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for teacher_data in data:
        # **teacher_data unpacks dictionary keys into the __init__ arguments
        teacher = Teacher(**teacher_data)
        teachers.append(teacher)

    return teachers

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []




def save_teachers_to_json(teachers, filename="Teacher.JSON"):
  """Saves a single Teacher object or a list of Teacher objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(teachers, Teacher):
    teachers = [teachers]

  # Convert each Teacher object into a dictionary of its attributes
  teachers_data = [vars(teacher) for teacher in teachers]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(teachers_data, file, indent=4)
    print(
        f"Successfully saved {len(teachers)} teacher record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")



# --- Usage Example ---
if __name__ == "__main__":
  teacher_list = load_teachers_from_json("Teacher.JSON")

  for s in Teacher._registry:
    print(f"Loaded Teacher: {s.first_name} {s.last_name}")

Teacher(
    "7890",
    "John",
    "Doe"
)


for s in Teacher._registry:
  print(f"Loaded Teacher: {s.first_name} {s.last_name}")

  # 2. Write the student object to Student.JSON
save_teachers_to_json(Teacher._registry, "Teacher.JSON")

