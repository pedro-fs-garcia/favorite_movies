from flask import Flask, render_template, redirect, request, url_for
import json, database
import random

app = Flask(__name__)


directors_films = {director:database.get_directors_movies(director) for director in database.get_directors()}
directors_images = database.get_images("directors")
films_images = database.get_images("films")
perguntas = database.get_questions()
all_films = [i for j in directors_films.values() for i in j]
# directors_films = json.load(open("./static/directors_films.json", encoding = "UTF-8"))
# perguntas = json.load(open("./static/questions.json", encoding = "UTF-8"))

@app.route("/")
def home_page():
    return redirect ("/home")


@app.route("/<name>")
def get_page(name):
    page = name
    if name == "home":
        page = "index"
    return render_template(f"{page}.html", directors_films = directors_films, directors_images = directors_images, films_images = films_images, perguntas=perguntas)


@app.route("/get_answer", methods=["POST", "GET"])
def get_answer():
    respostas={}
    acertos = 0
    for i in range(1, len(perguntas)+1):
        try:
            respostas[f"answer{i}"] = request.form[f"answer{i}"]
        except KeyError:
            respostas[f"answer{i}"] = ""
    for i in range(1, len(perguntas)+1):
        if perguntas[i][5] == respostas[f"answer{i}"]:
            acertos += 1
    erros = len(perguntas) - acertos
    porcentagem = f"{(acertos/len(perguntas) * 100):.2f}%"
    return render_template("result.html", acertos=acertos, erros=erros, porcentagem=porcentagem)


@app.route("/get_suggestion", methods=["POST", "GET"])
def get_suggestion():
    filme = request.form.get("movie_suggestion")
    diretor = request.form.get("director_suggestion")
    ano = request.form.get("year_suggestion")
    database.write_suggestion(filme, diretor, ano)
    return redirect("/sugestoes")


@app.route("/rating", methods=["GET", "POST"])
def rating():
    films = random.sample(all_films, 2)
    film1 = [films[0], database.get_film_id(films[0]), films_images[films[0]]]
    film2 = [films[1], database.get_film_id(films[1]), films_images[films[1]]]
    return render_template("rating.html", film1 = film1, film2 = film2)


@app.route("/get_rating", methods=["GET", "POST"])
def get_rating():
    if request.method == 'POST':
        k = 24
        ans = [int(i) for i in request.form.get("chooseoption").split(",")]
        winner, loser = ans[0], ans[2]
        RA = database.get_rating(winner)
        RB = database.get_rating(loser)
        EA = 1/(1+10**((RB-RA)/400))
        EB = 1/(1+10**((RA-RB)/400))
        new_RA = RA + k*(1 - EA)
        new_RB = RB + k*(0 - EB)
        database.update_rating(winner, new_RA)
        database.update_rating(loser, new_RB)
        films = random.sample(all_films, 2)
        film1 = [films[0], database.get_film_id(films[0]), films_images[films[0]]]
        film2 = [films[1], database.get_film_id(films[1]), films_images[films[1]]]
        # if ans[1] == 1:
        #     winner_name = database.get_film_name(winner)
        #     film1 = [winner_name, winner, films_images[winner_name]]
        #     film2 = random.choice(all_films)
        #     while film2 == film1[0]:
        #         film2 = random.choice(all_films)
        #     film2 = [film2, database.get_film_id(film2), films_images[film2]]
        # else:
        #     winner_name = database.get_film_name(winner)
        #     film2 = [winner_name, winner, films_images[winner_name]]
        #     film1 = random.choice(all_films)
        #     while film1 == film2[0]:
        #         film1 = random.choice(all_films)
        #     film1 = [film1, database.get_film_id(film1), films_images[film1]]
        # return render_template("rating.html", film1 = film1, film2 = film2, cont = True)
        return render_template("rating.html", film1 = film1, film2 = film2, cont = True)
    else:
        return redirect("/rating")


@app.route("/all_ratings")
def all_ratings():
    films_ratings = []
    for film in all_films:
        film_id = database.get_film_id(film)
        film_rating = database.get_rating(film_id)
        films_ratings.append((film, film_rating))
    # films_ratings.sort(key = lambda x: x[1], reverse=True)
    return render_template("all_ratings.html", films_ratings = films_ratings)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug = True)