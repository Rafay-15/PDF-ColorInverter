import fitz  # PyMuPDF
from PIL import Image, ImageOps
import img2pdf
import os

# Function to invert colors of a PDF file
def invert_color(filepath):
    # Open the PDF file
    pdf_document = fitz.open(filepath)

    idx_counter = []
    for page_number in range(len(pdf_document)):
        # Render the page as an image
        page = pdf_document.load_page(page_number)
        pixmap = page.get_pixmap()

        # Convert the pixmap to PIL Image
        img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Invert colors
        inverted_img = ImageOps.invert(img)

        # Save the inverted image
        output_path = f"output_page_{page_number}.jpeg"
        inverted_img.save(output_path)
        idx_counter.append(output_path)

    # Convert the inverted images to PDF
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert(idx_counter))

    # Remove temporary image files
    for image_file in idx_counter:
        os.remove(image_file)

# Example usage
invert_color("input.pdf")
