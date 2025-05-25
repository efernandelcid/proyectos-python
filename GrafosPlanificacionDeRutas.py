# Importación de librerías necesarias
import tkinter as tk  # Librería para la creación de interfaces gráficas
from tkinter import messagebox  # Para mostrar mensajes emergentes
import folium  # Librería para crear mapas interactivos
import webbrowser  # Para abrir archivos HTML en el navegador
import os  # Para manejar rutas de archivos en el sistema

# === CLASE GRAFO Y DIJKSTRA ===

class Grafo:
    def __init__(self):
        self.vertices = {}  # Diccionario que almacenará las conexiones (aristas) entre ciudades

    def agregar_arista(self, origen, destino, distancia):
        # Agrega una arista entre dos ciudades (nodos) con una distancia
        self.vertices.setdefault(origen, []).append((destino, distancia))
        self.vertices.setdefault(destino, []).append((origen, distancia))  # Arista bidireccional

    def vecinos(self, nodo):
        # Devuelve la lista de vecinos (ciudades conectadas) de un nodo
        return self.vertices.get(nodo, [])

def dijkstra(grafo, inicio, fin):
    # Algoritmo de Dijkstra para encontrar el camino más corto
    import heapq  # Cola de prioridad para seleccionar el nodo más cercano
    distancias = {nodo: float('inf') for nodo in grafo.vertices}  # Inicializa todas las distancias como infinitas
    distancias[inicio] = 0  # La distancia al nodo inicial es 0
    anteriores = {}  # Diccionario para reconstruir el camino
    cola = [(0, inicio)]  # Cola con tuplas de (distancia, nodo)

    while cola:
        actual_dist, actual_nodo = heapq.heappop(cola)  # Extrae el nodo más cercano

        if actual_nodo == fin:
            break  # Si llegamos al destino, detenemos el algoritmo

        for vecino, peso in grafo.vecinos(actual_nodo):
            nueva_dist = actual_dist + peso
            if nueva_dist < distancias[vecino]:  # Si encontramos un camino más corto
                distancias[vecino] = nueva_dist
                anteriores[vecino] = actual_nodo
                heapq.heappush(cola, (nueva_dist, vecino))  # Añadimos a la cola de prioridad

    # Reconstrucción del camino desde el final al inicio
    camino = []
    actual = fin
    while actual in anteriores:
        camino.insert(0, actual)
        actual = anteriores[actual]
    if camino:
        camino.insert(0, inicio)  # Añade el inicio al principio del camino
    return camino

def crear_grafo_guatemala():
    # Crea un grafo con ciudades y distancias entre ellas
    grafo = Grafo()
    grafo.agregar_arista("Retalhuleu", "Mazatenango", 30)
    grafo.agregar_arista("Mazatenango", "San Felipe", 15)
    grafo.agregar_arista("San Felipe", "Quetzaltenango", 25)
    grafo.agregar_arista("Retalhuleu", "Quetzaltenango", 60)
    grafo.agregar_arista("Mazatenango", "Quetzaltenango", 50)
    grafo.agregar_arista("San Felipe", "Coatepeque", 20)
    grafo.agregar_arista("Coatepeque", "Quetzaltenango", 30)
    return grafo

# === INTERFAZ GRÁFICA ===

