from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Rotate it!</title>
        <style> 
         form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

    <form action="/" method="post">
        <label> 
            Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <br>
            <textarea name="text">Enter text here</textarea> 
        <br>
            <input type="submit" value="Submit Query"/>  
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    content = form 
    return content
    
@app.route("/", methods=['POST'])
def encrypt():
    textt = request.form["rot"]
    rott = request.form["text"]
    encrypty = rotate_string(textt, rott)
    #print(encrypty)
    content= form  
    
    return content

app.run()