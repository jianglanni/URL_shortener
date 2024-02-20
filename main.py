from flask import Flask, render_template, redirect, request
from shortener import Shortener

app = Flask(__name__, template_folder="")
shortener1 = Shortener()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form["url"]
    temp_shorter = Shortener()
    short_url = temp_shorter.shorten(url)
    return render_template("result.html", short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    temp_shorter = Shortener()
    complete_url = temp_shorter.get_url(short_url)
    if complete_url is None:
        return 'URL not found'
    if complete_url[:4] != "http":
        complete_url = "http://" + complete_url
    return redirect(complete_url)

if __name__ == '__main__':
    #DO not remove any Code below
    port = 3000
    app.run(debug=True, host="0.0.0.0", port=port)
