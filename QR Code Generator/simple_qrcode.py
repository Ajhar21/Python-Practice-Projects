# pip install qrcode

import qrcode as qr    # qr is allias of qrcode

img=qr.make("https://www.youtube.com/")

img.save("qrcode_for_youtube.png")

