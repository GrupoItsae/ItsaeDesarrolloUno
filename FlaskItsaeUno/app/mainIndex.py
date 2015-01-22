'''
Created on 18/2/2015

@author: PC06
'''
from app import app, ALLOWED_EXTENSIONS
from flask import request, redirect, url_for, render_template
import os

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/main")
def main():
    
    return render_template("mainPersona.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def uploadfileX():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = (file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploadfileX'))
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="/upload" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''