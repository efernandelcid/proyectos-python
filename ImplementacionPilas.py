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
        return self.items[-1] 

    def size(self):
        return len(self.items) 
    

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


def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    salida = []
    pila = Stack()
    
    tokens = expresion.split()

    for token in tokens:
        if token.isnumeric():  
            salida.append(token)
        elif token in precedencia:  
            while (not pila.is_empty() and pila.peek() in precedencia and 
                   precedencia[pila.peek()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
        elif token == '(':  
            pila.push(token)
        elif token == ')':  
            while not pila.is_empty() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  

    while not pila.is_empty():  
        salida.append(pila.pop())

    return " ".join(salida)

expresionValida = "( 3 + 2 ) * ( 8 / 4 )"
expresionInvalida = "( ( 3 + 2 ) * ( 8 / 4 "

print("Validación de paréntesis:")
print(validarExpresion(expresionValida))  
print(validarExpresion(expresionInvalida))  
expresionInfija = "3 + 5 * ( 2 - 8 )"
print("Conversión a postfija:")
print(infija_a_postfija(expresionInfija)) 
