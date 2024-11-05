from bs4 import BeautifulSoup
from typing import List, Optional


class Balise:
    def __init__(self, nom: str, type: str, pattern: Optional[str] = None):
        self.nom = nom
        self.type = type  # 'fixe' ou 'variable'
        self.pattern = pattern

    def trouver_position(self, html: str) -> List[int]:
        soup = BeautifulSoup(html, 'html.parser')
        positions = []

        if self.type == 'fixe':
            elements = soup.find_all(self.nom)
        elif self.type == 'variable' and self.pattern:
            elements = soup.find_all(self.nom, string=lambda text: self.pattern in text if text else False)
        else:
            return positions

        for element in elements:
            positions.append(len(str(soup).split(str(element))[0]))

        return positions