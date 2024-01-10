contenu_complet = """Squatinidae Squatina squatina Ange de mer commun CR ? CR
Centrophoridae Centrophorus granulosus Requin-chagrin EN ? VU
Centrophoridae Centrophorus squamosus Squale-chagrin de l'Atlantique EN ? VU
Lamnidae Lamna nasus Requin-taupe commun EN ? VU
Squalidae Squalus acanthias Aiguillat commun EN ? VU
Cetorhinidae Cetorhinus maximus Requin-pèlerin VU ? VU
Carcharhinidae Prionace glauca Requin peau bleue NT  NT
Etmopteridae Centroscyllium fabricii Aiguillat noire NT ? LC
Scyliorhinidae Galeus melastomus Chien espagnol LC  LC
Scyliorhinidae Scyliorhinus canicula Petite roussette LC  LC
Scyliorhinidae Scyliorhinus stellaris Grande roussette LC  NT
Alopiidae Alopias vulpinus Requin-renard commun DD ? VU
Carcharhinidae Carcharhinus brachyurus Requin cuivré DD ? NT
Carcharhinidae Carcharhinus brevipinna Requin-tisserand DD ? NT
Carcharhinidae Carcharhinus limbatus Requin bordé DD ? NT
Carcharhinidae Carcharhinus plumbeus Requin gris DD ? VU
Centrophoridae Deania calcea Squale-savate DD ? LC
Chlamydoselachidae Chlamydoselachus anguineus Requin-lézard DD ? NT
Dalatiidae Centroscymnus coelolepis Pailona commun DD ? NT
Dalatiidae Dalatias licha Squale-liche DD ? NT
Dalatiidae Scymnodon ringens Squale-grogneur commun DD ? DD
Dalatiidae Squaliolus laticaudus Squale nain DD ? LC
Echinorhinidae Echinorhinus brucus Squale bouclé DD ? DD
Etmopteridae Etmopterus princeps Sagre rude DD ? DD
Etmopteridae Etmopterus spinax Sagre commun DD ? LC
Hexanchidae Heptranchias perlo Perlon DD ? NT
Hexanchidae Hexanchus griseus Griset DD ? NT
Lamnidae Carcharodon carcharias Grand requin blanc DD ? VU
Mitsukurinidae Mitsukurina owstoni Requin-lutin DD ? LC
Odontaspididae Carcharias taurus Requin-taureau DD ? VU
Odontaspididae Odontaspis ferox Requin-féroce DD ? VU
Oxynotidae Oxynotus centrina Centrine commune DD ? VU
Oxynotidae Oxynotus paradoxus Humantin DD ? DD
Pseudotriakidae Pseudotriakis microdon Requin à longue dorsale DD ? DD
Scyliorhinidae Apristurus melanoasper Holbiche noire DD ? DD
Somniosidae Centroselachus crepidater Pailona à long nez DD ? LC
Somniosidae Somniosus microcephalus Laimargue du Groenland DD ? NT
Somniosidae Somniosus rostratus Laimargue de Méditerranée DD ? DD
Somniosidae Zameus squamulosus Squale-grogneur velouté DD ? DD
Sphyrnidae Sphyrna lewini Requin-marteau halicorne DD ? EN
Sphyrnidae Sphyrna mokarran Grand requin-marteau DD ? EN
Sphyrnidae Sphyrna zygaena Requin-marteau commun DD ? VU
Squalidae Squalus blainville Aiguillat-coq DD ? DD
Squalidae Squalus uyato Petit squale-chagrin DD ? DD
Squatinidae Squatina aculeata Ange de mer épineux DD ? CR
Squatinidae Squatina oculata Ange de mer ocellé DD ? CR
Triakidae Galeorhinus galeus Requin hâ DD ? VU
Triakidae Mustelus asterias Émissole tachetée DD ? LC
Triakidae Mustelus mustelus Émissole lisse DD ? VU
Triakidae Mustelus punctulatus Émissole pointillée DD ? DD"""
contenu_complet = contenu_complet.replace('é', 'e').replace('\u00c3\u00a9', 'e').replace('\u00e8', 'e').replace('EX', 'Ex').replace('RE', 'Re').replace('CR', 'Cr').replace('EN', 'En').replace('VU', 'Vu').replace('NT', 'Nt').replace('LC', 'Lc').replace('DD', 'Dd').replace('NA', 'Na').replace('NE', 'Ne').replace('', 'Downa').replace('', 'Uppera').replace('', 'Stilla')

categorie = 'requins'
sous_categorie = 'NULL'
clrm = 'NULL'
tendance = 'NULL'

def add_X(texte):
    lignes = texte.split('\n')  # Divise le texte en lignes

    for index, ligne in enumerate(lignes, start=2231):
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

        # nouveaux_mots.append('\\t' + tendance)
        # nouveaux_mots.append('\\t' + clrm)
        nouveaux_mots.append('\\t' + categorie)
        nouveaux_mots.append('\\t' + sous_categorie)

        if len(nouveaux_mots) >= (4 + int(count) + 1):  # Check if the index is within the valid range
            if nouveaux_mots[(4 + int(count))] == '\\tX':
                nouveaux_mots.pop(4 + int(count))
                nouveaux_mots.append('\\tX')
            else:
                nouveaux_mots.append('\\tNULL')
        else:
            nouveaux_mots.append('\\tNULL')

                
        
        
        lignes[index-2231] = ' '.join(nouveaux_mots)
        
    resultat = '\n'.join(lignes)
    resultat = resultat.replace('__', '_').replace(' ', '')

    return resultat

added_x = add_X(contenu_complet)
output_file = 'test.txt'


with open(output_file, 'w', encoding='utf-8') as file:
    file.write(added_x)
