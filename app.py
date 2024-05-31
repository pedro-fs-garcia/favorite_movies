from flask import Flask, render_template, redirect, request, url_for
import json, database


app = Flask(__name__)


directors_films = {director:database.get_directors_movies(director) for director in database.get_directors()}
perguntas = database.get_questions()
# directors_films = json.load(open("./static/directors_films.json", encoding = "UTF-8"))
# perguntas = json.load(open("./static/questions.json", encoding = "UTF-8"))

@app.route("/")
def home_page():
    return redirect ("/home")


@app.route("/<name>")
def get_page(name):
    if name == "home":
        return render_template(f"index.html", directors = directors_films, perguntas=perguntas)

    return render_template(f"{name}.html", directors = directors_films, perguntas=perguntas)


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
        if perguntas[str(i)][5] == respostas[f"answer{i}"]:
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


if __name__ == '__main__':
    app.run()