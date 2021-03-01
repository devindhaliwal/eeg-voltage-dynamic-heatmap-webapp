from flask import Flask, render_template

app = Flask(__name__, template_folder='Templates')

@app.route("/")
def home():
    return render_template("figure.html")

if __name__ == "__main__":
    app.run(debug=False)
