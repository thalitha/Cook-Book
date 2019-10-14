from flask import Flask
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
     return 

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True) 