
# Scraping Best-seller films

Ce projet est conçu pour réaliser du scraping de données afin de récupérer les best-sellers des 50 films les plus vus d'un site et les stocker dans un fichier CSV.

## Structure du Projet

```bash 
proyecto-scraping/
├── README.md          # Información sobre el proyecto
├── requirements.txt   # Dependencias del proyecto
├── src/               # Código fuente
│   ├── main.py        # Script principal
│   ├── scraper.py     # Lógica de scraping
│   └── utils.py       # Funciones auxiliares
├── data/              # Datos extraídos
│   └── output.csv     # Archivo de salida
├── logs/              # Archivos de registro
│   └── scraper.log    # Registros del scraping
└── tests/             # Pruebas del proyecto
    └── test_scraper.py
```
## Environnement Virtuel

Pour créer un environnement virtuel, utilisez la commande suivante :

```bash
python -m venv .venv
```
`.venv` est le nom de l'environnement virtuel.

### Se connecter à l'environnement virtuel

Pour activer l'environnement virtuel, utilisez la commande suivante selon votre système d'exploitation :

- **mac/linux** : 
  ```bash
  source .venv/bin/activate.fish
  ```
- **windows** : 
  ```bash
  .venv/Scripts/activate
  ```
  ou
  ```bash
  .venv/Scripts/activate.ps1
  ```

### Désactiver l'environnement virtuel

Pour désactiver l'environnement virtuel, utilisez la commande suivante :

```bash
deactivate
```