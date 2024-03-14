from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/directors")
def directors():
    return render_template("directors.html")


@app.route("/all_films")
def all_films():
    return render_template("all_films.html")

@app.route("/my_attempts")
def my_attempts():
    return render_template("my_attempts.html")


@app.route("/directors/<name>")
def redirect_page(name):
    return render_template(f"/directors/{name}.html")


@app.route("/all_films/<film>")
def redirect_film(film):
    return render_template(f"/all_films/{film}.html")






if __name__ == '__main__':
    app.run(debug=True)