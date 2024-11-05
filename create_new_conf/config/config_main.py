from balise import Balise
class Config:
    def __init__(self, nom: str):
        self.nom = nom
        self.balises = []

    def ajouter_balise(self, balise: Balise):
        self.balises.append(balise)

    def trouver_positions(self, html: str) -> dict:
        positions = {}
        for balise in self.balises:
            positions[balise.nom] = balise.trouver_position(html)
        return positions

from bs4 import BeautifulSoup

# Supposons que nous avons le HTML suivant
html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="fr">

<head>
	
	<title>les Résultats des Compétitions</title>
	

<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<link rel="stylesheet" href="/css/v3/main.css" type="text/css" />
<link rel="stylesheet" href="/css/v3/listing.css?v=1" type="text/css" />


    <script language="javascript" src="/javascript/v3/jquery-1.9.1.min.js" type="text/javascript"></script>
    <script language="javascript" src="/javascript/v3/refresh.js" type="text/javascript"></script>

</head>

<body onload="mainThrowOnLoadEvents()">

    <div id="ctnMain">
    
        <div id="ctnTop"><div style="margin-bottom:15px;height:92px;overflow:hidden;text-align:center"><a onclick="countClick(47)" href="http://athletismemagazine.athle.fr" target="_blank"><img src="/upload/marketing/2024/athlemag-v728-90.jpg" width="728px" height="90px" alt="" class="picsNoRoll" /></a></div></div>

        <div id="ctnContent">

            <div class="titles" style="background:url('/images/v3/pic.performance.png') no-repeat; margin-bottom:15px; padding-left:80px"><span style="font-family:FaktSlabConProLight">les Résultats</span> des Compétitions</div>

            <div style="float:left;font-family:FaktSlabSemiBold;font-size:13px;margin:0 10px 5px 0"><img src="/images/v3/pic.nav.inv.png" alt="" style="margin-right:5px;height:10px;width:8px" /><a class="black" href="/asp.net/accueil.aspx?frmbase=resultats&frmmode=1&frmespace=0">RECHERCHER</a></div><div style="float:left;font-family:FaktSlabSemiBold;font-size:13px;margin:0 10px 5px 0"><img src="/images/v3/pic.nav.inv.png" alt="" style="margin-right:5px;height:10px;width:8px" /><a class="black" href="/asp.net/accueil.aspx?frmbase=resultats&frmmode=0&frmespace=0">LISTE</a></div><div style="float:right;font-family:FaktSlabSemiBold;font-size:13px;margin-bottom:5px;text-align:right;position:relative"><a class="black" href="javascript:SlideDiv('navigation', 600)">NAVIGATION</a><img src="/images/v3/pic.nav.png" alt="" style="margin-left:5px;height:10px;width:8px" /><div id="navigation" style="background-color:#FFF;display:none;position:absolute;right:0px;border:solid 2px #A00014;padding:5px 10px;white-space:nowrap"><div style="padding:1px"><a class="black" href="https://www.athle.fr">Accueil Athle.fr</a></div><div class="lineRed" style="margin:3px 0px"></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=calendrier">Le Calendrier des compétitions</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=evenements">Le Calendrier des formations</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=resultats">Les Résultats</a></div><div style="padding:1px"><a class="black" href="https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=5268">Les Bilans</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=podiums">Les Podiums</a></div><div style="padding:1px"><a class="black" href="https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=2117">Les Records</a></div><div style="padding:1px"><a class="black" href="https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=5260">Le Classement des Clubs</a></div><div style="padding:1px"><a class="black" href="https://www.athle.fr/asp.net/main.html/html.aspx?htmlid=2149">La Vitesse au Km</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=criteriums">Les Challenges et Critériums</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=coupe">Les Challenges Running</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=qualifies">Les Qualifié(e)s</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=selections">Les Internationaux</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=biographies">Les Biographies</a></div><div style="padding:1px"><a class="black" href="/asp.net/accueil.aspx?frmbase=contacts">Les Contacts</a></div></div></div>
<div class="clearer"></div>
            <div class="lineRed" style="height:5px"></div>
<table cellpadding="0" cellspacing="0" class="barContainer">
</table>
<table cellpadding="0" cellspacing="0" id="ctnResultats">
<tr><td colspan="17"><div class="mainheaders">24/11/19 - 10 km de la St Nicolas<br/><span style="font-size:13px">NANCY - G-E - 054 - Label National</span></div></td></tr>
<tr><td colspan="17">
<table cellpadding="0" cellspacing="0"><tr>
<td class="barLink">>>&nbsp;<a class="black" href="javascript:mainPopupParameters('Statistiques','/asp.net/statscompetitions.aspx?frmcompetition=219184',true,820,700,true)">Statistiques</a></td><td class="barLink" style="text-align:right"><a class="black" href="javascript:mainPopupParameters('Jury','/asp.net/jury.aspx?frmcompetition=219184',true,820,700,true)">Jury</a>&nbsp;<<</td></tr></table>
</td></tr>
<tr><td colspan="17" class="submainheaders">
      Athlètes, pensez à donner votre n° de licence, lors de l'inscription, aux organisateurs pour les exploitations (lien et alimentation de votre fiche personnelle, qualification aux Chpts de France, classement des clubs, bilans, records, etc... )
      </td></tr>
