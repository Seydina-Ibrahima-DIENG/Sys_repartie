# Image de base légère avec Python
FROM python:3.9-slim

# Dossier où le code vivra dans le conteneur
WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Commande pour lancer l'API
CMD ["python", "app.py"]
