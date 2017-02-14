from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from myngram import ngram_hemal1
from tokensdict import formdict
from bson import BSON
from bson import json_util
from pprint import pprint
from jinja2 import Template
import json
import bson
from werkzeug import secure_filename
import os


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

# Initialize the Flask application
app = Flask(__name__)

connection = MongoClient('localhost', 27017)
db = connection.project #database name.
collection = connection.tag # collection name.

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case


@app.route('/hello', methods=['POST'])
def hello():
    tagn = get_tags()
    textentered=request.form['description']
    tokens=ngram_hemal1(textentered)
    tokendic= formdict(textentered)
    name=request.form['yourname']
    db.collection.insert({'title': name, 'description': textentered,'tag': tokendic})
    return render_template('form_submit.html', description=tokens)




@app.route("/")
def getdata():      
    list =  [          
          {"tag": "java"            ,  "weight": 2},
          {"tag": "python"          ,  "weight": 12},
          {"tag": "object oriented" ,  "weight": 22},
          {"tag": "c#"              ,  "weight": 32}
            ]
    # add defensive programming at this point in case my_data is None
    return render_template('features.html', row=list)
      


def get_tags():
    return [          
          {"tag": "java"            ,  "weight": 2},
          {"tag": "python"          ,  "weight": 12},
          {"tag": "object oriented" ,  "weight": 22},
          {"tag": "c#"              ,  "weight": 32}
            ]
          
  
@app.route("/technology")
def get_records():
    list =  [          
          {"tag": "java"            ,  "weight": 2},
          {"tag": "python"          ,  "weight": 12},
          {"tag": "object oriented" ,  "weight": 22},
          {"tag": "c#"              ,  "weight": 32}
            ]
          
    return jsonify(results = list)

@app.route('/About')
def default_jsonencoder():
    now = datetime.now()
    return jsonify({'now': now})

@app.route('/upload',methods = ['POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
    return render_template('upload.html')

@app.route('/featureschange', methods=['POST'])
def features():
    connection = MongoClient('localhost', 27017)
    db = connection.project
    data = db.collection
    output = []
    
    #alist = data.find()

    cursor = data.find()
    for document in cursor: 
        #output1 = pprint(document)
        output.append(document)    
    return render_template('featureschange.html', rows=output)



# Run the app :)
if __name__ == '__main__':
  app.run(debug=True)