<tr><td colspan="17" class="submainheaders" style="text-align:right">Société de Chronométrie : CHRONOPRO - <a href="http://chronopro.net/" target="_blank">chronopro.net/</a> - <a href="mailto:bagraph@chronopro.net">Email</a></td></tr>
<tr><td colspan="17"><div class="subheaders"><a class="white" title="Records principaux pour cette épreuve" href="/asp.net/liste.aspx?frmbase=records&frmmode=2&frmespace=0&frmcompetition=219184&frmepreuve=261&frmsexe=M&frmserie=10 Km Route">10 Km Route</a> | 10 Km Route | Chr : M | 10000 m</div></td></tr>
<tr><td class="datas0">251</td><td class="separator3"></td><td class="datas0"><b>38'31''</b> (38'27'')</td><td class="separator3"></td><td class="datas0"><a href="javascript:bddThrowAthlete('resultats', 113592, 0)">BIGEREL Clement</a></td><td class="separator3"></td><td class="datas0"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&pardisplay=1&frmespace=0&frmcompetition=219184&frmclub=054020">Us Toul Athletisme</a></td><td class="separator3"></td><td class="datas0"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&FrmDepartement=054">054</a></td><td class="separator3"></td><td class="datas0"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&FrmLigue=G-E">G-E</a></td><td class="separator3"></td><td class="datas0"><a title="Résultats pour la catégorie du participant" href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&frmepreuve=10 Km Route&frmcategorie=M0&frmsexe=M">M0M</A>/81</td><td class="separator3"></td><td class="datas0">R6</td><td class="separator3"></td><td class="datas0">&nbsp;</td></tr>
<tr><td class="datas1">252</td><td class="separator3"></td><td class="datas1"><b>38'31''</b> (38'25'')</td><td class="separator3"></td><td class="datas1"><a href="javascript:bddThrowAthlete('resultats', 15566226, 0)">DRELON Arno</a></td><td class="separator3"></td><td class="datas1"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&pardisplay=1&frmespace=0&frmcompetition=219184&frmclub=054031">Dombasle Athletisme</a></td><td class="separator3"></td><td class="datas1"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&FrmDepartement=054">054</a></td><td class="separator3"></td><td class="datas1"><a href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&FrmLigue=G-E">G-E</a></td><td class="separator3"></td><td class="datas1"><a title="Résultats pour la catégorie du participant" href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&frmepreuve=10 Km Route&frmcategorie=CA&frmsexe=M">CAM</A>/04</td><td class="separator3"></td><td class="datas1">R6</td><td class="separator3"></td><td class="datas1">&nbsp;</td></tr>
<tr><td class="datas0">253</td><td class="separator3"></td><td class="datas0"><u><b>38'33''</b></u> (38'23'')</td><td class="separator3"></td><td class="datas0">WITZ Sylvain</td><td class="separator3"></td><td class="datas0">Univ Lorraine - Ensgsi Nancy</td><td class="separator3"></td><td class="datas0">&nbsp;</td><td class="separator3"></td><td class="datas0">&nbsp;</td><td class="separator3"></td><td class="datas0"><a title="Résultats pour la catégorie du participant" href="/asp.net/liste.aspx?frmbase=resultats&frmmode=1&frmespace=0&frmcompetition=219184&frmepreuve=10 Km Route&frmcategorie=SE&frmsexe=M">SEM</A>/97</td><td class="separator3"></td><td class="datas0">R6</td><td class="separator3"></td><td class="datas0">&nbsp;</td></tr>
"""

from bs4 import BeautifulSoup

# Supposons que le HTML soit stocké dans la variable 'html'

soup = BeautifulSoup(html, 'html.parser')

# Trouver toutes les lignes de résultats
rows = soup.find_all('tr')

results = []

for row in rows:
    # Vérifier si la ligne contient des données de coureur
    cells = row.find_all('td', class_=['datas0', 'datas1'])
    if cells and len(cells) >= 5:
        # Extraire le temps
        time_cell = cells[1]
        time = time_cell.b.text.strip() if time_cell.b else ''
        if not time and time_cell.u:
            time = time_cell.u.b.text.strip() if time_cell.u.b else ''

        # Extraire le nom
        name_cell = cells[2]
        name = name_cell.a.text.strip() if name_cell.a else name_cell.text.strip()

        # Si on a trouvé un temps et un nom, les ajouter aux résultats
        if time and name:
            results.append({'name': name, 'time': time})

# Afficher les résultats
for result in results:
    print(f"Nom: {result['name']}, Temps: {result['time']}")