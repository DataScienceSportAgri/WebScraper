import tkinter as tk


def orientation_window():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Sélection d'application")

    # Utilisation de StringVar pour stocker app_used
    app_used = tk.StringVar()

    # Fonction pour mettre à jour la variable app_used et fermer la fenêtre
    def set_app_used(app_name):
        app_used.set(app_name)
        root.quit()
        root.destroy()

    # Création des boutons
    btn_config = tk.Button(root, text="configuration_app", command=lambda: set_app_used("configuration_app"))
    btn_scraping = tk.Button(root, text="scraping_app", command=lambda: set_app_used("scraping_app"))

    # Placement des boutons dans la fenêtre
    btn_config.pack(pady=10)
    btn_scraping.pack(pady=10)

    # Lancement de la boucle principale de l'interface
    root.mainloop()

    # Retourner la valeur de app_used
    return app_used.get()
