from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fill-form')
def about():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdMuP48yiKMjd0R5DX2kxpGBubb0wlLtwXdsopeOuOGEngT-A/viewform?usp=header")