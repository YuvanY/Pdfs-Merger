from heapq import merge
import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    
    print("Pdfs are merged Successfully!")
    
    merger.write('super.pdf')

pdf_combiner(inputs)
