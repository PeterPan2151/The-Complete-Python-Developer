import PyPDF2
import sys

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

    
inputs = sys.argv[1:]
pdf_combiner(inputs)

