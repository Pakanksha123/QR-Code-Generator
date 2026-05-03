import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data("https://drive.google.com/file/d/1M93T36N1CjQ6bTlvSxELxeTcCR5ORym1/view?usp=drive_link")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("resume.png")
