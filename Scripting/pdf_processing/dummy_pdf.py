import PyPDF2

with open('twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    num_pages = reader.numPages

    for i in range(num_pages):
        page = reader.getPage(i)
        page.rotateClockwise(90)
        writer.addPage(page)
        
    with open('new_dummy.pdf', 'wb') as new_file:
        writer.write(new_file)
