import json

class Lesson:

    _registry = []

    def __init__(self, lesson_id=None, page_id=None, lesson_id_list=None, title=None, description=None, date=None, time=None, review_date=None):
        self.lesson_id = lesson_id
        self.page_id = page_id
        self.lesson_id_list = lesson_id_list
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.review_date = review_date

    # Register this instance
        Lesson._registry.append(self)

    @classmethod
    def get_all_instances(cls):
        """Returns all tracked instances."""
        return cls._registry

    @classmethod
    def delete_all_instances(cls):
        """Deletes all tracked instances."""
        cls._registry.clear()


    def __del__(self):
        print(f"Lesson object destroyed for {self.lesson_id}")


def load_lessons_from_json(filename="Lesson.JSON"):
  lessons = []
  Lesson.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for lesson_data in data:
        # **lesson_data unpacks dictionary keys into the __init__ arguments
        lesson = Lesson(**lesson_data)
        lessons.append(lesson)

    return lessons

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []




def save_lessons_to_json(lessons, filename="Lesson.JSON"):
  """Saves a single Lesson object or a list of Lesson objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(lessons, Lesson):
    lessons = [lessons]

  # Convert each Lesson object into a dictionary of its attributes
  lessons_data = [vars(lesson) for lesson in lessons]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(lessons_data, file, indent=4)
    print(
        f"Successfully saved {len(lessons)} lesson record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")



# --- Usage Example ---
if __name__ == "__main__":
  lesson_list = load_lessons_from_json("Lesson.JSON")

  for s in Lesson._registry:
    print(f"Loaded Lesson: {s.title} {s.description}")

  Lesson(
    "GEO-101",
    "PG-006",
    ["GEO-099","MATH-100"],      
    "Introduction to Life Basics",
    "Learn the fundamentals of functional Living.",
    "2026-09-01",
    "09:00:00",
    "2026-09-01"
  )

  for s in Lesson._registry:
    print(f"Loaded Lesson: {s.title} {s.description}")

  # 2. Write the student object to Student.JSON
  save_lessons_to_json(Lesson._registry, "Lesson.JSON")

