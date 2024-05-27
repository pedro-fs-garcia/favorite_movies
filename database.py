import mysql.connector

config = {"user": "pedro", "password": "", "host": "localhost", "database": "grandes_filmes"}


def write_suggestion(movie, director, year):
    con = mysql.connector.connect(**config)
    cur = con.cursor()

    query = "INSERT INTO sugestoes (filme, diretor, ano) VALUES (%s, %s, %s)"
    values = (movie, director, year)

    cur.execute(query, values)
    con.commit()
    cur.close()
    con.close()


def get_directors_movies(director):
    con = mysql.connector.connect(**config)
    cur = con.cursor()    
    query = f"SELECT filme FROM filmes WHERE diretor='{director}'"
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    con.close()
    return [i[0] for i in res]


def get_directors():
    con = mysql.connector.connect(**config)
    cur = con.cursor()    
    query = f"SELECT diretor FROM diretores"
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    con.close()
    return [i[0] for i in res]


def get_director_description(diretor):
    con = mysql.connector.connect(**config)
    cur = con.cursor()    
    query = f"SELECT descricao FROM diretores WHERE diretor='{diretor}'"
    cur.execute(query)
    res = cur.fetchone()
    cur.close()
    con.close()
    return res[0]


def get_questions():
    con = mysql.connector.connect(**config)
    cur = con.cursor()    
    query = f"SELECT * FROM perguntas"
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    con.close()
    return {i[0]:[i[k] for k in range(1,8)] for i in res}

