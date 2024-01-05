from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

app.config['SECRET_KEY'] = 'tcnb65421@@'


@app.route('/', methods=['GET', 'POST'])
def main():
    

        
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def session():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)









