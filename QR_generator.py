from flask import Flask, render_template, request
from segno import helpers
import segno
from urllib.request import urlopen
import os

app = Flask(__name__,
            template_folder='/Users/mxuser1/Desktop/Dev/QR Code')


@app.route('/', methods=['GET', 'POST'])  # Main Route.
def home_qr():

    #  Default field values.
    url_field = ""
    scale_field = ""
    border_field = ""
    error_field = ""
    color_field = ""
    file_name = ""
    file_path = ""
    if request.method == 'POST':
        url_field = request.form.get('url_field')
        scale_field = request.form.get('scale_field')
        border_field = request.form.get('border_field')
        error_field = request.form.get('error_field')
        color_field = request.form.get('color_field')
        #  For testing purposes.
        print(">>>Data from user:", url_field, scale_field,
              border_field, error_field, color_field)
        # QR name and route to save it.
        file_name = "qr.png"
        file_path = os.path.join('static', file_name)
        #  Create QR code.
        qrcode = segno.make_qr(url_field)
        qrcode.save(
            file_path,
            scale=int(scale_field),
            border=int(border_field),
            light=color_field,)

    else:
        print(request.method)

    return render_template('main.html', qr_image=file_name)


@app.route('/v-card', methods=['GET', 'POST'])  # Route 2.
def Vcard():
    # QR name and route to save it.
    file_name = "qr_svg.svg"
    file_path = os.path.join('static', file_name)

    if request.method == 'POST':
        #  Get all the user input values.
        name_form = request.form.get('name_field')
        email_form = request.form.get('email_field')
        title_form = request.form.get('title_field')
        mobile_form = request.form.get('mobile_field')
        address_form = request.form.get('address_field')
        scale_form = request.form.get('scale_card')
        border_form = request.form.get('border_card')
        background_vcard = request.form.get('color_card')

        #  Testing, this line could be omitted.
        print("From user >>>>", title_form, email_form,
              mobile_form, address_form,
              scale_form, border_form, background_vcard)

        # Create VCard QR.
        qrcode = helpers.make_vcard(name=name_form, displayname=name_form,
                                    title=title_form,
                                    email=email_form,
                                    phone=mobile_form, street=address_form,
                                    )
        # Saving the VCard QR.
        qrcode.save(file_path, scale=int(scale_form), border=int(border_form),
                    light=background_vcard)

        return render_template('main.html', name=name_form,
                               file_name=file_name)

    # By default, If the method isn't POST.
    return render_template('main.html')


@app.route('/art-card', methods=['GET', 'POST'])  # Route 3.
def artCard():
    if request.method == 'POST':
        #  Get all the user input values.
        url_art = request.form.get('artistic_url')
        background_art = request.form.get('artistic_background')
        border_art = request.form.get('artistic_border')
        scale_art = request.form.get('artistic_scale')
        color = request.form.get('artistic_color')

        #  Testing, this line could be omitted.
        print("From user>>>>", url_art, background_art, border_art,
              scale_art, color)

        # QR name and route to save it.
        file_name_art = "qr_art.gif"
        file_path = os.path.join('static', file_name_art)

        # Making QR Code.
        slts_qrcode = segno.make_qr(url_art, error='M')
        img_background = urlopen(background_art)
        slts_qrcode.to_artistic(
            background=img_background,
            target=file_path,
            light=color,
            scale=int(scale_art),
            border=int(border_art))
        # To see if the QR code was saved successfully.
        print("QR generated")

    return render_template('main.html', file_name_art=file_name_art)


if __name__ == '__main__':
    app.run(debug=False)
