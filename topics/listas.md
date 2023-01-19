# Metodos usados en Listas 🐍

## append
Método usado para insertar elementos  a una lista. El elemento insertado ocupa la última posición de la lista

```
lista.append(element)
```

## insert
Método para insertar elementos a una lista. Este método permite establecer la posicion del elemento 
```
lista.insert(int,elemento)
```

## extend
Método usado para insertar un iterable lista, set o tupla en la lista. Estos elementos se posicionarán al final de la lista.
```
lista.extend(iterable)
```


## pop
Método para remover un elemento de una lista, indicando la posición del elemento
```
lista.pop(int)
```

## remove
Método usado para remover un elemento de una lista, dando como parámetro el valor del elemento. Por ejemplo en la lista: ```['banana','apple','orange']```, se remueve el elemento ```apple```
```
lista.remove('apple')
```

## sort | reverse
El método sort se usa para ordenar una lista. En listas de texto, ordena por la primera letra del abecedario y los ordena en orden alfabético. Es CASE SENSITIVE, lo que quiere decir que le da prioridad a los texto que empiezan con mayúsculas. En numeros, los ordena del menor al mayor.
```
lista.sort()
```

Cuando la lista tiene una mezcla de tipos de datos, esta no se puede ordenar
```
TypeError: '<' not supported between instances of 'int' and 'str'
```
El método reverse se usa para cambiar el orden de la lista. Lo interesante es que solo ordena de forma inversa el orden inicial de la lista
```
numeric = [3,5,8,12,0,56,34,1] # orden inicial
numeric.reverse()

# output
[1, 34, 56, 0, 12, 8, 5, 3]
```
Si se requiere que una lista numérica se ordene del número mayor al menor, primero se debe usar el método *sort()*, para ordenar los valores numéricos del menor a mayor y después ordenarlo de forma inversa con el método *reverse()*

## copy
El método copy, permite copiar la lista en una nueva variable
```
new_list = list.copy()
```
## count
El método count retorna el numero de veces que un elemento está presente en una lista

```
list.count(e)
```
The *e* represents an element

## index
El método index retorna la posición de un elemento
```
list.index(e)
```
La letra *e* representa al elemento dado

# Manejo de archivos de texto 🗒

## with
El comando with es un manejador contextual que ayuda a proteger los arhivos consultados si el sistema falla y cierra inesperadamente. 

## open()

Open es una función que se encarga de abrir archivos y puede recibir varios parámetros. Como mínimo debe recibir 2: 

1. Ruta del archivo
2. Modo de apertura

### open("ruta/del/archivo","modo de apertura") 

## Sintaxis

1. with -> para 
2. open() -> dos parámetros como mínimo: ruta del archivo, modo de apertura
3. as -> asignar el archivo a una variable
4. variable
5. ":" -> terminar con ":"

    ### with open("ruta/del/archivo", "r") as f:

```
with open("ruta del archivo","modo de apertura->r,w,a") as f:
```
