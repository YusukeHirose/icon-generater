from flask import Flask
app = Flask(__name__)
default_name = 'yusuke'

@app.route("/")
def get_icon():
    name = default_name

    header = '<html><head><title>Icon</title></head><body>'

    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{}">
              <input type="submit" value="submit">
              </form>
              <p> You look like a:
              <img src="/a/a.png"/>
              '''.format(name)
              
    footer = '</body></html>'

    return header + body + footer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')