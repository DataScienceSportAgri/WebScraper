import sqlite3

def save_to_db(interest_element_scraped):
    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Insertion des données dans la table
    insert_query = '''
    INSERT INTO important_elements (distance, annee, temps, nom, prenom, temps_scratch, temps_reel, classement)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(insert_query, (
        interest_element_scraped.distance,
        interest_element_scraped.annee,
        interest_element_scraped.temps,
        interest_element_scraped.nom,
        interest_element_scraped.prenom,
        interest_element_scraped.temps_scratch,
        interest_element_scraped.temps_reel,
        interest_element_scraped.classement
    ))

    # Commit et fermeture de la connexion
    conn.commit()
    conn.close()

# Exemple d'utilisation
# Supposons que interest_element_scraped est un objet avec les attributs appropriés
# save_to_db(interest_element_scraped)