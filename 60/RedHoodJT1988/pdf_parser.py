import PyPDF2
pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
pageObj.extractText('sample.txt')
