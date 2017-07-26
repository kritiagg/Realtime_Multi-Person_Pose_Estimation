import os
import json
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    print("The uploaded file is:",filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/api/hello')
def index():
    return "Hello!"


# Route that will process the file upload
@app.route('/api', methods=['POST'])
def upload():
 print("file upload request")
 from PIL import Image
 from PIL import ImageDraw
 from PIL import ImageFont
 import io
 import binascii
 
 data = request.data
 
 stream = io.BytesIO(data)
 
 img = Image.open(stream)
 draw = ImageDraw.Draw(img)
 img.save("test.jpg")
 d = {"Scene":{"Content":"Your custom caption here.","Format":"Text","Success":True}}
 return json.dumps(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
