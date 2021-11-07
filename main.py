from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/calc",methods=["POST", "GET"])
def calc():
    if request.method == "POST":

        text = request.form['input_form']
        return str(eval(f"{text}"))

    return render_template("calc.html")


if __name__ == "__main__":
    app.run(debug=True)