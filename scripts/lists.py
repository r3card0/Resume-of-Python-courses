def description():
    desc = """
    Este programa muestra los metodos
    de las listas en Python 🐍
    """
    return desc

# given an empty list

tectonic_plates = []

# function to add an element in a list : append
def addElement(list:list,string:str):
    list.append(string)
    return list

# function to add an element in a list : insert
def insertElement(list:list,string:str,pos:int):
    list.insert(pos,string)
    return list

def run():
    print(description())
    print(addElement(tectonic_plates, 'North-American plate'))
    print(addElement(tectonic_plates, 'Eurasian plate'))
    print(insertElement(tectonic_plates,'Philipine plate',1))


if __name__ == "__main__":
    run()