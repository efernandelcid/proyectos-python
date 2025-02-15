import random  # La libreria se utiliza para generar numeros aleatorios ya que nos ayudaran a generar los nombres y los ids de los usuarios
import string  # La libreria se utiliza para generar nombres aleatorios de los usuarios 
import timeit # La libreria se utiliza para medir el tiempo de ejecucion de nuestro programa

usuario = { # Se crea un diccionario con los datos del usuario como ejemplo de lo que generaremos
    "id": 1,
    "Nombre": "Juan",
    "Edad": 25,
}
print("id del usuario",usuario["id"])
print("Nombre del usuario",usuario["Nombre"])
print("Edad del usuario",usuario["Edad"])

def generar_nombre(): # Se crea la funcion que ayudara a generar los nombres aleatorios 
    longitud_nombre = random.randint(5, 10) # se genera un numero aleatorio entre 5 y 10 para la longitud del nombre
    return ''.join(random.choices(string.ascii_letters, k=longitud_nombre)) # Esto nos regresa el nombre aleatorio generado con la longitud aleatoria

def generar_usuarios(cantidad=100000): # Se crea la funcion que ayudara a generar los usuarios aleatorios con el rango que le indicamos 
    usuarios = []
    for i in range(1, cantidad, +1):  
        usuario = {
            "id": i,
            "Nombre": generar_nombre(),
            "Edad": random.randint(15, 70),  # Se crea un rango de edad entre 15 y 70 años
        }
        usuarios.append(usuario) 
    return usuarios

def busquedad_lineal(usuarios, id): # Se crea la funcion que ayudara a buscar el usuario por id de manera lineal
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None

def busquedad_binaria(usuarios, id): # Se crea la funcion que ayudara a buscar el usuario por id de manera binaria
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

usuarios = generar_usuarios() # Se genera la lista de usuarios aleatorios

id = random.randint(1, 100000) # Se genera un id aleatorio para buscar el usuario

tiempo_lineal = timeit.timeit(lambda: busquedad_lineal(usuarios, id), number=1) # Se mide el tiempo de ejecucion de la busqueda lineal
tiempo_binario = timeit.timeit(lambda: busquedad_binaria(usuarios, id), number=1) # Se mide el tiempo de ejecucion de la busqueda binaria

print(f"Tiempo busqueda lineal: {tiempo_lineal} segundos") # Se imprime el tiempo de ejecucion de la busqueda lineal
print(f"Tiempo busqueda binaria: {tiempo_binario} segundos") # Se imprime el tiempo de ejecucion de la busqueda binaria

usuario = busquedad_lineal(usuarios, id) # Se busca el usuario por id de manera lineal
usuario = busquedad_binaria(usuarios, id) # Se busca el usuario por id de manera binaria

print("usuario encontrado (lineal); ", usuario) # Se imprime el usuario encontrado por busqueda lineal
print("usuario encontrado (binaria); ", usuario) # Se imprime el usuario encontrado por busqueda binaria

