from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from time import perf_counter
print(perf_counter())
buffer = BytesIO()
p = canvas.Canvas(buffer, pagesize=A4)
p.drawString(185, 618, "surname")
p.drawString(185, 608, "name")
p.drawString(185, 596, "fathername")
p.drawString(185, 584.5, "male or female")
p.drawString(185, 573, "age")
p.drawString(185, 560, "adress")
p.drawString(185, 547, "document")
p.showPage()
p.save()
buffer.seek(0)
newPdf = PdfFileReader(buffer)
pdf1 = buffer.getvalue()
open('pdf1.pdf', 'wb').write(pdf1)
existingPdf = PdfFileReader(open('template.pdf', 'rb'))
output = PdfFileWriter()
page = existingPdf.getPage(0)
page.mergePage(newPdf.getPage(0))
output.addPage(page)
outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()
