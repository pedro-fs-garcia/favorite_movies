from database import configure
import database
import mysql.connector
import json

directors_films = json.load(open("./static/directors_films.json", encoding = "UTF-8"))
perguntas = json.load(open("./static/questions.json", encoding = "UTF-8"))


def write_directors():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()
    query = "INSERT INTO directors (director, description, image_file) VALUES (%s, %s, %s)"
    for diretor in directors_films.keys():
        image = f"{diretor}.jpg"
        diretor = diretor.replace("_", " ").title()
        values = (diretor, None, image)
        cur.execute(query, values)
        con.commit()

def get_director_id_by_name(name):
    con = mysql.connector.connect(**configure)
    cur = con.cursor()
    query = "SELECT director_id FROM directors WHERE director = %s"
    cur.execute(query, (name,))
    result = cur.fetchone()
    return result[0]

def write_movies(directors_films):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()

            query = "INSERT INTO films (film, director, year, image_file, rating) VALUES (%s, %s, %s, %s, %s)"
            for diretor, filmes in directors_films.items():
                for filme in filmes:
                    director = diretor.replace("_", " ").title()
                    director_id = get_director_id_by_name(director)
                    if director_id is None:
                        print(f"Diretor '{director}' não encontrado.")
                        continue  # Pular este filme se o diretor não for encontrado

                    image = f"{filme.replace(' ', '_')}.jpg"
                    rating = 1400
                    values = (filme.replace("_", " ").capitalize(), director_id, None, image, rating)
                    cur.execute(query, values)
                    con.commit()
            print("Filmes inseridos com sucesso.")
    except OSError as e:
        print(f"Erro ao inserir dados no MySQL: {e}")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def create_questions_table():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()
    query = '''CREATE TABLE questions (
                question_id int NOT NULL AUTO_INCREMENT UNIQUE, 
                question VARCHAR(255) NOT NULL, 
                option_a VARCHAR(255), 
                option_b VARCHAR(255), 
                option_c VARCHAR(255), 
                option_d VARCHAR(255), 
                answer VARCHAR(50), 
                hint VARCHAR(255), 
                PRIMARY KEY (question_id)
            )'''
    cur.execute(query), con.commit(), cur.close(), con.close()


def write_questions():
    con = mysql.connector.connect(**configure)
    cur = con.cursor()
    query = "INSERT INTO questions (question_id, question, option_a, option_b, option_c, option_d, answer, hint) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for key, value in perguntas.items():
        values = (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6])
        cur.execute(query, values)
        con.commit()

