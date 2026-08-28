import os
import sys
import json
import re
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
    prerequisites_pointer = 0
    materials_pointer = 0


    for item in toc:
        level, title, page = item[0], item[1], item[2]
        
        # Indent visually based on hierarchy level
        indent = '\u00A0' * (level * 4)

        curriculum.page_id.append(page)

        newPage = Page()
        newPage.page_id = page
        newPage.title = f"{indent} {title}"
        newPage.subject_id = state_subject.get_id()

        if len(prereqs) > prerequisites_pointer and prereqs[prerequisites_pointer]["page"] == newPage.page_id:
           newPage.prerequisite_text = prereqs[prerequisites_pointer]["paragraph"]
           prerequisites_pointer+=1

        if len(materials) > materials_pointer and materials[materials_pointer]["page"] == newPage.page_id:
           newPage.material_text = materials[materials_pointer]["paragraph"]
           materials_pointer+=1

        # Output the text of the entry
        print(f"{indent}- {title} (Page {page})")

    save_new_pages_to_json(Page.get_all_instances())
    # Close the document
    doc.close()




def load_extant_curriculum_from_json( filename="Curriculum.JSON" ):
    curriculums = []
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
      try:
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
      except OSError as e:
           sys.exit(f"I/O Error. {e.errno} {e.strerror}")
    else:  
        data = []
        return data







def load_extant_pages_from_json( filename="Page.JSON" ):
    pages = []
    Page.delete_all_instances();
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
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
          #  return JSON format of Page.JSON
          return page_data  
        except OSError as e:
           sys.exit(f"I/O Error. {e.errno} {e.strerror}")
    else:
      data=[]
      return
    




def save_new_pages_to_json(pages, filename="Page.JSON"):
  """Saves a single Page object or a list of Page objects to a JSON file."""
  # Ensure input is formatted as a list
  if isinstance(pages, Page):
    pages = [pages]

  # Convert each Page object into a dictionary of its attributes
#  pages_data = [vars(page) for page in pages]
  pages_data = [page.to_dict() for page in pages]

  try:
    with open(filename, "w", encoding="utf-8") as file:
      # indent=4 formats the output with pretty-printing for readability
      json.dump(pages_data, file, indent=4)
    print(
        f"Successfully saved {len(pages)} page record(s) to '{filename}'."
    )
  except IOError as e:
    print(f"Failed to write to file '{filename}': {e}")
    sys.exit(f"I/O Error. {e.errno} {e.strerror}")



def save_new_curriculum_to_json(curriculums, filename="Curriculum.JSON"):
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
    sys.exit(f"I/O Error. {e.errno} {e.strerror}")


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

  except FileNotFoundError as e:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(f"I/O Error. {e.errno} {e.strerror}")

  except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON from '{filename}'. Check format.")
    sys.exit(f"I/O Error. {e.errno} {e.strerror}")




def extract_prerequisites(pdf_path: str) -> list[dict]:
    """
    Searches a PDF for 'Prerequisite' headers and extracts the following paragraph.
    Returns a list of dicts with page numbers, header text, and the extracted paragraph.
    """
    results = []
    doc = pymupdf.open(pdf_path)

    # Regex to match 'Prerequisite' or 'Prerequisites' as a standalone header/line
    header_pattern = re.compile(r"^\s*Prerequisites?[:\s]*$", re.IGNORECASE)

    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # get_text("blocks") returns tuples: (x0, y0, x1, y1, text, block_no, block_type)
        # block_type == 0 indicates text (type 1 is an image)
        blocks = [b for b in page.get_text("blocks") if b[6] == 0]

        for i, block in enumerate(blocks):
            block_text = block[4].strip()
            
            # Case 1: The header is its own block, target is the next block
            if header_pattern.match(block_text):
                if i + 1 < len(blocks):
                    paragraph = blocks[i + 1][4].strip()
                    results.append({
                        "page": page_num + 1,
                        "header": block_text,
                        "paragraph": paragraph
                    })

            # Case 2: The header and paragraph share the same block (first line is header)
            elif re.match(r"^\s*Prerequisites?[:\s]*\n", block_text, re.IGNORECASE):
                lines = block_text.splitlines()
                header = lines[0].strip()
                paragraph = "\n".join(lines[1:]).strip()
                results.append({
                    "page": page_num + 1,
                    "header": header,
                    "paragraph": paragraph
                })

    doc.close()
    return results



def extract_materials(pdf_path: str) -> list[dict]:
    """
    Searches a PDF for 'Materials' headers and extracts the following paragraph.
    Returns a list of dicts with page numbers, header text, and the extracted paragraph.
    """
    results = []
    doc = pymupdf.open(pdf_path)

    # Regex to match 'Material' or 'Materials' as a standalone header/line
    header_pattern = re.compile(r"^\s*Materials?[:\s]*$", re.IGNORECASE)

    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # get_text("blocks") returns tuples: (x0, y0, x1, y1, text, block_no, block_type)
        # block_type == 0 indicates text (type 1 is an image)
        blocks = [b for b in page.get_text("blocks") if b[6] == 0]

        for i, block in enumerate(blocks):
            block_text = block[4].strip()
            
            # Case 1: The header is its own block, target is the next block
            if header_pattern.match(block_text):
                if i + 1 < len(blocks):
                    paragraph = blocks[i + 1][4].strip()
                    results.append({
                        "page": page_num + 1,
                        "header": block_text,
                        "paragraph": paragraph
                    })

            # Case 2: The header and paragraph share the same block (first line is header)
            elif re.match(r"^\s*Materials?[:\s]*\n", block_text, re.IGNORECASE):
                lines = block_text.splitlines()
                header = lines[0].strip()
                paragraph = "\n".join(lines[1:]).strip()
                results.append({
                    "page": page_num + 1,
                    "header": header,
                    "paragraph": paragraph
                })

    doc.close()
    return results



# mainline logic
if __name__ == "__main__":

    # Replace with your PDF path or pass it via command line
  if len(sys.argv) == 3:
    inputPDF = sys.argv[1]
    inputSubject = sys.argv[2]

    prereqs = extract_prerequisites(inputPDF)
    materials = extract_materials(inputPDF)

    curriculum = Curriculum()
    load_subject_from_json(inputSubject)
    existsPages = load_extant_pages_from_json()
    existsCurriculum = load_extant_curriculum_from_json()  
    # create and save new Page objects  
    parse_pdf_toc(inputPDF)

    save_new_curriculum_to_json( curriculum.get_all_instances() )
        
  else:
    print( "args pdf and subject required")