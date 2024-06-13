import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'sarif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csvFile' not in request.files or 'sarifFile' not in request.files:
        return 'No file part', 400

    csv_file = request.files['csvFile']
    sarif_file = request.files['sarifFile']

    if csv_file.filename == '' or sarif_file.filename == '':
        return 'No selected file', 400

    if csv_file and allowed_file(csv_file.filename) and sarif_file and allowed_file(sarif_file.filename):
        csv_filename = secure_filename(csv_file.filename)
        sarif_filename = secure_filename(sarif_file.filename)

        csv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_filename))
        sarif_file.save(os.path.join(app.config['UPLOAD_FOLDER'], sarif_filename))

        return 'Files uploaded successfully!', 200

    return 'Invalid file type', 400

if __name__ == '__main__':
    app.run(debug=True)
