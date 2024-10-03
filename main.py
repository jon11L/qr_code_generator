from flask import Flask, render_template, request
import qrcode 

from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def generate_qr():
    ''' create QRcode, with data/link inserted by user and optionally color can be customized.
        Default color value are black `color_1` and white `color_2`.
    '''
    memory = BytesIO()
    # --- getting the user's datas ---
    color_1 = request.form.get("fill-color")
    color_2 = request.form.get("background-color")
    data_passed = request.form.get("link")

    if not data_passed:
        # --- if no data is passed, then no QRcode created. ---
        return render_template("index.html")
    else:
        # --- QRcode creation -----
        qr = qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
        )

        qr.add_data(data_passed)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color_1, back_color=color_2)

        # ---- save the created image in memory temporarily (qrcode not saved locally)---- 
        img.save(memory)
        memory.seek(0)
        base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode("ascii")

        return render_template("index.html" ,data=base64_img)


if __name__ == "__main__":
    app.run(debug=True)
