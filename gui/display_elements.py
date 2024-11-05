import tkinter as tk

from .draggable_element import DraggableObject
from bs4 import BeautifulSoup, NavigableString, Tag

OBJECT_WIDTH = 150
OBJECT_HEIGHT = 100

def element_displaying(frame, html_content):
    # Charger le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    canvas = tk.Canvas(frame, width=300, height=200, bg="white")
    # Fonction pour obtenir les éléments de premier niveau
    def get_first_level_elements(soup):
        first_level = []
        for element in soup.children:
            if isinstance(element, NavigableString):
                if element.strip():
                    first_level.append(element.strip())
            elif isinstance(element, Tag):
                first_level.append(str(element))
        return first_level

    # Obtenir les éléments de premier niveau
    first_level_elements = get_first_level_elements(soup)

    parsedrepresentats = []

    for i, enfant in enumerate(first_level_elements):
        x = 50 + (i * (OBJECT_WIDTH + 20))  # 20 pixels d'espacement entre les objets
        y = 50
        obj = DraggableObject(canvas, x, y, OBJECT_WIDTH, OBJECT_HEIGHT, enfant,
                              lambda new_html: element_displaying(frame, new_html))
        obj.display()  # Afficher l'objet dans le canvas
        parsedrepresentats.append(obj)

    # Ajuster la région de défilement du canvas si nécessaire
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.pack()
    return parsedrepresentats