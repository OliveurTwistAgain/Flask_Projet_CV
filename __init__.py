from flask import Flask,render_template

app = Flask(__name__) #creating flask app name


@app.route('/')
def resume_2():
    return render_template("resume_2.html")


if(__name__ == "__main__"):
    app.run()
