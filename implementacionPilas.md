## PROGRAMACION 3 TAREA 1

Edgar Fernando Zuñiga Del Cid 2890-23-25237

# Implementación de una Pila y Aplicaciones en Python

## 1. Clase `Stack`

La clase `Stack` se implementa sin utilizar estructuras predefinidas como `list`, `deque` o `queue.LifoQueue`. Su objetivo es representar una pila con las siguientes operaciones:

- **`push(element)`**: Agrega un elemento a la pila.
- **`pop()`**: Elimina y devuelve el elemento superior.
- **`peek()`**: Devuelve el elemento superior sin eliminarlo.
- **`is_empty()`**: Retorna `True` si la pila está vacía.
- **`size()`**: Retorna el número de elementos en la pila.

```python
class Stack:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return self.items == [] 

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        return self.items.pop() 

    def peek(self):
        return self.items[-1] if not self.is_empty() else None 

    def size(self):
        return len(self.items) 
```

## 2. Validación de expresiones matemáticas (Paréntesis balanceados)

Esta función verifica si una expresión matemática tiene los paréntesis correctamente balanceados. Utiliza una pila para almacenar los paréntesis de apertura y los compara con los de cierre:

```python
def validarExpresion(expresion):
    pila = Stack()
    for char in expresion:
        if char == '(':
            pila.push(char)
        elif char == ')': 
            if pila.is_empty():
                return False
            pila.pop()
    return pila.is_empty()
```

### **Ejemplo de uso:**
```python
expresionValida = "(3 + 2) * (8 / 4)"
expresionInvalida = "((3 + 2) * (8 / 4"

print(validarExpresion(expresionValida))  # True
print(validarExpresion(expresionInvalida))  # False
```

## 3. Conversión de Notación Infija a Postfija

La conversión de notación infija a postfija se realiza utilizando una pila. Se siguen estas reglas:

1. Los operandos (números) se agregan directamente a la salida.
2. Los operadores se apilan según su precedencia.
3. Los paréntesis izquierdos `(` se apilan.
4. Al encontrar un paréntesis derecho `)`, se desapilan operadores hasta encontrar `(`.
5. Al final, se desapilan todos los operadores restantes.

```python
def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    salida = []
    pila = Stack()
    
    tokens = expresion.split()

    for token in tokens:
        if token.isnumeric():  # Si es un número, se añade a la salida
            salida.append(token)
        elif token in precedencia:  # Si es un operador
            while (not pila.is_empty() and pila.peek() in precedencia and 
                   precedencia[pila.peek()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
        elif token == '(':  # Si es un paréntesis izquierdo, se apila
            pila.push(token)
        elif token == ')':  # Si es un paréntesis derecho, vaciar hasta '('
            while not pila.is_empty() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar el '('

    while not pila.is_empty():  # Vaciar lo que quede en la pila
        salida.append(pila.pop())

    return " ".join(salida)
```

### **Ejemplo de uso:**
```python
expresionInfija = "3 + 5 * ( 2 - 8 )"
print(infija_a_postfija(expresionInfija))  # Salida esperada: "3 5 2 8 - * +"
```

## 4. Conclusión

Este código implementa una pila desde cero y la aplica a dos problemas comunes:
1. **Validación de paréntesis balanceados** en expresiones matemáticas.
2. **Conversión de expresiones en notación infija a postfija**.

Ambas soluciones aprovechan la estructura de la pila para manejar la jerarquía y secuencia de los elementos de manera eficiente.


## VIDEO



## BIBLIOGRAFIA 

https://docs.hektorprofe.net/python/colecciones-de-datos/pilas/
https://runestone.academy/ns/books/published/pythoned/BasicDS/ImplementacionDeUnaPilaEnPython.html
