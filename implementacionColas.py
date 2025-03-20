class Queue:
    def __init__(self):
        self.cola_alta_prioridad = [] 
        self.cola_normal = []         

    def enqueue(self, element, priority=False):
        if priority:
            self.cola_alta_prioridad.append(element)  
        else:
            self.cola_normal.append(element)         

    def dequeue(self):
        if self.cola_alta_prioridad:
            return self.cola_alta_prioridad.pop(0)  
        elif self.cola_normal:
            return self.cola_normal.pop(0)         
        else:
            return None

    def front(self):
        if self.cola_alta_prioridad:
            return self.cola_alta_prioridad[0]  
        elif self.cola_normal:
            return self.cola_normal[0]         
        else:
            return None

    def is_empty(self):
        return not self.cola_alta_prioridad and not self.cola_normal

    def size(self):
        return len(self.cola_alta_prioridad) + len(self.cola_normal)

#Ejemplo gestion de tareas
queue = Queue()
queue.enqueue("Tarea normal 1")
queue.enqueue("Tarea urgente 1", priority=True)
queue.enqueue("Tarea normal 2")

print("Frente de la cola:", queue.front())
print("Atendiendo:", queue.dequeue())
print("Atendiendo:", queue.dequeue())
print("Tamaño de la cola:", queue.size())

#Ejemplo atencion al cliente
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
