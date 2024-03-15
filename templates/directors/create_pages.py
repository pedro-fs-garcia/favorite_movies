names = open("names.txt", "r")
for i in names:
    d = i

print(d)

# for name in d.split():
#     with open(f"{name}.html", "w") as file:
#         file.write("{% extends 'base.html' %}\n{% block title %}" + f"{name.replace('_', ' ')}" + "{% endblock %}\n{% block page_title %}My Favorite Directors{% endblock %}\n{% block header_image %}"+ f"<header class='header_image' style='background-image:url(/static/images/{name}.jpg); background-position: center -160px'></header>" +"{% endblock %}\n{% block content %}\n"+f"<h2>{name.replace('_', ' ').title()}</h2>" + "{% endblock %}")

for name in d.split():
    with open("collapsable.txt", "a") as file:
        file.write(f'''<details>
        <summary><h3 style="margin:2px">{name.replace("_", " ").title()}</h3>
            <div class="director_summary">
            <div>
                <img class="director_image" src="/static/images/{name}.jpg">
            </div>
            <div style="margin:auto 15px;">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestiae repellendus perspiciatis natus reiciendis eaque repudiandae consectetur corrupti sequi blanditiis maiores, necessitatibus magnam, asperiores recusandae, aliquam esse? Quaerat quos aperiam reiciendis.</div>
        </div>
        </summary>
        <div class="movie_posters">his main movies</div>
    </details><br>\n\n''')