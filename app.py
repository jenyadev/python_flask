from flask import Flask
from flask import redirect

app = Flask (__name__)

@app.route('/')
def home_page():
    name = 'jenya'
    return f'<html><h1><b>welcome to flask! {name}</b></h1></html>'


@app.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page

@app.route('/w3')
def goto_w3():
    return redirect ('https://www.w3schools.com/')


app.run()
