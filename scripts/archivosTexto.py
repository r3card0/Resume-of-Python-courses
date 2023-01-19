# función read crea una lista a partir de un archivo .csv
def read():
    lista_vacia = []
    with open("./Text-Files/category.csv","r", encoding="utf-8") as f:
        for line in f:
            lista_vacia.append(line)

    print(lista_vacia)

# función write creá un archivo  partir de una lista
def write():
    lista_nombre=["Goku,", "Batman,", "Venom,", "spider-man,","Ironman,","Rocío@@"]
    with open("./Text-Files/nombres3.csv","w", encoding="utf-8") as f:
        for nombres in lista_nombre:
            f.write(nombres)
            #f.write("\n") # para indicar un salto de línea


def run():
    write()


if __name__ == "__main__":
    run()