import qrcode
import qrcode.image.svg

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=2,
)

qr.add_data("https://github.com/jon11L")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("myqrcode.png")


# factory = qrcode.image.svg.SvgPathImage
# svg_img = qrcode.make("hello world", image_factory=factory)

# data_img = input("insert your link or text here.")
# svg_img.save("myqr.svg")