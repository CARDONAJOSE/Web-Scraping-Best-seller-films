import requests
from bs4 import BeautifulSoup
from utils import impression_extrac
import pandas as pd

url = 'https://www.chasse-aux-livres.fr/best-sellers'

def fetch_best_seller(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/',
        '^sec-ch-ua': '^\\^Google',
        '^sec-ch-ua-arch': '^\\^x86^\\^^',
        '^sec-ch-ua-bitness': '^\\^64^\\^^',
        '^sec-ch-ua-full-version-list': '^\\^Google',
        'sec-ch-ua-mobile': '?0',
        '^sec-ch-ua-model': '^\\^^\\^^',
        '^sec-ch-ua-platform': '^\\^Windows^\\^^',
        '^sec-ch-ua-platform-version': '^\\^10.0.0^\\^^',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    print(response.status_code)
    return soup

def extraction_info(soup):
    table= soup.find('li', class_= 'ipc-metadata-list-summary-item')
    #films= table.find_all('div', class_="sc-54004b59-3 eOhSkH dli-parent")
    for film in table:
        print(film.find('div', class_ = "ipc-title").find('a').find('h3').text)
        metadata= film.find('div', class_ = "sc-300a8231-6 dBUjvq dli-title-metadata")
        anne=metadata.find_all('span', class_='sc-300a8231-7 eaXxft dli-title-metadata-item')[0].text.strip()
        dure=metadata.find_all('span', class_='sc-300a8231-7 eaXxft dli-title-metadata-item')[1].text.strip()
        directeur=film.find('a', class_="ipc-link ipc-link--base dli-director-item").text
        acteurs=film.find_all('a', class_="ipc-link ipc-link--base dli-cast-item")[0].text
        acteurs_1=film.find_all('a', class_="ipc-link ipc-link--base dli-cast-item")[1].text
        acteurs_2=film.find_all('a', class_="ipc-link ipc-link--base dli-cast-item")[2].text
        #img=film.find('div', class_ = "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--media-radius ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img").find('img', class_ = "ipc-image").find('src=')
        img=film.find('img', class_ = "ipc-image").get('src')

        impression_extrac(anne, dure, directeur, acteurs, acteurs_1, acteurs_2, img)

def extraction_dataframe(soup):
# creation de list pour garde le resultat de chaque variable
    titre=[]
    année=[]
    dure=[]
    directeur=[]
    acteurs=[]
    url_img=[]

#iteration la jusqua dexieme page pour recuperer le 50 livres
    for page in range(2):
        table= soup.find_all('li', class_= 'ipc-metadata-list-summary-item')
        for film in table:
            title=film.find('div', class_ = "ipc-title").find('a').find('h3').text
            metadata= film.find('div', class_ = "sc-300a8231-6 dBUjvq dli-title-metadata")
            anne=metadata.find_all('span', class_='sc-300a8231-7 eaXxft dli-title-metadata-item')[0].text.strip()
            duration=metadata.find_all('span', class_='sc-300a8231-7 eaXxft dli-title-metadata-item')[1].text.strip()
            director=film.find('a', class_="ipc-link ipc-link--base dli-director-item").text
            acteurs_elements = film.find_all('a', class_="ipc-link ipc-link--base dli-cast-item")
            actors = [acteur.text for acteur in acteurs_elements[:3]]
            img=film.find('img', class_ = "ipc-image").get('src')

# ajoute le resulta a chaque liste
            titre.append(title)
            année.append(anne)
            dure.append(duration)
            directeur.append(director)
            acteurs.append(actors)
            url_img.append(img)

# creation du dicitionaire et dataframe pour transforme les liste dans un tableau
    df_films = pd.DataFrame({
        'Titre': titre,
        'Année': année,
        'Durée': dure,
        'Directeur': directeur,
        'Acteurs': acteurs,
        'url':url_img
    })
    print("\nNombre de films récupérés:", len(df_films))
    df_films.to_csv("data/top_films.csv", index=False)
    return df_films
