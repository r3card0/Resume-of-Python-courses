def description():
    desc = """
    Este programa muestra los metodos
    de las listas en Python 🐍
    """
    return desc

# given an empty list

tectonic_plates = []

plates = ['Australian-Indian plate','Scotia plate','Antartic plate']

numeric = [3,5,8,12,0,56,34,1]

# function to add an element in a list : append
def addElement(list:list,string:str):
    list.append(string)
    return list

# function to add an element in a list : insert
def insertElement(list:list,string,pos:int):
    list.insert(pos,string)
    return list

# function to add in iterable in a list
def addIterable(list:list,iterable):
    list.extend(iterable)
    return list

# function to remove an element: pop
def removeElement(list:list,pos:int):
    list.pop(pos)
    return list

# function to remove an element: remove
def removeElementRemove(list:list,string):
    list.remove(string)
    return list

# function to sort elements of a list: sort
def sortList(list):
    list.sort()
    return list

# function to sort elements of a list in reverse order: reverse
def sortReverseList(list):
    list.reverse()
    return list

# function to copy a list: copy
def copyList(list):
    new_list = list.copy()
    return new_list

# function to count an element: count
def countElement(list:list, e): # e means an element
    x = list.count(e)
    return x

def run():
    print(description())
    print(addElement(tectonic_plates, 'North-American plate'))
    print(addElement(tectonic_plates, 'Eurasian plate'))
    print(insertElement(tectonic_plates,'Philipine plate',1))
    print(removeElement(tectonic_plates,2))
    print(insertElement(tectonic_plates,'South-American plate',0))
    print(removeElementRemove(tectonic_plates,'North-American plate'))
    print(addIterable(tectonic_plates,plates))
    print(sortList(tectonic_plates))
    print(addIterable(tectonic_plates,numeric))
    # print(sortList(tectonic_plates)) # TypeError: '<' not supported between instances of 'int' and 'str'
    print(sortReverseList(numeric))
    print(sortList(numeric))
    print(sortReverseList(numeric))
    print(copyList(plates))
    addIterable(plates,plates)
    print(countElement(plates,'Australian-Indian plate'))


if __name__ == "__main__":
    run()