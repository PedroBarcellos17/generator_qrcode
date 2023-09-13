import qrcode
import matplotlib.pyplot as plt


data = "https://twitter.com/i/flow/login"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
