from flask import Flask, render_template, request
import qrcode 

from io import BytesIO
from base64 import b64encode

# import qr_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/", methods=["POST"])
def generate_qr():
    ''' create QRcode including data given by user and render QRcode image back'''
    memory = BytesIO()
    # --- getting the datas from the user, 
    color_1 = request.form.get("fill-color")
    color_2 = request.form.get("background-color")
    data = request.form.get("link")

    # --- QRcode creation -----
    qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color_1, back_color=color_2)

    # ---- save the created image ---- 
    img.save(memory)
    memory.seek(0)
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode("ascii")

    return render_template("home.html" ,data=base64_img)


if __name__ == "__main__":
    app.run(debug=True)