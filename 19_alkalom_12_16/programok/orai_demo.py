from collections import OrderedDict

od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

od.move_to_end('a')

print(od)

od.popitem(last=False)
od.popitem(last=True)

print(od)



from collections import Counter

c = Counter('abracadabra')

print(c)

print(c.most_common(2))
print(list(c.elements()))




from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(10, 20)

print(p.x, p.y)

p2 = p._replace(x=15)
print(p2)
print(p._asdict())




from collections import deque
# fifo lifo

dq = deque([1,2,3])

dq.append(4)
dq.appendleft(0)

print(dq)

dq.rotate(1)

print(dq)




from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("data/export/output.pdf")
writer = PdfWriter()

print(f'Oldalak száma: {len(reader.pages)}')

for page in reader.pages:
    print(page.extract_text())
    writer.add_page(page)

with open("data/export/output.pdf", 'wb') as output_file:
    writer.write(output_file)



from reportlab.pdfgen import canvas

c = canvas.Canvas("data/export/output_report.pdf")
c.drawString(100, 750, "hello reportlab")
c.save()


from PIL import Image

img = Image.open("data/example.jpg")
img.save("data/export/output.png")

resized = img.resize((200, 200))
resized.save("data/export/resized.jpg")


from PIL import ImageFilter

blurred = img.filter(ImageFilter.BLUR)
blurred.save("data/export/blurred.jpg")


img = Image.open("data/example.jpg")
gray = img.convert("L")
gray.save("data/export/gray.jpg")


cropped = img.crop((50, 50, 200, 200))
cropped.save("data/export/cropped.jpg")

rotated = img.rotate(45)
rotated.save("data/export/rotated.jpg")



# exif -> exchangable image file format

img = Image.open('data/lahmacun_p.JPG')
exif_data = img.getexif()

print(exif_data)

if exif_data:
    for tag, value in exif_data.items():
        print(f'{tag}: {value}')