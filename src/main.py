

from scraper import fetch_best_seller, extraction_info, extraction_dataframe

url = 'https://www.imdb.com/list/ls055386972/'  # URL de la lista de películas
soup = fetch_best_seller(url)
extraction_dataframe(soup)

