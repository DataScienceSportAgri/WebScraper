import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from .display_elements import element_displaying
from .draggable_element import DraggableObject

class RecupDataType:
    def __init__(self, category_of_data, order_of_data):
        self.category_of_data = category_of_data
        self.order_of_data = order_of_data

    def process_data(self, data):
        print(f"Traitement des données pour {self.category_of_data}")
        # Ajoutez ici la logique de traitement spécifique


class ZoneDrop(tk.Frame, TkinterDnD.DnDWrapper):
    def __init__(self, master, **kwargs):
        # Extraire les arguments personnalisés
        self.category_of_data = kwargs.pop('categorie_of_data', '')
        self.order_of_data = kwargs.pop('order_of_data', 0)

        # Initialiser le Frame parent
        tk.Frame.__init__(self, master, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        # Configuration visuelle de la zone de drop
        self.config(relief=tk.SUNKEN, borderwidth=2)
        self.label = tk.Label(self, text=f"Zone: {self.category_of_data}", fg="grey")
        self.label.pack(expand=True, fill=tk.BOTH)

        # Enregistrement pour le drag-and-drop
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop)

        # Associez votre instance de classe personnalisée ici
        self.custom_instance = RecupDataType(self.category_of_data, self.order_of_data)

    def drop(self, event):
        data = event.data
        print(f"Élément déposé dans {self.category_of_data}: {data}")
        self.custom_instance.process_data(data)

history_list = []

def retour(root):
    elements_displayed = DraggableObject()
    try:
        if len(history_list) > 1:
            history_list.pop()  # Supprime l'élément actuel
            previous_content = history_list[-1]  # Obtient le contenu précédent
            elements_displayed = element_displaying(root, previous_content)
        else:
            print('Erreur retour : premier niveau html')
    except IndexError as e:
        print('Erreur retour :', e)

    return elements_displayed

def create_widgets(root):

    # Création du cadre pour les boutons en haut
    button_frame = ttk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    # Boutons Mode et Retour
    mode_button = ttk.Button(button_frame, text="Mode: Exploration")
    mode_button.pack(side=tk.LEFT, padx=5, pady=5)

    back_button = ttk.Button(button_frame, text="Retour", command=lambda: retour(root))
    back_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Créer un cadre principal pour contenir les deux zones inférieures
    main_frame = ttk.Frame(root)
    main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Créer un cadre pour les éléments parsés qui occupe deux tiers de la fenêtre
    elements_frame = ttk.Frame(main_frame)
    elements_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Ajouter un label d'indication pour les éléments parsés
    ttk.Label(elements_frame, text='Zone des Éléments Parsés').pack(pady=20, expand=True)

    # Créer un cadre pour les catégories qui occupe un tiers de la fenêtre
    drop_zone_frame = ttk.Frame(main_frame)
    drop_zone_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
    # Ajouter un label d'indication pour les éléments parsés
    ttk.Label(drop_zone_frame, text='Zone de reception des drag and drop').pack(pady=20, expand=True)
    elements_frame.config(width=600)
    return root, drop_zone_frame, elements_frame

def create_main_window(root, html_content):

    root.title("Sélecteur d'éléments HTML")

    # Liste des catégories pour chaque ZoneDrop
    categories = ["Finisher", "Nom", "Prénom", "Temps Scratch", "Temps Réel", "Catégorie Coureur"]
    root, categories_frame, elements_frame = create_widgets(root)
    print(categories_frame)
    elements = element_displaying(elements_frame, html_content)
    print('elements', elements)
    zone_drops = []
    for categorie in categories:
        if categorie == 'Finisher':
            zone_drops.append(ZoneDrop(categories_frame, order_of_data=0, categorie_of_data=categorie, width=300, height=200, bg="white"))
        else:
            zone_drops.append(ZoneDrop(categories_frame, width=300, height=200, bg="white", order_of_data=1,
                                       categorie_of_data=categorie))
    print('zone_drops', zone_drops)
    return elements, zone_drops, root


def run_gui(html_content):
    root = TkinterDnD.Tk()
    root.geometry("900x600")
    elements, zone_drops, root = create_main_window(root, html_content)

    root.mainloop()

    return elements
