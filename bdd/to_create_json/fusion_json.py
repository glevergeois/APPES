import json

def fusionner_fichiers_json(fichier1, fichier2, fichier_sortie):
    # Charger les données du premier fichier JSON
    with open(fichier1, 'r') as f1:
        data1 = json.load(f1)

    # Charger les données du deuxième fichier JSON
    with open(fichier2, 'r') as f2:
        data2 = json.load(f2)

    # Fusionner les fichiers en évitant les duplicatas d'index
    index_max = max(max(data1.index()), max(data2.index()))
    data_fusionne = {}

    for i in range(1, index_max + 1):
        if i in data1:
            data_fusionne[i] = data1[i]
        if i in data2:
            data_fusionne[i] = data2[i]

    # Écrire les données fusionnées dans un nouveau fichier JSON
    with open(fichier_sortie, 'w') as f_sortie:
        json.dump(data_fusionne, f_sortie, indent=2)

# Spécifiez les noms de vos fichiers d'entrée et de sortie
fichier_json1 = '../correct_json_files/mammiferes_terrestre.json'
fichier_json2 = '../correct_json_files/poissons_eaudouce.json'
fichier_sortie = 'fusion.json'

# Appeler la fonction pour fusionner les fichiers
fusionner_fichiers_json(fichier_json1, fichier_json2, fichier_sortie)
