import json

# Chemin vers votre fichier JSON
chemin_fichier_json = 'erreur.json'

# Charger le fichier JSON
with open(chemin_fichier_json, 'r') as fichier:
    data = json.load(fichier)

# Ajouter 38 à la valeur de l'index
for element in data:
    element['Index'] += 39

# Enregistrer les modifications dans le fichier JSON
with open('votre_fichier_modifie.json', 'w') as fichier_modifie:
    json.dump(data, fichier_modifie, indent=2)

print('La valeur de l\'index a été mise à jour avec succès.')
