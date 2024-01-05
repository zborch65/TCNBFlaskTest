from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

app.config['SECRET_KEY'] = 'tcnb65421@@'


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        busname = request.form['busname']
        busacctnum = request.form['busacctnum']
        print(busname, busacctnum)  # do something here?

        
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def session():
    return render_template('index.html')









