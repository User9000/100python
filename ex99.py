

#create a web app in where you add lines same as ex98 but with a webapp

from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form['data_ui']
    file=open("data_from_flask.txt","a+")
    file.write(data + "\n")
    file.close()
    data_ui =None
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)





