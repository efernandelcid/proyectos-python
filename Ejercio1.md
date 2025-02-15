## PROGRAMACION 3 TAREA 1

Edgar Fernando Zuñiga Del Cid 2890-23-25237

# Explicacion de codigo 

## Librerias utilizadas 

El codigo utilizo las librerias:
- 'random' que nos sirvio para poder crear los numeros aleatorios que nos ayudaban a generar el ID y los nombres
- ´ String' esta nos ayudo a generar los nombres utilizando las letras mayusculas y minisculas
- ' Timeit' esta nos ayudo a poder controlar los tiempos que demoraba la maquina en ejecutar el codigo ya sea de forma lineal o forma binaria 

## Creacion de usuario ejemplo

Defini un diccionario para que se entendiera como se iban a generar el usuario ejemplificando:


```python
usuario = {
    "id": 1,
    "Nombre": "Juan",
    "Edad": 25,
}
```

Este se imprimia en pantalla 


## Generacion de Nombres aleatorios 

cree una funcion que pudiera generar nombres entre 5 y 10 caracteres llamando a las librerias 

```python
def generar_nombre():
    longitud_nombre = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters, k=longitud_nombre))
```


## Generacion de Usuarios Aleatorios 

se crea la funcion haciendo una lista de usuarios que contenga un ID y un nombre generado aleatoriamente y edad, en la edad damos un rango para que no se vaya a generar un numero mayor a 100 o que no sea real para ser una edad

```python
def generar_usuarios(cantidad=100000):
    usuarios = []
    for i in range(1, cantidad, +1):
        usuario = {
            "id": i,
            "Nombre": generar_nombre(),
            "Edad": random.randint(15, 70),
        }
        usuarios.append(usuario)
    return usuarios
```
# Busquedad 

## Busquedad Lineal 

la funcion con ayuda de la lista de usuarios recorre la misma uno por uno hasta encontrar el ID deseado 

```python
def busquedad_lineal(usuarios, id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None
```

## Busquedad Binaria 

la funcion binaria, en cambio a la lineal no busca uno por uno si no que divide en mitades la lista hasta encontrar el ID deseado

```python
def busquedad_binaria(usuarios, id):
    inicio = 0
    fin = len(usuarios) - 1
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if usuarios[mitad]["id"] == id:
            return usuarios[mitad]
        elif usuarios[mitad]["id"] < id:
            inicio = mitad + 1
        else:
            fin = mitad - 1
    return None
```
## EJECUCCION DEL PROGRAMA 
1. Se genera una lista de 100,000 usuarios.
2. Se elige un ID aleatorio para buscar.
3. Se mide el tiempo de ejecución de ambas búsquedas.
4. Se imprimen los resultados.

```python
usuarios = generar_usuarios()
id = random.randint(1, 100000)

tiempo_lineal = timeit.timeit(lambda: busquedad_lineal(usuarios, id), number=1)
tiempo_binario = timeit.timeit(lambda: busquedad_binaria(usuarios, id), number=1)

print(f"Tiempo busqueda lineal: {tiempo_lineal} segundos")
print(f"Tiempo busqueda binaria: {tiempo_binario} segundos")
```

## Conclusión

- La **búsqueda lineal** es simple pero ineficiente en listas grandes, ya que revisa uno a uno.
- La **búsqueda binaria** es mucho más rápida, pero requiere que la lista esté ordenada.
- La comparación de tiempos de ejecución permite ver la diferencia de rendimiento entre ambas estrategias.

## VIDEO

- [drive]https://drive.google.com/file/d/1c70xxWrlNpQ2Thpff0lsLEyscctTT9HU/view?usp=drive_link


## BIBLIOGRAFIA 

https://ellibrodepython.com/

https://telefonicatech.com/blog/python-para-todos-5-formas-de-generar-datos-aleatorios

https://j2logo.com/python/generar-numeros-aleatorios-en-python/
