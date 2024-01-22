# import pandas
# df=pandas.read_excel("file.xlsx")
# print(df)

'''Program read pdf'''
from pdfquery import PDFQuery
pdf=PDFQuery("cv.pdf")
pdf.load()
#use CSS-like to selector to locate the element
text_elements = pdf.pq('LTTextLineVertical')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)

#read the PDF
pdf = PDFQuery.PDFQuery('cv.pdf')
pdf.load()


#convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print = True)
pdf