class PlanificadorRutas:
    def __init__(self, master):
        self.master = master
        self.master.title("Planificador de Rutas con Grafos y Mapa")
        self.paquetes = []  # Lista para almacenar los paquetes a entregar

        # Entradas y etiquetas para ciudad de origen
        tk.Label(master, text="Ciudad de origen:").grid(row=0, column=0, sticky="e")
        self.origen_entry = tk.Entry(master, width=50)
        self.origen_entry.grid(row=0, column=1, padx=10, pady=5)
        self.origen_entry.insert(0, "Retalhuleu")

        # Entradas y etiquetas para ciudad de destino
        tk.Label(master, text="Ciudad de destino final:").grid(row=1, column=0, sticky="e")
        self.destino_entry = tk.Entry(master, width=50)
        self.destino_entry.grid(row=1, column=1, padx=10, pady=5)
        self.destino_entry.insert(0, "Quetzaltenango")

        # Entrada para nombre del destinatario
        tk.Label(master, text="Nombre del destinatario:").grid(row=2, column=0, sticky="e")
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.grid(row=2, column=1, padx=10, pady=5)

        # Entrada para dirección de entrega
        tk.Label(master, text="Dirección de entrega:").grid(row=3, column=0, sticky="e")
        self.direccion_entry = tk.Entry(master, width=50)
        self.direccion_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botón para agregar paquete
        tk.Button(master, text="Agregar Paquete", command=self.agregar_paquete).grid(row=4, column=1, sticky="e", pady=5)

        # Lista de paquetes agregados
        self.lista_paquetes = tk.Listbox(master, width=80)
        self.lista_paquetes.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Botón para planificar la ruta
        tk.Button(master, text="Planificar Ruta", command=self.planificar_ruta).grid(row=6, column=1, sticky="e", pady=10)

    def agregar_paquete(self):
        # Agrega un paquete a la lista si los campos no están vacíos
        nombre = self.nombre_entry.get().strip()
        direccion = self.direccion_entry.get().strip()

        if nombre and direccion:
            self.paquetes.append((nombre, direccion))
            self.lista_paquetes.insert(tk.END, f"{nombre} - {direccion}")
            self.nombre_entry.delete(0, tk.END)
            self.direccion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor llena todos los campos del paquete.")

    def planificar_ruta(self):
        # Función principal para calcular la ruta óptima
        origen = self.origen_entry.get().strip()
        destino = self.destino_entry.get().strip()
        direcciones = [direccion for _, direccion in self.paquetes]

        if not origen or not destino or not direcciones:
            messagebox.showerror("Error", "Debes ingresar origen, destino y al menos un paquete.")
            return

        grafo = crear_grafo_guatemala()
        puntos = [origen] + direcciones + [destino]

        def normalizar(nombre):
            return nombre.lower().replace(", guatemala", "").strip()

        # Normaliza y mapea los nombres de ciudades
        puntos_norm = [normalizar(p) for p in puntos]
        vertices_norm = {normalizar(ciudad): ciudad for ciudad in grafo.vertices}

        ruta_total = []
        for punto in puntos_norm:
            if punto not in vertices_norm:
                messagebox.showerror("Error", f"La ciudad '{punto}' no está en el grafo definido.")
                return
            ruta_total.append(vertices_norm[punto])

        # Calcular ruta óptima entre todos los puntos (origen → direcciones → destino)
        resultado = [ruta_total[0]]
        actual = ruta_total[0]

        for siguiente in ruta_total[1:]:
            subruta = dijkstra(grafo, actual, siguiente)
            if not subruta:
                messagebox.showerror("Ruta no encontrada", f"No se pudo encontrar una ruta entre {actual} y {siguiente}")
                return
            resultado += subruta[1:]
            actual = siguiente

        # Mostrar ruta textual al usuario
        ruta_texto = " → ".join(resultado)
        messagebox.showinfo("Ruta calculada", f"Ruta óptima:\n{ruta_texto}")

        # Coordenadas ficticias para cada ciudad (para mostrar en el mapa)
        coordenadas_ciudades = {
            "Retalhuleu": (14.5345, -91.6778),
            "Mazatenango": (14.5333, -91.5000),
            "San Felipe": (14.6167, -91.4500),
            "Quetzaltenango": (14.8341, -91.5182),
            "Coatepeque": (14.7000, -91.8667)
        }

        # Crear mapa con Folium centrado en la ciudad de inicio
        mapa = folium.Map(location=coordenadas_ciudades.get(resultado[0], [14.5, -91.5]), zoom_start=10)

        # Añadir marcadores y líneas al mapa
        puntos_mapa = []
        for ciudad in resultado:
            coord = coordenadas_ciudades.get(ciudad)
            if coord:
                folium.Marker(coord, tooltip=ciudad).add_to(mapa)
                puntos_mapa.append(coord)

        if len(puntos_mapa) > 1:
            folium.PolyLine(puntos_mapa, color="blue", weight=3).add_to(mapa)

        # Guardar mapa como HTML y abrirlo en el navegador
        ruta_archivo = "ruta_optima.html"
        mapa.save(ruta_archivo)
        webbrowser.open('file://' + os.path.realpath(ruta_archivo))

# === EJECUTAR APLICACIÓN ===

if __name__ == "__main__":
    # Punto de entrada de la aplicación: crear ventana principal y ejecutar loop de Tkinter
    root = tk.Tk()
    app = PlanificadorRutas(root)
    root.mainloop()
