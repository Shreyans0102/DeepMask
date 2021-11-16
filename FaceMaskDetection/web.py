from flask import Flask
import os
from flask import request
from flask import render_template

app = Flask("Hall of Shame!")
picFolder = os.path.join('static', 'imgs')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")

def index():
    imageList = os.listdir('static/imgs')
    imagelist = ['imgs/' + image for image in imageList]
    return render_template("index.html", imagelist=imagelist)

    

if __name__ == "__main__":

    app.run(debug=True)