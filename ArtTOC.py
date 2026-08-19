import os
import sys
import json
import pymupdf  # PyMuPDF
from mont import Curriculum, Page, Subject


class StateSubject:

  def __init__(self, id_val: str = '', name_val: str = ''):
    self.id = id_val
    self.name = name_val

  def set_id(self, new_id: str):
    self.id = new_id

  def get_id(self) -> str:
    return self.id

  def set_name(self, new_name: str):
    self.name = new_name

  def get_name(self) -> str:
    return self.name


# Create your instance
state_subject = StateSubject()



def parse_pdf_toc(pdf_path: str):
    """Opens a PDF and prints each Table of Contents (TOC) entry text to the screen."""
    try:
        # Open the PDF document
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    # Retrieve the table of contents
    # Returns a list of items: [lvl, title, page, ...]
    toc = doc.get_toc()

    if not toc:
        print("No Table of Contents (bookmarks/outlines) found in this PDF.")
        doc.close()
        return

    print(f"Table of Contents for: {pdf_path}\n" + "-" * 40)

    curriculum.subject_id = state_subject.get_id()
    curriculum.title = state_subject.get_name()

    for item in toc:
        level, title, page = item[0], item[1], item[2]
        
        # Indent visually based on hierarchy level (Level 1 = 0 indents, Level 2 = 2 spaces, etc.)
        indent = "  " * (level - 1)

        curriculum.page_id.append(page)

        newPage = Page()
        newPage.page_id = page
        newPage.title = f"{indent} {title}"
        newPage.subject_id = state_subject.get_id()

        # Output the text of the entry
        print(f"{indent}- {title} (Page {page})")

    save_art_pages_to_json(Page.get_all_instances())
    # Close the document
    doc.close()




def load_extant_curriculum_from_json( filename="Curriculum.JSON" ):
    curriculums = []
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Handle cases where JSON is either a list of objects or a single object
        if isinstance(data, dict):
            data = [data]

        for curriculum_data in data:
            # **curriculum_data unpacks dictionary keys into the __init__ arguments
            extantCurriculum = Curriculum(**curriculum_data)
            curriculums.append(extantCurriculum)

        curriculum_data = [vars(curr) for curr in Curriculum._registry]

        return curriculum_data

    else:  
        data = []
        return data






def load_art_pages_from_json( filename="Page.JSON" ):
    pages = []
    Page.delete_all_instances();
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
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
        #  return JSON format of Page.JSON
        return page_data  
    else:
        data=[]
        return data




def save_art_pages_to_json(pages, filename="Page.JSON"):
  """Saves a single Page object or a list of Page objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(pages, Page):
    pages = [pages]

  # Convert each Page object into a dictionary of its attributes
  pages_data = [vars(page) for page in pages]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(pages_data, file, indent=4)
    print(
        f"Successfully saved {len(pages)} page record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")



def save_art_curriculum_to_json(curriculums, filename="Curriculum.JSON"):
  """Saves a single  object or a list of objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(curriculums, Curriculum):
    curriculums = [curriculums]

  # Convert each Curriculum object into a dictionary of its attributes
  curriculums_data = [vars(curriculum) for curriculum in curriculums]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(curriculums_data, file, indent=4)
    print(
        f"Successfully saved {len(curriculums)} curriculum record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")


def load_subject_from_json(subjectName='Art', filename="Subject.JSON"):
  Subject.delete_all_instances();
  try:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

      # Handle cases where JSON is either a list of objects or a single object
      if isinstance(data, dict):
        data = [data]

      for subject_data in data:
        # **subject_data unpacks dictionary keys into the __init__ arguments
        thisSubject = Subject(**subject_data)
        if thisSubject.name == subjectName:
            state_subject.set_id(thisSubject.subject_id)
            state_subject.set_name(thisSubject.name)

    return thisSubject

  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return []
  except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    return []



# mainline logic
if __name__ == "__main__":

    # Replace with your PDF path or pass it via command line
    file_path = sys.argv[1] if len(sys.argv) > 1 else "final.art.pdf"

    curriculum = Curriculum()

    load_subject_from_json()
    existsPages = load_art_pages_from_json()
    existsCurriculum = load_extant_curriculum_from_json()    
    parse_pdf_toc(file_path)

    save_art_curriculum_to_json( curriculum.get_all_instances() )    
