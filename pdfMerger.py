import os
from PyPDF2 import PdfFileMerger

source = os.getcwd()
merger = PdfFileMerger()
# print(source)

files = sorted(os.listdir(source))
for file in files:
    if file.endswith('pdf'):
        merger.append(file)

merger.write('final.pdf')
merger.close()