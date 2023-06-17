# pip install qrcode
# pip install PIL

import qrcode
import image

qr=qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=20, border=10)  # customize

qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

img=qr.make_image(fill_color='indigo', back_ground='white')
img.save("elaborate_qrcode.png")