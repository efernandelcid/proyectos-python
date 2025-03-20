
# Explicación del Código: Implementación de una Cola con Prioridad en Python

## Introducción
Este código implementa una estructura de datos de cola (queue) con soporte para prioridades. Se maneja mediante dos listas internas: una para elementos de alta prioridad y otra para elementos normales.

## Implementación de la Clase `Queue`
### Constructor `__init__`
```python
def __init__(self):
    self.cola_alta_prioridad = []
    self.cola_normal = []         
```
El constructor inicializa dos listas:
- `cola_alta_prioridad`: almacena elementos de alta prioridad.
- `cola_normal`: almacena elementos de prioridad normal.

### Método `enqueue`
```python
def enqueue(self, element, priority=False):
    if priority:
        self.cola_alta_prioridad.append(element)  
    else:
        self.cola_normal.append(element)         
```
Este método permite agregar un elemento a la cola. Si el parámetro `priority` es `True`, el elemento se añade a `cola_alta_prioridad`; de lo contrario, se añade a `cola_normal`.

### Método `dequeue`
```python
def dequeue(self):
    if self.cola_alta_prioridad:
        return self.cola_alta_prioridad.pop(0)  
    elif self.cola_normal:
        return self.cola_normal.pop(0)         
    else:
        return None
```
Este método extrae y devuelve el primer elemento en la cola. Si hay elementos en `cola_alta_prioridad`, se atienden primero. Si está vacía, se atiende a `cola_normal`. Si ambas listas están vacías, devuelve `None`.

### Método `front`
```python
def front(self):
    if self.cola_alta_prioridad:
        return self.cola_alta_prioridad[0]  
    elif self.cola_normal:
        return self.cola_normal[0]         
    else:
        return None
```
Este método devuelve el primer elemento en la cola sin eliminarlo.

### Método `is_empty`
```python
def is_empty(self):
    return not self.cola_alta_prioridad and not self.cola_normal
```
Devuelve `True` si ambas colas están vacías y `False` en caso contrario.

### Método `size`
```python
def size(self):
    return len(self.cola_alta_prioridad) + len(self.cola_normal)
```
Devuelve el número total de elementos en la cola.

## Ejemplo 1: Gestión de Tareas
```python
queue = Queue()
queue.enqueue("Tarea normal 1")
queue.enqueue("Tarea urgente 1", priority=True)
queue.enqueue("Tarea normal 2")

print("Frente de la cola:", queue.front())
print("Atendiendo:", queue.dequeue())
print("Atendiendo:", queue.dequeue())
print("Tamaño de la cola:", queue.size())
```
**Explicación:**
1. Se encola una tarea normal.
2. Se encola una tarea urgente (prioritaria).
3. Se encola otra tarea normal.
4. Se consulta el primer elemento de la cola (`front`).
5. Se atienden las tareas siguiendo la prioridad.
6. Se imprime el tamaño de la cola al final.

**Salida esperada:**
```
Frente de la cola: Tarea urgente 1
Atendiendo: Tarea urgente 1
Atendiendo: Tarea normal 1
Tamaño de la cola: 1
```

## Ejemplo 2: Atención al Cliente
```python
queue = Queue()
queue.enqueue("Cliente regular 1")
queue.enqueue("Cliente VIP 1", priority=True)
queue.enqueue("Cliente regular 2")
queue.enqueue("Cliente VIP 2", priority=True)
queue.enqueue("Cliente regular 3")

print("Frente de la cola:", queue.front())
print("Atendiendo:", queue.dequeue())
print("Atendiendo:", queue.dequeue())
print("Atendiendo:", queue.dequeue())
print("Atendiendo:", queue.dequeue())
print("Tamaño de la cola:", queue.size())
```
**Explicación:**
1. Se encola un cliente regular.
2. Se encola un cliente VIP (prioritario).
3. Se encola otro cliente regular.
4. Se encola otro cliente VIP (prioritario).
5. Se encola un tercer cliente regular.
6. Se atienden los clientes siguiendo la prioridad.

**Salida esperada:**
```
Frente de la cola: Cliente VIP 1
Atendiendo: Cliente VIP 1
Atendiendo: Cliente VIP 2
Atendiendo: Cliente regular 1
Atendiendo: Cliente regular 2
Tamaño de la cola: 1
```

## Conclusión
Esta implementación permite gestionar colas con prioridad de forma eficiente, asegurando que los elementos de alta prioridad sean atendidos antes que los normales. Es útil en aplicaciones como gestión de tareas y atención al cliente.


