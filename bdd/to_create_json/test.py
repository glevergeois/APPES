contenu_complet = """Decapoda Austropotamobius torrentium Écrevisse des torrents CR DD
Decapoda Astacus astacus Écrevisse à pattes rouges EN VU
Decapoda Gallocaris inermis Crevette cavernicole X VU NE
Decapoda Austropotamobius pallipes Écrevisse à pattes blanches VU EN
Decapoda Atyaephyra desmaresti Caridine de Desmarest LC NE"""
contenu_complet = contenu_complet.replace('é', 'e').replace('\u00c3\u00a9', 'e').replace('\u00e8', 'e').replace('EX', 'Ex').replace('RE', 'Re').replace('CR', 'Cr').replace('EN', 'En').replace('VU', 'Vu').replace('NT', 'Nt').replace('LC', 'Lc').replace('DD', 'Dd').replace('NA', 'Na').replace('NE', 'Ne').replace('', 'Downa').replace('', 'Uppera').replace('', 'Stilla')

categorie = 'crustaces'
sous_categorie = 'decapode'
clrm = 'NULL'
tendance = 'NULL'

def add_X(texte):
    lignes = texte.split('\n')  # Divise le texte en lignes

    for index, ligne in enumerate(lignes, start=714):
        mots = ligne.split()
        nouveaux_mots = [str(index)]
        count = 0

        for mot in mots:
            if mot.lower() == 'de':
                nouveaux_mots.append('_de_')
                count += 1
            elif mot.lower() == 'du':
                nouveaux_mots.append('_du_')
                count += 1
            elif mot.lower() == 'des':
                nouveaux_mots.append('_des_')
                count += 1
            elif (not mot[0].isupper() and not nouveaux_mots[-1][-1].isupper() and 
                not mot.endswith('?') and not mot.startswith("'")):
                nouveaux_mots[-1] += '_' + mot
            elif (mot[0].isupper() and nouveaux_mots[-1].endswith('_')):
                nouveaux_mots[-1] += mot
            else:
                nouveaux_mots.append("\\t" + mot)

        nouveaux_mots.append('\\t' + tendance)
        # nouveaux_mots.append('\\t' + clrm)
        nouveaux_mots.append('\\t' + categorie)
        nouveaux_mots.append('\\t' + sous_categorie)

        if len(nouveaux_mots) >= 1:
            if nouveaux_mots[(4 + int(count))] == '\\tX':
                nouveaux_mots.pop(4 +int(count))
                nouveaux_mots.append('\\tX')

        lignes[index-714] = ' '.join(nouveaux_mots)
        
    resultat = '\n'.join(lignes)
    resultat = resultat.replace('__', '_').replace(' ', '')

    return resultat

added_x = add_X(contenu_complet)
output_file = 'test.txt'


with open(output_file, 'w', encoding='utf-8') as file:
    file.write(added_x)
