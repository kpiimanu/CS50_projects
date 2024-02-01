# Program that prompts user for name and outputs a CS50 shirtificate

from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        # Adding title
        self._pdf.set_font('Arial', 'B', 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', align='C')
        # Rendering shirt design
        self._pdf.image('shirtificate.png', w=150, h=150, x=50, y=100)
        self._pdf.set_font_size(35)
        self._pdf.set_text_color(255, 255, 255)
        # Using user input for name to be used in shirt text
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

# Instantiation of inherited class
name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")