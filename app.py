from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/directors")
def directors():
    with open('./templates/directors/names.txt') as file:
        for line in file: names = line.split()
    return render_template("directors.html", names=names)


@app.route("/all_films")
def redirect_film():
    with open("./templates/directors/films.txt", "r") as file:
        for line in file: films = line.split()
    return render_template("all_films.html", films=films)


@app.route("/my_attempts")
def my_attempts():
    return render_template("my_attempts.html")


if __name__ == '__main__':
    app.run(debug=True)