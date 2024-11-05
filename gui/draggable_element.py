import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import html

class YourCustomClass:
    def __init__(self, content):
        self.soup = BeautifulSoup(content, 'html.parser')
        self.balise = self.soup.tag

    def get_in(self, level):
        res = self.soup.find_all(recursive=False)
        test = BeautifulSoup(res[0], 'html.parser')
        if test != self.soup:
            return self.soup.find_all(recursive=False)
        else:
            return [tag for parent in self.soup.find_all(recursive=False)
                    for tag in parent.find_all(recursive=False)]


class DraggableObject:
    def __init__(self, canvas, x, y, width, height, htmlParsed, regenerate_callback):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.htmlParsed = htmlParsed
        self.rect = None
        self.label = None
        self.button = None
        self.regenerate_callback = regenerate_callback

    def display(self):
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="lightblue", tags="draggable")
        self.label = self.canvas.create_text(self.x + 10, self.y + 10, text=self.htmlParsed[:20], anchor="nw")
        self.button = self.canvas.create_window(self.x + 10, self.y + 40, window=tk.Button(self.canvas, text="Explorer", command = self.explorer), anchor="se")
        self.button = self.canvas.create_window(self.x + 10, self.y + 40,
                                                window=tk.Button(self.canvas, text="Voir", command = self.voir), anchor="se")

        self.canvas.tag_bind(self.rect, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)

    def explorer(self):
        # Appeler la fonction de rappel avec le HTML de cet élément
        self.regenerate_callback(self.htmlParsed)

    def voir(self):
        # Créer une nouvelle fenêtre
        view_window = tk.Toplevel(self.canvas.master)
        view_window.title("Contenu HTML")
        view_window.geometry("600x400")

        # Créer un frame avec scrollbar
        main_frame = ttk.Frame(view_window)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Créer un canvas
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Ajouter une scrollbar au canvas
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configurer le canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Créer un frame à l'intérieur du canvas
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Ajouter le contenu HTML dans un widget Text
        text_widget = tk.Text(inner_frame, wrap=tk.WORD, width=80, height=20)
        text_widget.pack(padx=10, pady=10)

        # Insérer le contenu HTML échappé
        escaped_html = html.escape(self.htmlParsed)
        text_widget.insert(tk.END, escaped_html)

        # Rendre le widget Text en lecture seule
        text_widget.configure(state='disabled')

        # Ajouter un bouton pour fermer la fenêtre
        close_button = ttk.Button(view_window, text="Fermer", command=view_window.destroy)
        close_button.pack(pady=10)

        # Mettre à jour la géométrie de la fenêtre
        view_window.update_idletasks()
        view_window.geometry(f"{min(view_window.winfo_width(), 800)}x{min(view_window.winfo_height(), 600)}")

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.label, dx, dy)
        self.canvas.move(self.button, dx, dy)
        self.start_x = event.x
        self.start_y = event.y



