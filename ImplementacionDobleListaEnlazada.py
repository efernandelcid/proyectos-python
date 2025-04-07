import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = self.current_node = new_node
        else:
            if self.current_node and self.current_node.next:
                temp = self.current_node.next
                while temp:
                    next_temp = temp.next
                    temp.prev = temp.next = None
                    temp = next_temp
                self.current_node.next = None
                self.tail = self.current_node

            self.current_node.next = new_node
            new_node.prev = self.current_node
            self.tail = new_node
            self.current_node = new_node

    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                if self.current_node == node:
                    self.current_node = node.prev if node.prev else node.next
                break
            node = node.next

    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev

    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next

    def current(self):
        return self.current_node.value if self.current_node else ""

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto con Historial")
        self.history = DoublyLinkedList()

        self.text_area = tk.Text(root, wrap="word", height=20, width=60)
        self.text_area.pack(padx=10, pady=10)

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=5)

        self.save_btn = ttk.Button(button_frame, text="Guardar Estado", command=self.save_state)
        self.save_btn.pack(side="left", padx=5)

        self.undo_btn = ttk.Button(button_frame, text="Deshacer", command=self.undo)
        self.undo_btn.pack(side="left", padx=5)

        self.redo_btn = ttk.Button(button_frame, text="Rehacer", command=self.redo)
        self.redo_btn.pack(side="left", padx=5)

    def save_state(self):
        content = self.text_area.get("1.0", "end-1c")
        self.history.append(content)

    def undo(self):
        self.history.move_backward()
        self.update_text_area()

    def redo(self):
        self.history.move_forward()
        self.update_text_area()

    def update_text_area(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", self.history.current())

if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = TextEditor(root)
    root.mainloop()
