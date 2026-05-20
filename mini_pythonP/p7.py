import qrcode

text = "fuckk gandu sobit"

img = qrcode.make(text)

img.save("funny_qr.png")

print("QR Code saved!")