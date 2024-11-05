from scraper.base_scraper import BaseScraper
from gui.main_window import run_gui
from initchoice import orientation_window
from create_new_conf.create_config import config_specification
from database import init_db, save_config, get_all_configs, get_config_by_name
from Finding_data.Processing_urls import start_downloading_process
import json

def main():
    base_url = input("Entrez l'URL de base de la page de résultats : ")
    scraper = BaseScraper(base_url)
    app_used = orientation_window()
    try:
        initial_html = scraper.html_fetcher.fetch_html(base_url)
        print(f"L'application utilisée est : {app_used}")
        if app_used == 'configuration_app':
            if initial_html:
                selected_elements = run_gui(initial_html)
                if selected_elements:
                    config = config_specification(selected_elements)
                    config_name = input("Entrez un nom pour cette configuration : ")
                    save_config(config_name, json.dumps(config))
                    print(f"Configuration '{config_name}' enregistrée avec succès.")
                else:
                    print("Aucun élément n'a été sélectionné.")
            else:
                print("Impossible de récupérer le HTML de la page initiale.")
        elif app_used == 'scraping_app':
            configs = get_all_configs()
            print("Configurations disponibles :")
            for config in configs:
                print(f"- {config.name}")

            config_name = input("Entrez le nom de la configuration à utiliser : ")
            selected_config = get_config_by_name(config_name)

            if selected_config:
                config_data = json.loads(selected_config.config_data)
                # Utilisez config_data pour votre logique de scraping
                print(f"Utilisation de la configuration : {config_name}")
                print(config_data)
                runners_data = start_downloading_process(config_data)
            else:
                print("Configuration non trouvée.")
    finally:
        scraper.close()




if __name__ == '__main__':
    main()