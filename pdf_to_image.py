#pip install PyMuPDF     1000 
import fitz
zoom_x = 3.0
zoom_y = 3.0
mat = fitz.Matrix(zoom_x, zoom_y)
doc = fitz.open("dinner recipes book.pdf")
for page in doc:
    pix = page.get_pixmap(matrix=mat)
    pix.save("pdf_to_image\\page-%i.jpg" % page.number)