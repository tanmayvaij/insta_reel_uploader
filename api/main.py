from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from instagrapi import Client

app = Flask(__name__)

cors = CORS()
cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

@app.route('/upload', methods=['POST'])
def upload():

    client = Client()

    username = request.headers.get('username')
    password = request.headers.get('password')

    for fname in request.files:
        f = request.files.get(fname)
        f.save('./uploads/%s' % secure_filename(fname))

    try:
        file = os.listdir("./uploads")[0]
        client.login(username, password)
        client.clip_upload(f"./uploads/{file}", caption="")

    except Exception as e:
        print(f"Failed: {e}")

    finally:
        dir = './uploads'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))


    return 'Okay!'

if __name__ == '__main__':
    if not os.path.exists('./uploads'):
        os.mkdir('./uploads')
    app.run(debug=True)
