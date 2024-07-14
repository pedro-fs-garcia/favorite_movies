import mysql.connector
import sys
import config

configure = {"user": f"{config.DB_USER}", "password": f"{config.DB_PASSWORD}", "host": f"{config.DB_HOST}", "database": f"{config.DB_NAME}"}


def get_directors_movies(director):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            director_id = get_director_id(director)
            query = "SELECT film FROM films WHERE director = %s"
            cur.execute(query, (director_id,))
            res = cur.fetchall()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()
    return [i[0] for i in res]


def get_directors():
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT director FROM directors"
            cur.execute(query)
            res = cur.fetchall()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()
    return [i[0] for i in res]


def get_director_description(diretor):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = f"SELECT description FROM directors WHERE director='{diretor}'"
            cur.execute(query)
            res = cur.fetchone()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()
    return res[0]


def get_images(table):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            if table == "directors":
                query = "SELECT director, image_file FROM directors"
            elif table == "films":
                query = "SELECT film, image_file FROM films"
            cur.execute(query)
            res = cur.fetchall()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()
    return {name:image for name, image in res}


def write_suggestion(movie, director, year):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "INSERT INTO suggestions (suggestion_film, suggestion_director, suggestion_year) VALUES (%s, %s, %s)"
            values = (movie, director, year)
            cur.execute(query, values)
            con.commit()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()


def get_film_id(film):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT film_id FROM films WHERE film = %s"
            cur.execute(query, (film,))
            id = cur.fetchone()
    except OSError as e:
        print(e)
        return False
    finally:
        return id[0]
    

def get_film_name(film_id=int):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT film FROM films WHERE film_id = %s"
            cur.execute(query, (film_id, ))
            name = cur.fetchone()
    except OSError as e:
        print(e)
        return False
    finally:
        return name[0]


def get_director_id(nome=str):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT director_id FROM directors WHERE director = %s"
            values = nome.title()
            cur.execute(query, (values,))
            id = cur.fetchone()
    except OSError as e:
        print(e)
        return False
    finally:
        if cur: cur.close()
        if con: con.close()
    return id[0]


def write_director_to_database(name, description):
    name = name.title()
    image_file = f"{name.lower().replace(' ', '_')}.jpg"
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "INSERT INTO directors (director, description, image_file) VALUES (%s, %s, %s)"
            values = (name, description, image_file)
            cur.execute(query, values)
            con.commit()
    except OSError as e:
        print(e)
        return None
    finally:
        if cur: cur.close()
        if con: con.close()


def write_film_to_database(film=str, director=str, year=int):
    image_file, rating = f"{film.lower().replace(' ', '_')}.jpg", 1400
    film = film.title()
    director_id = get_director_id(director.capitalize())
    if not director_id:
        write_director_to_database(director, None)
        director_id = get_director_id(director.capitalize())
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "INSERT INTO films (film, director, year, image_file, rating) VALUES (%s, %s, %s, %s, %s)"
            values = (film, director_id, year, image_file, rating,)
            cur.execute(query, values)
            con.commit()
    except OSError as e:
        print(e)
        return False
    finally:
        if cur: cur.close()
        if con: con.close()
    return True


def get_questions():
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT * FROM questions"
            cur.execute(query)
            questions = cur.fetchall()
    except OSError as e:
        print(e)
        return False
    finally:
        if cur: cur.close()
        if con: con.close()
    return {info[0] : info[1:] for info in questions}


def get_rating(film_id):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "SELECT rating FROM films WHERE film_id = %s"
            values = film_id
            cur.execute(query,(values,))
            res = cur.fetchone()
    except OSError as e:
        print(e)
        return False
    finally:
        if cur: cur.close()
        if con: con.close()
    return res[0]



def update_rating(film_id, new_rating):
    try:
        con = mysql.connector.connect(**configure)
        if con.is_connected():
            cur = con.cursor()
            query = "UPDATE films SET rating = %s WHERE film_id = %s"
            cur.execute(query, (new_rating, film_id,))
            con.commit()
    except OSError as e:
        print(e)
        return False
    finally:
        if cur: cur.close()
        if con: con.close()


