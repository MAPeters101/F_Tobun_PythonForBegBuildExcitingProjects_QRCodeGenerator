import qrcode

qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40, higher is denser)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Error correction level
    box_size=10, # Siz of each QR code "box" in pixels
    border=4, # Border around the QR code (4 is a good default)
)

data = "https://www.bethmedia.com"
qr.add_data(data)

qr.make(fit=True)

# Create an Image object from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

img.save('qr.png')

img.show()