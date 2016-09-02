from flask import Flask, render_template, request, url_for, redirect
from blinkstick import blinkstick
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

# you need to have methods POST, due to the type of form sent by the HTML Buttons, otherwise nothing works!

@app.route("/on", methods=['POST'])
def blinkon():
    for bstick in blinkstick.find_all():
    		bstick.set_random_color()
    print('status: blinkstick on')
    return redirect("/")

@app.route("/off", methods=['POST'])
def blinkoff():
    for bstick in blinkstick.find_all():
             bstick.turn_off()
    print('status: blinkstick off')    
    return redirect("/")


@app.route("/preset", methods=['POST'])
def blinkpreset():
    for bstick in blinkstick.find_all():
                 bstick.set_color(name=request.form['color'])
    print('status: blinkstick color - ' + request.form['color'])   
    return redirect("/")


@app.route("/custom", methods=['POST'])
def blinkcustom():
    for bstick in blinkstick.find_all():
                 bstick.set_color(hex=request.form['color'])
    print('status: blinkstick color - ' + request.form['color'])    
    return redirect("/")


if __name__ == "__main__":
    app.run()