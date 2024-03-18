import json
# dir_file = open("C:\\Users\\Home\\Documents\\programacao\\python\\file_handle_exercises\\filmes.json", "r", encoding = "utf-8")
# films = json.load(dir_file)
# print(films["Lars Von Trier"])




# directors = json.load(open("directors_films.json", "r"))
# directors["akira_kurosawa"] = "the bad sleeps well, high and low, the seven samurai, yojimbo, sanjuro, rashomon".replace(" ","_").split(",_")

# with open("directors_films.json", "a") as file:
#     json.dump(directors["akira_kurosawa"],file)


# sk = "the shining,eyes wide shut".lower().replace(" ", "_").split(",")
# with open("directors_films.json", "a") as file:
#     json.dump(sk, file)


directors = json.load(open("templates/directors/directors_films.json", "r"))
for name in directors:
    for poster in directors[name]:
        print(poster.replace(" ", "_"))
