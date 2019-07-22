from flask import Flask, Response
import requests

app = Flask(__name__)
default_name = 'yusuke'
dnmonster_api_path = 'http://dnmonster:8080/monster/'

@app.route("/")
def get_template():
    name = default_name

    header = '<html><head><title>Icon</title></head><body>'

    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{}">
              <input type="submit" value="submit">
              </form>
              <p> You look like a:
              <img src="/user/a.png"/>
              '''.format(name)

    footer = '</body></html>'

    return header + body + footer

@app.route("/user/<name>")
def get_icon(name):
    response = requests.get(dnmonster_api_path + name + "?size=80")
    image = response.content

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')