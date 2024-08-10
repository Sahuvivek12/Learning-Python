# Merge pdf using PyPDF2 module

from PyPDF2 import *
import os
import sys

files = os.listdir('./day 21 of coding/pdf')
print(files)
merger = PdfMerger()

for file in files:
    absfile = os.path.join('day 21 of coding/pdf', file)
    if file.endswith(".pdf"):
        merger.append(absfile)

merger.write("./day 21 of coding/pdf/Merged.pdf")


# done










