from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

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