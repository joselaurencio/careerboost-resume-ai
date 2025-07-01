from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # you will grab form data here later
        return "Form submitted!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
