

# --- Usage Example ---
if __name__ == "__main__":
  student_list = load_students_from_json("Student.JSON")

  for s in Student._registry:
    print(f"Loaded Student: {s.first_name} {s.last_name} (ID: {s.student_id})")
    print(f"  Math Lessons: {s.math_lesson_id_list}")

    print(f"  Language Lessons: {s.Language_lesson_id_list}")


  # 1. Create a sample student
  Student(
      student_id="S102",
      first_name="Bob",
      last_name="Johnson",
      email="bob@example.com",
      phone_number="555-0200",
      math_lesson_id_list=[101, 103],
      Language_lesson_id_list=[301],
      geography_lesson_id_list=[502],
  )


  for s in Student._registry:
    print(f"Added Student: {s.first_name} {s.last_name} (ID: {s.student_id})")
    print(f"  Math Lessons: {s.math_lesson_id_list}")

    print(f"  Language Lessons: {s.Language_lesson_id_list}")



  # 2. Write the student object to Student.JSON
  save_students_to_json(Student._registry, "Student.JSON")

  student_list = load_students_from_json("Student.JSON")

  for s in Student._registry:
    print(f"Loaded Student: {s.first_name} {s.last_name} (ID: {s.student_id})")
    print(f"  Math Lessons: {s.math_lesson_id_list}")

    print(f"  Language Lessons: {s.Language_lesson_id_list}")


