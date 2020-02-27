f= open("restoran.txt","r")
bilosto= f.readlines()
f.close()

class Restoraniste:
    def __init__(self, name, street):
        self.name = name
        self.street = street
for anja in bilosto:
    single_restoran = anja.split(", ")
    name = single_restoran[0]
    street = single_restoran[1].replace("\n", "")
    restoran1 = Restoraniste(name, street)

    html_file = open("index.html","a")
    html_file.write("<h1>{} {}</h1>\n".format(name, street))
    print(name, street)