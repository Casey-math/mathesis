#!/bin/bash

# Aller dans le répertoire du projet
cd /home/john/mathesis || exit

# Synchroniser avec le dépôt distant
git pull origin main

# Ajouter les changements locaux
git add .

# Faire un commit
git commit -m "Mise à jour rapide du site"

# Pousser les changements vers le dépôt distant
git push origin main

