import qrcode

img = qrcode.make('introduce')

f = open('output.png', 'wb')
img.save(f)

f.close()