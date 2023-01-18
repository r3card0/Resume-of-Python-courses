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
def insertElement(list:list,string,pos:int):
    list.insert(pos,string)
    return list

# function to remove an element: pop
def removeElement(list:list,pos:int):
    list.pop(pos)
    return list

# function to remove an element: remove
def removeElementRemove(list:list,string):
    list.remove(string)
    return list

def run():
    print(description())
    print(addElement(tectonic_plates, 'North-American plate'))
    print(addElement(tectonic_plates, 'Eurasian plate'))
    print(insertElement(tectonic_plates,'Philipine plate',1))
    print(removeElement(tectonic_plates,2))
    print(insertElement(tectonic_plates,['Nazca plate','South-American plate'],0))
    print(removeElementRemove(tectonic_plates,'North-American plate'))


if __name__ == "__main__":
    run()