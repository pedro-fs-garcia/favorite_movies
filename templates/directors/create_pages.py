names = open("names.txt", "r")
for i in names:
    d = i
print(i)

for name in i.split():
    with open(f"{name}.html", "w") as file:
        file.write("{% extends 'base.html' %}\n{% block title %}" + f"{name.replace('_', ' ')}" + "{% endblock %}\n{% block page_title %}My Favorite Directors{% endblock %}\n{% block header_image %}"+ f"<header class='header_image' style='background-image:url(/static/images/{name}.jpg); background-position: center -160px'></header>" +"{% endblock %}\n{% block content %}\n"+f"<h2>{name.replace('_', ' ').title()}</h2>" + "{% endblock %}")

