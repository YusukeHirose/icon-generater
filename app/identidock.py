from flask import Flask, Response, request
import requests
import hashlib

app = Flask(__name__)
default_name = 'yusuke'
dnmonster_api_path = 'http://dnmonster:8080/monster/'
salt = "UNIQUE_SALT"

@app.route("/", methods=['GET', 'POST'])
def get_template():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']

    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title>Icon</title></head><body>'

    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{0}">
              <input type="submit" value="submit">
              </form>
              <p> You look like a:
              <img src="/user/{1}"/>
              '''.format(name, name_hash)

    footer = '</body></html>'

    return header + body + footer

@app.route("/user/<name>")
def get_icon(name):
    response = requests.get(dnmonster_api_path + name + "?size=80")
    image = response.content

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')