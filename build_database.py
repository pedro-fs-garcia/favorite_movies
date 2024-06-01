from database import configure
import mysql.connector
import json

directors_films = json.load(open("./static/directors_films.json", encoding = "UTF-8"))
perguntas = json.load(open("./static/questions.json", encoding = "UTF-8"))

def write_directors():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()

    query = "INSERT INTO diretores (diretor, descricao) VALUES (%s, %s)"
    for diretor in directors_films.keys():
        values = (diretor, None)
        cur.execute(query, values)
        con.commit()

    cur.close()
    con.close()


def write_movies():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()

    query = "INSERT INTO filmes (filme, diretor, ano) VALUES (%s, %s, %s)"
    for diretor, filmes in directors_films.items():
        for filme in filmes:
            values = (filme, diretor, None)
            cur.execute(query, values)
            con.commit()
    cur.close()
    con.close()


def write_questions():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()

    query = "INSERT INTO perguntas (id, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, correta, dica) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for key, value in perguntas.items():
        values = (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6])
        cur.execute(query, values)
        con.commit()
    cur.close()
    con.close()

write_directors()
write_movies()
write_questions()