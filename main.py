from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from api import transform_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkeylol'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['MAX_CONTENT_LENGTH'] = 64 * 1000 * 1000

class UploadFileForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/',  methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        #check if file is a valid submission file
        status = transform_file(form.username.data)
        return render_template('download_page.html', status=status)
    return render_template('index.html', form=form)

@app.route('/submitted', methods=['POST'])
def submitted():
    if request.method == 'POST':
        username = request.form['user']
        print(username)
        file = request.form['subs']
        return jsonify({'output': 'Processing submissions of user ' + username + '. This might take a while.'})
    else:
        print("error...")

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)