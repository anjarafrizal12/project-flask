from flask import Flask
from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
import base64
import os

app = Flask(__name__)

my_string = ""

@app.route('/upload-ui', methods=["POST"])
def uploadui():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        name, extension = os.path.splitext(filename)

        print(extension.upper())

        if extension.upper() == ".PNG" or extension.upper() == ".JPG" or extension.upper() == ".JPEG":
            my_string = base64.b64encode(file.read())
            my_string = my_string.decode('utf-8')

            return {"Uploaded file": file.filename, "base64":my_string}
            
        else:
            return {"error":"invalid extension","allowed":"JPG, JPEG, PNG","upload_ext":extension.upper()}
            

        
    