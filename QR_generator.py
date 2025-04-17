#  Code used in QR generator deployed on PythonAnywhere
from flask import Flask, render_template, request
from segno import helpers
import segno
import os
import io
from PIL import Image  # Importing the Image module from Pillow

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Main Route.
def home_qr():
    # Default field values
    url_field = ""
    scale_field = ""
    border_field = ""
    color_field = ""
    file_name = ""

    if request.method == 'POST':
        url_field = request.form.get('url_field')
        scale_field = request.form.get('scale_field')
        border_field = request.form.get('border_field')
        color_field = request.form.get('color_field')

        #  For testing purposes
        #print(">>>Data from user:", url_field, scale_field,
              #border_field, error_field, color_field)

        # Path for static folder
        static_folder = os.path.join(os.path.dirname(__file__), 'static')
        file_name = os.path.join(static_folder, 'qr.png')  # full path to file

        # Set defaults if values are empty
        scale = int(scale_field) if scale_field else 10
        border = int(border_field) if border_field else 2
        color = color_field if color_field else '#ffffff'  # white background

        # Save QR code
        qrcode = segno.make_qr(url_field)
        qrcode.save(file_name, scale=scale, border=border, light=color)

        #  Testing save route
        print(">>> Saved QR code to:", file_name)
        print(">>> Current working dir:", os.getcwd())

        return render_template('main.html', image_url='qr.png')

    # By default return
    return render_template('main.html')



@app.route('/v-card', methods=['GET', 'POST'])  # Route 2.
def Vcard():
    # QR name and route to save it.
    file_name = "qr_svg.svg"

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
        '''print("From user >>>>", title_form, email_form,
              mobile_form, address_form,
              scale_form, border_form, background_vcard)'''


        #  Path for static folder, to save the QR
        static_folder = os.path.join(os.path.dirname(__file__), 'static')
        file_name = os.path.join(static_folder, 'qr_svg.svg')  # full path to file


        # Create VCard QR.
        qrcode = helpers.make_vcard(name=name_form, displayname=name_form,
                                    title=title_form,
                                    email=email_form,
                                    phone=mobile_form, street=address_form,
                                    )
        # Saving the VCard QR.
        qrcode.save(file_name, scale=int(scale_form), border=int(border_form),
                    light=background_vcard)

        return render_template('main.html',image_url_svg='qr_svg.svg')

    # By default, If the method isn't POST.
    return render_template('main.html')


@app.route('/artCard', methods=['POST', 'GET']) #  Route 3
def artCard():
    if request.method == 'POST':
        # Get all the user input values.
        url_art = request.form.get('artistic_url')
        border_art = request.form.get('artistic_border')
        scale_art = request.form.get('artistic_scale')
        selected_option = request.form.get('options')
        color = request.form.get('artistic_color')

        #  Testing, this line could be omitted.
        print("Image option selected >>", selected_option)

        # Corrected path to static files
        background_art = os.path.join('mysite','static', selected_option)
        print("********Full path to image:", background_art)


        # Check if the image file selected exists
        if not os.path.exists(background_art):
            print(f"Error: The file '{background_art}' does not exist.")
            return "Image not found!", 404


        # Code section taken from Segno documentation
        out = io.BytesIO()
        segno.make(url_art, error='h').save(out, scale=int(scale_art),
                                            border=int(border_art),
                                            kind='png', light=color)
        out.seek(0)  # Important to let Pillow load the PNG
        img = Image.open(out)
        img = img.convert('RGB')  # Ensure colors for the output
        img_width, img_height = img.size
        logo_max_size = img_height // 3  # May use a fixed value as well
        logo_img = Image.open(background_art)  # The logo

        # Resize the logo to logo_max_size
        logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)

        # Calculate the center of the QR code
        box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
        img.paste(logo_img, box)

        #  Name and path to save the QR generated
        file_name_art = 'qrcode_with_logo_art.png'
        img.save(os.path.join('mysite','static', file_name_art))

        return render_template('main.html', file_name_art=file_name_art)
    # If there is not qr, the render template doesn't show anything file
    return render_template('main.html', file_name_art=file_name_art)


if __name__ == '__main__':
    app.run(debug=False)

