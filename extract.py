import fitz  # PyMuPDF
import re

def extract_prerequisites(pdf_path: str) -> list[dict]:
    """
    Searches a PDF for 'Prerequisite' headers and extracts the following paragraph.
    Returns a list of dicts with page numbers, header text, and the extracted paragraph.
    """
    results = []
    doc = fitz.open(pdf_path)

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


if __name__ == "__main__":
    pdf_file = "final.math.pdf"
    prereqs = extract_prerequisites(pdf_file)

    for entry in prereqs:
        print(f"--- Page {entry['page']} ---")
        print(f"Header: {entry['header']}")
        print(f"Paragraph:\n{entry['paragraph']}\n")

     